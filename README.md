# 🏁 Competencia RL — DQN sobre `MountainCar-v0`

<p align="center">
  <img src="gifs/mountain_car.gif" alt="Agente DQN escalando la montaña en MountainCar-v0" width="490">
</p>

> **Damas y caballeros, arranca la temporada.** Esto no es la Fórmula 1, pero el
> espíritu es el mismo: cada escudería —su equipo— lleva su propio monoplaza a la
> pista. Solo que acá el monoplaza es una **red Q entrenada** y el circuito es la
> ladera de `MountainCar-v0`. El motor sin potencia no alcanza para subir de frente:
> hay que tomar impulso, leer el momento justo y dejar que la política haga el resto.
>
> No gana quien tiene el auto más rápido, sino quien **llega a la cima en menos pasos**
> y de forma **consistente vuelta tras vuelta** (seed tras seed). Los tiempos se miden
> contra seeds que nadie vio, el cronómetro no miente y el **podio se arma solo** en el
> [leaderboard](LEADERBOARD.md). 🏆

Entrenan su DQN localmente y suben **solo los pesos** como un archivo ONNX.
El board se actualiza solo a medida que mergeamos submissions, y el día de la
competencia corre la ronda final sobre seeds que nadie vio.

## Fechas

| | |
|---|---|
| Apertura de submissions | _a confirmar_ |
| Última submission (cierre) | _a confirmar_ — después de esta fecha no se mergean más PRs |
| Ronda final (día D) | _a confirmar_ |

## Regla de oro

> **Solo se suben pesos. Si el PR contiene CÓDIGO, queda descalificado automáticamente.**

El PR puede tocar **únicamente** estos archivos, y solo dentro de la carpeta de tu equipo:

- `submissions/<tu-equipo>/policy.onnx`  — obligatorio
- `submissions/<tu-equipo>/metadata.json` — opcional (nombre del equipo, integrantes)

Cualquier `.py`, `.ipynb`, `.sh`, notebook, o archivo fuera de esa carpeta hace fallar la validación.

**Nombre de la carpeta (`<tu-equipo>`):** solo letras sin tildes, números, `-` y `_`
(nada de espacios, `ñ` ni tildes). Ese nombre es el que aparece en el leaderboard y
tiene que ser **siempre el mismo** en todas tus submissions. No toques carpetas de
otros equipos.

`metadata.json` (opcional) tiene este formato:

```json
{"team": "mi-equipo", "members": ["Nombre Apellido", "Nombre Apellido"], "notes": "DQN + target network"}
```

## Contrato del `policy.onnx`

Tu red Q tiene que exportarse exactamente así:

| | nombre | shape | dtype |
|---|---|---|---|
| entrada | `observation` | `[batch, 2]` | float32 |
| salida | `q_values` | `[batch, 3]` | float32 |

- La observación es `[posición, velocidad]`; las 3 acciones son empujar izquierda / nada / derecha.
- Opset **17**, solo operadores estándar de ONNX (sin dominios custom).
- La salida son los **Q-values** de las 3 acciones (no apliques argmax: lo hace el evaluador).
- **Un solo archivo:** los pesos tienen que estar dentro del `policy.onnx`. Las versiones
  nuevas de PyTorch los exportan aparte, en un `policy.onnx.data`; ese archivo no se sube
  y el validador rechaza un `.onnx` que dependa de él. El script de ejemplo ya lo resuelve.
- La política de evaluación es greedy: `acción = argmax(q_values)`.

En `submissions/_ejemplo/export_example.py` tenés cómo exportar desde PyTorch
(ese archivo es solo guía local; **no** lo suban al repo).

## Cómo evalúa

- Una corrida por seed; con política y entorno deterministas, **más seeds = más muestras**.
- En MountainCar la recompensa es **-1 por paso** (máximo -200 si nunca llega a la meta).
  Por eso los retornos son **negativos**: cuanto **más cerca de 0**, mejor.
  Una policy sin entrenar marca -200 fijo. El ranking por la media descendente ordena bien.
- Métrica de ranking: **media** de los retornos, con intervalo de confianza al 95% por bootstrap.
  Se reporta también el **IQM** (interquartile mean, robusto a outliers) como dato informativo.
