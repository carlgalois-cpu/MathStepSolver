# MathStepSolver

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/)

Una herramienta educativa para resolver problemas matemáticos mostrando cada paso del proceso, este software es educativo, es solo para aprender a usar de mejor forma el conocimiento matemático y después tener mayor creatividad.

## Características

- Resuelve integrales, derivadas, ecuaciones, límites y más
- Muestra los pasos intermedios de forma clara y detallada
- Soporta múltiples métodos de resolución
- Salida en texto plano y LaTeX (próximamente)

## Instalación

```bash
pip install mathstepsolver

## Uso

### Como línea de comandos:
```bash
mathstepsolver "x*sin(x)"
mathstepsolver "x^2 + 3x + 2 = 0" --type equation
### Como librería Python:
from mathstepsolver import solve_problem

pasos = solve_problem("x^2")
for paso in pasos:
    print(paso)
