from sympy import Derivative, symbols, sympify, diff

def solve_derivative(expression, variable='x'):
    """
    Resuelve una derivada y devuelve los pasos.
    """
    x = symbols(variable)
    expr = sympify(expression)
    derivative = diff(expr, x)
    return derivative
