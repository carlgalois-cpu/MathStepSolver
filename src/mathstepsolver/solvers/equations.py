from sympy import Eq, symbols, sympify, solve

def solve_equation(expression, variable='x'):
    """
    Resuelve una ecuación y devuelve las soluciones.
    """
    x = symbols(variable)
    
    if '=' in expression:
        parts = expression.split('=')
        left = sympify(parts[0])
        right = sympify(parts[1])
        equation = Eq(left, right)
    else:
        equation = Eq(sympify(expression), 0)
    
    solutions = solve(equation, x)
    return solutions
