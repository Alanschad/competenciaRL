#!/usr/bin/env python3
"""
EJEMPLO PARA ALUMNOS — cómo exportar su DQN al ONNX que pide el contrato.

Este archivo NO se sube al repo de la competencia (subir código = descalificación).
Es solo una guía para que generen su policy.onnx localmente y lo cumplan.

Contrato:
  - entrada:  "observation"  float32  shape [batch, OBS_DIM]
  - salida:   "q_values"     float32  shape [batch, N_ACTIONS]
  - opset 17, operadores estándar.
La policy de evaluación hace: accion = argmax(q_values).
"""
import os
import tempfile

import onnx
import torch
import torch.nn as nn

OBS_DIM = 2       # MountainCar-v0: [posición, velocidad]
N_ACTIONS = 3     # empujar izq / nada / der

class QNetwork(nn.Module):
    """Reemplazá esto por TU arquitectura ya entrenada."""
    def __init__(self):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(OBS_DIM, 128), nn.ReLU(),
            nn.Linear(128, 128), nn.ReLU(),
            nn.Linear(128, N_ACTIONS),
        )

    def forward(self, x):
        return self.net(x)  # devuelve Q-values, NO argmax


def export(model: nn.Module, path: str = "policy.onnx"):
    model.eval()
    dummy = torch.zeros(1, OBS_DIM, dtype=torch.float32)
    # Las versiones nuevas de torch guardan los pesos en un archivo aparte
    # (policy.onnx.data) que NO se puede subir. Exportamos a un directorio
    # temporal y re-guardamos con onnx para que TODO quede dentro de policy.onnx.
    with tempfile.TemporaryDirectory() as tmp:
        tmp_path = os.path.join(tmp, "policy.onnx")
        torch.onnx.export(
            model, dummy, tmp_path,
            input_names=["observation"],
            output_names=["q_values"],
            dynamic_axes={"observation": {0: "batch"}, "q_values": {0: "batch"}},
            opset_version=17,
        )
        onnx.save(onnx.load(tmp_path), path)
    print(f"Exportado a {path} (un solo archivo, listo para subir)")


if __name__ == "__main__":
    net = QNetwork()
    # net.load_state_dict(torch.load("mi_dqn_entrenada.pt"))  # <- tus pesos
    export(net)
