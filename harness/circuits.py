#!/usr/bin/env python3
"""
Circuitos del campeonato: variantes de MountainCar-v0 que corren TODAS con la
misma policy (el contrato del ONNX no cambia).

La física es la de gymnasium MountainCar-v0, vectorizada en numpy para correr
miles de episodios en paralelo (una sola llamada al ONNX por paso para todo el
batch). En el circuito estándar es EXACTAMENTE gymnasium: misma largada por
seed (env.reset(seed)) y mismas cuentas en float64; evaluate.py lo verifica
contra gymnasium en cada corrida (check_vs_gymnasium).

Parámetros de un circuito (config.yaml -> circuits[].params). Cada uno puede
ser un número fijo o [min, max]; si es un rango se sortea uniforme POR EPISODIO
(domain randomization), de forma determinista a partir de la seed:
  force          potencia del motor              (default 0.001)
  gravity        pendiente                       (default 0.0025)
  freq           forma de la pista: cos(freq*x)  (default 3.0)
  wind           empuje constante sobre la vel.  (default 0.0)
  goal_position  meta                            (default 0.5)
  start_pos      largada: posición               (default: la de gymnasium, U[-0.6,-0.4])
  start_vel      largada: velocidad              (default 0.0)
  obs_noise_pos  ruido gaussiano (σ) en la posición observada  (default 0.0)
  obs_noise_vel  ruido gaussiano (σ) en la velocidad observada (default 0.0)
"""
import zlib

import gymnasium as gym
import numpy as np

MIN_POS, MAX_POS, MAX_SPEED = -1.2, 0.6, 0.07

DEFAULTS = {
    "force": 0.001, "gravity": 0.0025, "freq": 3.0, "wind": 0.0,
    "goal_position": 0.5, "start_vel": 0.0,
    "obs_noise_pos": 0.0, "obs_noise_vel": 0.0,
}
KNOWN = set(DEFAULTS) | {"start_pos"}


def gym_start_positions(env_id: str, seeds: list[int]) -> np.ndarray:
    """Largada de gymnasium para cada seed (idéntica a env.reset(seed=s))."""
    env = gym.make(env_id)
    # reset devuelve la obs en float32; el estado interno es float64 -> lo leemos de ahí.
    out = []
    for s in seeds:
        env.reset(seed=s)
        out.append(float(env.unwrapped.state[0]))
    env.close()
    return np.array(out, dtype=np.float64)


def sample_params(circuit: dict, seeds: list[int], base_pos: np.ndarray, max_steps: int):
    """Arrays por episodio con los parámetros del circuito (deterministas por seed)."""
    params = circuit.get("params") or {}
    unknown = set(params) - KNOWN
    if unknown:
        raise SystemExit(f"Circuito '{circuit['id']}': parámetros desconocidos {sorted(unknown)}")

    salt = zlib.crc32(circuit["id"].encode())
    rngs = [np.random.default_rng([s, salt]) for s in seeds]
    n = len(seeds)

    def draw(name):
        v = params.get(name, DEFAULTS.get(name))
        if isinstance(v, (list, tuple)):
            lo, hi = float(v[0]), float(v[1])
            return np.array([r.uniform(lo, hi) for r in rngs])
        return np.full(n, float(v))

    p = {k: draw(k) for k in DEFAULTS}
    p["start_pos"] = draw("start_pos") if "start_pos" in params else base_pos.copy()

    # Ruido de sensores pre-generado por episodio: [n, max_steps, 2].
    if (p["obs_noise_pos"] > 0).any() or (p["obs_noise_vel"] > 0).any():
        z = np.stack([r.standard_normal((max_steps, 2)) for r in rngs])
        sig = np.stack([p["obs_noise_pos"], p["obs_noise_vel"]], axis=1)[:, None, :]
        p["noise"] = z * sig
    else:
        p["noise"] = None
    return p


def rollout(policy, p: dict, max_steps: int) -> np.ndarray:
    """Corre todos los episodios en paralelo. Devuelve el retorno de cada uno."""
    pos = p["start_pos"].astype(np.float64).copy()
    vel = p["start_vel"].astype(np.float64).copy()
    n = len(pos)
    ret = np.zeros(n)
    alive = np.ones(n, dtype=bool)
    for t in range(max_steps):
        obs = np.stack([pos, vel], axis=1)
        if p["noise"] is not None:
            obs = obs + p["noise"][:, t, :]
        action = np.argmax(policy(obs.astype(np.float32)), axis=1)
        # Mismo orden de operaciones que gymnasium MountainCarEnv.step
        new_vel = vel + (action - 1) * p["force"] + np.cos(p["freq"] * pos) * (-p["gravity"]) + p["wind"]
        new_vel = np.clip(new_vel, -MAX_SPEED, MAX_SPEED)
        new_pos = np.clip(pos + new_vel, MIN_POS, MAX_POS)
        new_vel = np.where((new_pos == MIN_POS) & (new_vel < 0), 0.0, new_vel)
        pos = np.where(alive, new_pos, pos)
        vel = np.where(alive, new_vel, vel)
        ret -= alive
        alive &= ~((pos >= p["goal_position"]) & (vel >= 0))
        if not alive.any():
            break
    return ret


def check_vs_gymnasium(policy_single, policy_batch, env_id, seeds, base_pos, max_steps, k=20):
    """Garantía: en el circuito estándar el simulador da EXACTAMENTE lo mismo que gymnasium."""
    seeds = seeds[:k]
    expected = []
    for s in seeds:
        env = gym.make(env_id, max_episode_steps=max_steps)
        obs, _ = env.reset(seed=s)
        total = 0.0
        while True:
            a = int(np.argmax(policy_single(np.asarray(obs, np.float32).reshape(1, -1))[0]))
            obs, r, term, trunc, _ = env.step(a)
            total += float(r)
            if term or trunc:
                break
        env.close()
        expected.append(total)
    p = sample_params({"id": "estandar", "params": {}}, seeds, base_pos[:k], max_steps)
    got = rollout(policy_batch, p, max_steps)
    if not np.array_equal(np.array(expected), got):
        raise SystemExit("ERROR INTERNO: el simulador vectorizado no coincide con gymnasium "
                         f"(esperado {expected[:5]}..., obtenido {got[:5].tolist()}...).")
