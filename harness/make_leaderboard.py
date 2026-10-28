#!/usr/bin/env python3
"""
Arma LEADERBOARD.md leyendo todos los results/<equipo>.json.

Campeonato estilo F1: en cada circuito (config.yaml -> circuits) se ordena por
la métrica de ranking (mean por defecto) y se reparten puntos por posición
(config.yaml -> points). Gana quien sume más. Desempate: más primeros puestos,
después más segundos, etc.
"""
import json
from datetime import datetime, timezone
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
CFG = yaml.safe_load((ROOT / "config.yaml").read_text())
METRIC = CFG.get("rank_metric", "mean")
METRIC_LABEL = {"mean": "MEDIA", "iqm": "IQM"}.get(METRIC, METRIC.upper())
CIRCUITS = CFG["circuits"]
POINTS = CFG["points"]


def load_results() -> list[dict]:
    results = []
    for f in sorted((ROOT / "results").glob("*.json")):
        try:
            r = json.loads(f.read_text())
        except json.JSONDecodeError:
            continue
        if "circuits" not in r:
            print(f"Ignoro {f.name}: formato viejo (sin circuitos), se regenera en la próxima evaluación.")
            continue
        results.append(r)
    return results


def rank_circuit(results: list[dict], cid: str) -> list[tuple[int, dict]]:
    """[(posición, result)] ordenado. Empates exactos comparten posición."""
    rows = [r for r in results if cid in r["circuits"]]
    rows.sort(key=lambda r: r["circuits"][cid][METRIC], reverse=True)
    ranked, prev, pos = [], None, 0
    for i, r in enumerate(rows, 1):
        v = r["circuits"][cid][METRIC]
        if v != prev:
            pos, prev = i, v
        ranked.append((pos, r))
    return ranked


def points_for(pos: int) -> int:
    return POINTS[pos - 1] if pos <= len(POINTS) else 0


def main():
    results = load_results()
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    lines = [
        "# 🏆 Leaderboard — Campeonato RL (DQN)",
        "",
        f"Entorno base: `{CFG['env_id']}` · {len(CIRCUITS)} circuitos · "
        f"Ranking por **{METRIC_LABEL}** en cada circuito · Actualizado: {now}",
        "",
        f"Puntos por circuito: {', '.join(f'{p}' for p in POINTS)} (del 1° al {len(POINTS)}°). "
        "La misma policy corre en todos los circuitos. Detalle de cada uno en el README.",
        "",
    ]
    if not results:
        lines.append("_Sin submissions todavía._")
        (ROOT / "LEADERBOARD.md").write_text("\n".join(lines) + "\n")
        print("Leaderboard regenerado con 0 equipo(s).")
        return

    # Posiciones por circuito
    pos = {r["team"]: {} for r in results}
    ranked = {}
    for c in CIRCUITS:
        ranked[c["id"]] = rank_circuit(results, c["id"])
        for p, r in ranked[c["id"]]:
            pos[r["team"]][c["id"]] = p

    # Campeonato
    def champ_key(team):
        ps = [pos[team][c["id"]] for c in CIRCUITS if c["id"] in pos[team]]
        total = sum(points_for(p) for p in ps)
        # countback F1: más 1°, después más 2°, ...
        counts = tuple(-ps.count(k) for k in range(1, len(results) + 1))
        return (-total, counts)

    teams = sorted(pos, key=champ_key)
    short = [c["name"].replace("GP ", "") for c in CIRCUITS]
    lines += [
        "## 🏁 Campeonato",
        "",
        "| # | Equipo | **Pts** | " + " | ".join(short) + " |",
        "|---|--------|-----:|" + "|".join(":---:" for _ in CIRCUITS) + "|",
    ]
    medal = {1: "🥇", 2: "🥈", 3: "🥉"}
    prev_key, rank = None, 0
    for i, t in enumerate(teams, 1):
        k = champ_key(t)
        if k != prev_key:
            rank, prev_key = i, k
        cells = []
        for c in CIRCUITS:
            p = pos[t].get(c["id"])
            cells.append("—" if p is None else (f"{p}° ({points_for(p)})" if points_for(p) else f"{p}°"))
        lines.append(f"| {medal.get(rank, rank)} | {t} | **{-k[0]}** | " + " | ".join(cells) + " |")

    # Detalle por circuito
    for c in CIRCUITS:
        cid = c["id"]
        rows = ranked[cid]
        if not rows:
            continue
        leader = rows[0][1]["circuits"][cid]["mean"]
        lines += [
            "",
            f"## {c['name']}",
            "",
            f"_{c.get('desc', '')}_",
            "",
            "| # | Equipo | Pts | Media | IQM | Sin llegar | Min | Max | Episodios | Dif. al 1° |",
            "|---|--------|----:|-------|-----|-----------:|-----|-----|-----------|-----------|",
        ]
        for p, r in rows:
            m = r["circuits"][cid]
            gap = "—" if p == 1 else f"+{leader - m['mean']:.3f}"
            lines.append(
                f"| {p} | {r['team']} | {points_for(p)} | {m['mean']:.3f} | {m['iqm']:.3f} | "
                f"{100 * m['fail_rate']:.1f}% | {m['min']:.1f} | {m['max']:.1f} | {r['n_episodes']} | {gap} |"
            )

    (ROOT / "LEADERBOARD.md").write_text("\n".join(lines) + "\n")
    print(f"Leaderboard regenerado con {len(results)} equipo(s).")


if __name__ == "__main__":
    main()
