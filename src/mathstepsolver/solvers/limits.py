from sympy import Limit, symbols, sympify, oo

def solve_limit(expression, variable='x'):
    """
    Resuelve un límite y devuelve el resultado.
    """
    x = symbols(variable)
    expr = sympify(expression)
    
    limit_result = Limit(expr, x, 0).doit()
    return limit_result