- Hay dos conjuntos de seeds: las **públicas** (`seeds/public_seeds.txt`) para que
  prueben, y un set **oculto** para el ranking real. El día D se usa un tercer set
  de holdout que nadie vio.

## Antes de empezar: acceso al repo

Para subir tenés que trabajar en una **rama de este repo**, no en un fork: los forks
no acceden a las seeds ocultas y la evaluación no corre. Para eso necesitás permiso
de escritura:

1. Pasale tu **usuario de GitHub** al profe.
2. Te llega una invitación como colaborador (por mail, o en
   <https://github.com/nicoRomeroCuruchet/competenciaRL/invitations>). Aceptala.
3. Cloná el repo:
   ```bash
   git clone https://github.com/nicoRomeroCuruchet/competenciaRL.git
   cd competenciaRL
   ```

Tener permiso de escritura **no** significa que puedas tocar cualquier cosa: solo se
mergean PRs que cumplen la regla de oro, y no se pushea directo a `main`.

## Probá localmente antes de subir

El bot evalúa con Python 3.12 y las versiones exactas de `harness/requirements.txt`.
Instalá lo mismo para que tu score local coincida con el del board:

```bash
python3.12 -m venv venv && source venv/bin/activate
pip install -r harness/requirements.txt
pip install torch          # solo para exportar; el evaluador no lo usa
```

1. **Exportá** tu red con `submissions/_ejemplo/export_example.py`: copialo fuera del
   repo, cargá tus pesos donde lo indica el comentario y corrélo. Te deja un
   `policy.onnx` en el directorio donde lo corriste.
2. **Validá** el contrato (es lo mismo que corre el bot en el PR):
   ```bash
   python harness/validate_submission.py --onnx ruta/a/policy.onnx
   ```
3. **Evaluá** con las seeds públicas (`seeds/public_seeds.txt`):
   ```bash
   python harness/evaluate.py --onnx ruta/a/policy.onnx --team mi-equipo --out /tmp/result.json
   ```
   Te imprime la media, el IQM y sus intervalos de confianza. El score con las seeds
   ocultas va a ser parecido pero no idéntico. Usá `--out` para no ensuciar `results/`
   del repo (esa carpeta la escribe el bot).

## Cómo subir

```bash
git checkout main && git pull
git checkout -b submission-mi-equipo
mkdir -p submissions/mi-equipo
cp ruta/a/policy.onnx submissions/mi-equipo/policy.onnx
# opcional: submissions/mi-equipo/metadata.json
git add submissions/mi-equipo/
git commit -m "submission: mi-equipo"
git push -u origin submission-mi-equipo
```

1. Entrá al repo en GitHub y abrí un **Pull Request** de tu rama contra `main`.
2. El bot valida, corre la evaluación con las seeds ocultas y te comenta el **score de
   preview** en el PR (tarda unos minutos).
3. Si la validación falla, el PR queda en rojo con el motivo. Corregí, commiteá y
   pusheá a la misma rama: el bot vuelve a correr solo.
4. Cuando se mergea a `main`, se actualiza el [leaderboard](LEADERBOARD.md).

Pueden subir **múltiples policies** (PRs sucesivos); cuenta la última de cada equipo.
Para una nueva versión, partí de `main` actualizado (`git checkout main && git pull`)
y abrí un PR nuevo.

## Errores comunes

| Síntoma | Causa y solución |
|---|---|
| "Los pesos están en un archivo externo" | Exportaste con torch nuevo sin el script de ejemplo y quedó un `policy.onnx.data`. Re-exportá con `export_example.py`. |
| "El PR toca archivos fuera de submissions/<equipo>/" | Commiteaste algo más (un notebook, un `.pt`, el `export_example.py`, `results/`…). Sacalo del PR: `git rm --cached <archivo>`, commit y push. |
| "La entrada debe llamarse 'observation'" (o la salida `q_values`) | Faltan `input_names` / `output_names` en el `torch.onnx.export`. |
| Media de **-200** exacta | La policy nunca llega a la meta: suele ser una red sin entrenar o que no cargaste tus pesos antes de exportar. |
| El PR no tiene comentario del bot | Lo abriste desde un **fork**. Tiene que ser una rama de este repo. |
