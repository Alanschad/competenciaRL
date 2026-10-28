#!/usr/bin/env python3
"""
Evalúa un policy.onnx sobre un conjunto de seeds, en CADA circuito del
campeonato (config.yaml -> circuits; ver harness/circuits.py).

- Política: accion = argmax(Q(obs))  (greedy, determinista).
- Una corrida (episodio) por seed -> con política y entorno deterministas,
  más seeds = más muestras. La varianza entre seeds es la señal real en RL.
- Métrica de ranking: media de los retornos, con IC 95% por bootstrap.
  (También se reporta el IQM —media del 50% central— como dato informativo.)
- IMPORTANTE: nunca imprime los valores de las seeds (son secretas).

Las seeds se pasan por la variable de entorno EVAL_SEEDS (lista separada por
comas), que en el workflow viene de un GitHub Secret. Si no está, usa
seeds/public_seeds.txt (las de práctica).

Uso:
    EVAL_SEEDS="11,22,33" python evaluate.py --onnx policy.onnx --team mi_equipo
    python evaluate.py --onnx policy.onnx --team mi_equipo --out r.json --md r.md
"""
import argparse
import json
import os
from pathlib import Path

import numpy as np
import onnxruntime as ort
import yaml

from circuits import check_vs_gymnasium, gym_start_positions, rollout, sample_params

ROOT = Path(__file__).resolve().parent.parent
CFG = yaml.safe_load((ROOT / "config.yaml").read_text())


def load_seeds() -> list[int]:
    env_seeds = os.environ.get("EVAL_SEEDS", "").strip()
    if env_seeds:
        return [int(s) for s in env_seeds.split(",") if s.strip()]
    public = ROOT / "seeds" / "public_seeds.txt"
    if public.exists():
        return [int(s) for s in public.read_text().split() if s.strip()]
    raise SystemExit("No hay seeds: definí EVAL_SEEDS o seeds/public_seeds.txt")


def make_policy(onnx_path: str):
    """Devuelve (f_batch, f_single). Si el ONNX no acepta batch>1 (batch fijo en 1),
    f_batch cae a una llamada por fila: más lento, pero evalúa igual."""
    sess = ort.InferenceSession(onnx_path, providers=["CPUExecutionProvider"])
    inp, out = CFG["input_name"], CFG["output_name"]

    def single(x):
        return sess.run([out], {inp: x})[0]

    try:
        ok = single(np.zeros((2, CFG["obs_dim"]), np.float32)).shape == (2, CFG["n_actions"])
    except Exception:  # noqa: BLE001
        ok = False
    if ok:
        return single, single
    return (lambda x: np.concatenate([single(r[None, :]) for r in x])), single


def stats(returns: np.ndarray) -> dict:
    ci_iqm = bootstrap_ci(returns, iqm, CFG["bootstrap_resamples"])
    ci_mean = bootstrap_ci(returns, np.mean, CFG["bootstrap_resamples"])
    return {
        "mean": float(returns.mean()),
        "mean_ci95": [round(ci_mean[0], 3), round(ci_mean[1], 3)],
        "std": float(returns.std(ddof=1)) if len(returns) > 1 else 0.0,
        "iqm": iqm(returns),
        "iqm_ci95": [round(ci_iqm[0], 3), round(ci_iqm[1], 3)],
        "min": float(returns.min()),
        "max": float(returns.max()),
        # Episodios que no llegaron a la meta (retorno = -max_steps).
        "fail_rate": float((returns <= -CFG["max_steps_per_episode"]).mean()),
    }


def to_markdown(result: dict) -> str:
    names = {c["id"]: c["name"] for c in CFG["circuits"]}
    lines = [
        f"| Circuito | Media | IC95 | IQM | Sin llegar a la meta |",
        f"|---|---|---|---|---|",
    ]
    for cid, r in result["circuits"].items():
        lines.append(
            f"| {names.get(cid, cid)} | {r['mean']:.3f} | [{r['mean_ci95'][0]:.2f}, {r['mean_ci95'][1]:.2f}] "
            f"| {r['iqm']:.3f} | {100 * r['fail_rate']:.1f}% |"
        )
    return "\n".join(lines) + "\n"


def iqm(x: np.ndarray) -> float:
    """Interquartile mean using pure NumPy index slicing."""
    if len(x) == 0:
        return float("nan")

    # Calculate how many elements represent 25% of the data
    drop_count = len(x) // 4

    # If the array is too small to drop elements, return the standard mean
    if drop_count == 0:
        return float(np.mean(x))

    x_sorted = np.sort(x)
    # Slice off the bottom 25% and top 25% by position
    mid = x_sorted[drop_count:-drop_count]

    return float(np.mean(mid))


def bootstrap_ci(x: np.ndarray, stat, n_resamples: int, alpha=0.05):
    rng = np.random.default_rng(0)  # IC reproducible
    boot = [stat(rng.choice(x, size=len(x), replace=True)) for _ in range(n_resamples)]
    lo = float(np.percentile(boot, 100 * alpha / 2))
    hi = float(np.percentile(boot, 100 * (1 - alpha / 2)))
    return lo, hi


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--onnx", required=True)
    p.add_argument("--team", required=True)
    p.add_argument("--out", default=None, help="ruta del result.json de salida")
    p.add_argument("--md", default=None, help="opcional: tabla markdown con el resultado")
    args = p.parse_args()

    seeds = load_seeds()
    max_steps = CFG["max_steps_per_episode"]
    f_batch, f_single = make_policy(args.onnx)
    base_pos = gym_start_positions(CFG["env_id"], seeds)
    check_vs_gymnasium(f_single, f_batch, CFG["env_id"], seeds, base_pos, max_steps)

    result = {"team": args.team, "n_episodes": len(seeds), "circuits": {}}
    for c in CFG["circuits"]:
        params = sample_params(c, seeds, base_pos, max_steps)
        returns = rollout(f_batch, params, max_steps)
        result["circuits"][c["id"]] = stats(returns)

    # No imprimimos seeds ni el detalle por-seed (info de las seeds ocultas).
    print(json.dumps(result, indent=2))

    out = args.out or str(ROOT / "results" / f"{args.team}.json")
    Path(out).parent.mkdir(parents=True, exist_ok=True)
    Path(out).write_text(json.dumps(result, indent=2))
    print(f"\nGuardado en {out}")
    if args.md:
        Path(args.md).write_text(to_markdown(result))


if __name__ == "__main__":
    main()
