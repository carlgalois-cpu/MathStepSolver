from IPython.display import display, Math, Latex
from .core import solve_problem, detect_problem_type
from .steps_render import render_integral_steps  # Cambiado

class MathStepSolver:
    def __init__(self):
        pass

    def solve(self, expression, problem_type=None, variable='x'):
        """
        Resuelve un problema y muestra los pasos en LaTeX.
        """
        result = solve_problem(expression, problem_type, variable)
        explanations = render_integral_steps(result, use_latex=True)  # Cambiado

        for explanation in explanations:
            if '$' in explanation:
                display(Math(explanation))
            else:
                print(explanation)

# Funciones adicionales para compatibilidad
def solver(expression, problem_type=None, variable='x'):
    solver = MathStepSolver()
    return solver.solve(expression, problem_type, variable)
