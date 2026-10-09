import click
from .core import solve_problem, detect_problem_type
from .steps_render import render_integral_steps as render_steps

@click.command()
@click.argument('expression')
@click.option('--variable', default='x', help='Variable de integración')
@click.option('--type', help='Tipo de problema (opcional)')
@click.option('--latex', is_flag=True, help='Mostrar pasos en formato LaTeX')
def main(expression, variable, type):
    """Resuelve problemas matemáticos mostrando los pasos."""
    try:
        problem_type = type or detect_problem_type(expression, variable)
        result = solve_problem(expression, problem_type, variable)
        explanations = render_steps(result, problem_type)
        
        click.echo(f"Pasos para resolver {expression}:")
        for explanation in explanations:
            click.echo(explanation)
            
    except Exception as e:
        click.echo(f"Error: {e}", err=True)@click.command()
@click.argument('expression')
@click.option('--variable', default='x', help='Variable de integración')
@click.option('--type', help='Tipo de problema (opcional)')
@click.option('--latex', is_flag=True, help='Mostrar salida en formato LaTeX')
def main(expression, variable, type, latex):
    """Resuelve problemas matemáticos mostrando los pasos."""
    try:
        problem_type = type or detect_problem_type(expression, variable)
        result = solve_problem(expression, problem_type, variable)
        
        if latex:
            from .steps_render import render_latex
            explanations = render_latex(result, problem_type)
        else:
            explanations = render_steps(result, problem_type)
        
        click.echo(f"Pasos para resolver {expression}:")
        for explanation in explanations:
            click.echo(explanation)
            
    except Exception as e:
        click.echo(f"Error: {e}", err=True)

if __name__ == '__main__':
    main()
import click
from .core import solve_problem, detect_problem_type
from .steps_render import render_steps, render_latex

@click.command()
@click.argument('expression')
@click.option('--variable', default='x', help='Variable de integración')
@click.option('--type', help='Tipo de problema (opcional)')
@click.option('--latex', is_flag=True, help='Mostrar salida en formato LaTeX')
def main(expression, variable, type, latex):
    """Resuelve problemas matemáticos mostrando los pasos."""
    try:
        problem_type = type or detect_problem_type(expression, variable)
        result = solve_problem(expression, problem_type, variable)
        
        if latex:
            explanations = render_latex(result, problem_type)
        else:
            explanations = render_steps(result, problem_type)
        
        click.echo(f"Pasos para resolver {expression}:")
        for explanation in explanations:
            click.echo(explanation)
            
    except Exception as e:
        click.echo(f"Error: {e}", err=True)

if __name__ == "__main__":
    
    main(standalone_mode=False)
