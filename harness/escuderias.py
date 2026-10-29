#!/usr/bin/env python3
"""
A qué escudería pertenece cada auto (carpeta de submissions/).

La escudería es la CUENTA DE GITHUB que abrió el PR que creó la carpeta. No se
usa el nombre de la carpeta ni el autor del commit: los dos los elige el alumno.
Se saca del mensaje del merge commit en main ("Merge pull request #N from
<cuenta>/<rama>"), cuyo <cuenta> es el dueño del fork. Por eso los PRs se
mergean con "Create a merge commit" (no squash ni rebase).

Casos raros (dos cuentas de la misma persona, una carpeta que no vino por PR)
se corrigen a mano en config.yaml -> escuderias: {carpeta: cuenta}.
"""
import re
import subprocess

MERGE_RE = re.compile(r"^Merge pull request #\d+ from ([A-Za-z0-9-]+)/")
TEAM_RE = re.compile(r"^submissions/([^/]+)/")


def escuderias(root, ref: str = "origin/main", manual: dict | None = None) -> dict[str, str]:
    """{carpeta: cuenta de GitHub} según el PR que creó cada carpeta en `ref`."""
    log = subprocess.run(
        ["git", "log", "--first-parent", "--diff-merges=first-parent", "--name-only",
         "--reverse", "--format=@@%s", ref, "--", "submissions/"],
        cwd=root, capture_output=True, text=True, check=True,
    ).stdout
    owner, current = {}, None
    for line in log.splitlines():
        if line.startswith("@@"):
            m = MERGE_RE.match(line[2:])
            current = m.group(1) if m else None
        elif current and (m := TEAM_RE.match(line)):
            owner.setdefault(m.group(1), current)  # --reverse: gana el PR que la creó
    owner.update(manual or {})
    return owner
