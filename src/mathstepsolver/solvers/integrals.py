from sympy import Integral, symbols, sympify
from sympy.integrals.manualintegrate import integral_steps

def solve_integral(expression, variable='x'):
    """
    Resuelve una integral y devuelve los pasos.
    """
    x = symbols(variable)
    expr = sympify(expression)
    integral = Integral(expr, x)
    steps = integral_steps(integral)
    return steps
from sympy import Integral, symbols, sympify
from sympy.integrals.manualintegrate import integral_steps

def solve_integral(expression, variable='x'):
    """
    Resuelve una integral y devuelve los pasos.
    """
    x = symbols(variable)
    expr = sympify(expression)
    integral = Integral(expr, x)
    steps = integral_steps(integral)
    return steps
from sympy import symbols, sympify
from sympy.integrals.manualintegrate import integral_steps

def solve_integral(expression, variable='x'):
    """
    Resuelve una integral y devuelve los pasos.
    """
    try:
        x = symbols(variable)
        expr = sympify(expression)
        # Para SymPy >= 1.6, integral_steps espera (expr, symbol)
        steps = integral_steps(expr, x)
        return steps
    except Exception as e:
        return f"Error al resolver la integral: {str(e)}"
