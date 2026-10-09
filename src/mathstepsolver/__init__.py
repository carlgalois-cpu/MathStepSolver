"""
MathStepSolver - Una herramienta educativa para resolver problemas matemáticos.
"""

__version__ = "0.1.0"

from .core import solve_problem, detect_problem_type
from . import solvers
from .jupyter_integration import solver, MathStepSolver
