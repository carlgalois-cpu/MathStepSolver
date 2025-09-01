from sympy import symbols, sympify, Eq, Integral, Derivative, Limit, Matrix
from sympy import simplify, solve
from .solvers import integrals, derivatives, equations, limits, matrices, statistics

def detect_problem_type(expression, variable='x'):
    """
    Detecta el tipo de problema matemático.
    """
    try:
        expr = sympify(expression)
    except:
        return 'expression'
    
    if 'Integral' in str(expr) or 'integral' in expression.lower():
        return 'integral'
    
    if 'Derivative' in str(expr) or 'derivative' in expression.lower():
        return 'derivative'
    
    if 'Eq' in str(expr) or '=' in expression:
        return 'equation'
    
    if 'Limit' in str(expr) or 'limit' in expression.lower():
        return 'limit'
    
    if 'Matrix' in str(expr):
        return 'matrix'
    
    stats_keywords = ['mean', 'median', 'mode', 'std', 'variance']
    if any(keyword in expression.lower() for keyword in stats_keywords):
        return 'statistics'
    
    return 'expression'

def solve_problem(expression, problem_type=None, variable='x'):
    """
    Resuelve cualquier tipo de problema matemático.
    """
    if problem_type is None:
        problem_type = detect_problem_type(expression, variable)
    
    try:
        if problem_type == 'integral':
            return integrals.solve_integral(expression, variable)
        elif problem_type == 'derivative':
            # Si es una ecuación, tomar solo el lado izquierdo
            if '=' in expression:
                parts = expression.split('=')
                expression = parts[0].strip()
            return derivatives.solve_derivative(expression, variable)
        elif problem_type == 'equation':
            return equations.solve_equation(expression, variable)
        elif problem_type == 'limit':
            return limits.solve_limit(expression, variable)
        elif problem_type == 'matrix':
            return matrices.solve_matrix(expression)
        elif problem_type == 'statistics':
            return statistics.solve_statistics(expression)
        else:
            return simplify(sympify(expression))
    except Exception as e:
        return f"Error al resolver el problema: {str(e)}"
