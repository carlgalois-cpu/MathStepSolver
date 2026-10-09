from sympy import Matrix, sympify

def solve_matrix(expression):
    """
    Realiza operaciones con matrices y devuelve el resultado.
    """
    try:
        matrix = sympify(expression)
        return matrix
    except:
        return "No se pudo procesar la expresión matricial"
