#!/usr/bin/env python3
"""
Módulo para renderizar pasos de integración en LaTeX
"""

def render_integral_steps(steps, nivel=0, use_latex=False):
    """
    Renderiza los pasos de integración en texto o LaTeX
    """
    explicaciones = []
    sangria = "  " * nivel
    
    if not hasattr(steps, 'rule'):
        return [f"{sangria}Paso no reconocido: {steps}"]
    
    # Regla de potencia
    if steps.rule == 'PowerRule':
        integrand = getattr(steps, 'integrand', 'f(x)')
        variable = getattr(steps, 'variable', 'x')
        base = getattr(steps, 'base', 'x')
        exp = getattr(steps, 'exp', 'n')
        
        if use_latex:
            explicaciones.append(f"{sangria}Aplicar regla de potencia:")
            explicaciones.append(f"{sangria}$\\int {base}^{{{exp}}}  d{variable} = \\frac{{{base}^{{{exp}+1}}}}{{{exp}+1}} + C$")
            explicaciones.append(f"{sangria}Resultado: $\\frac{{{base}^{{{exp}+1}}}}{{{exp}+1}} + C$")
        else:
            explicaciones.append(f"{sangria}Aplicar regla de potencia:")
            explicaciones.append(f"{sangria}∫{base}^{exp} d{variable} = {base}^{exp+1}/{exp+1} + C")
    
    # Integración por partes
    elif steps.rule == 'IntegrationByParts':
        u = getattr(steps, 'u', 'u')
        dv = getattr(steps, 'dv', 'dv')
        
        if use_latex:
            explicaciones.append(f"{sangria}Aplicar integración por partes:")
            explicaciones.append(f"{sangria}Fórmula: $\\int u  dv = uv - \\int v  du$")
            explicaciones.append(f"{sangria}Donde: $u = {u}$, $dv = {dv}$")
        else:
            explicaciones.append(f"{sangria}Aplicar integración por partes:")
            explicaciones.append(f"{sangria}Fórmula: ∫u dv = uv - ∫v du")
            explicaciones.append(f"{sangria}Donde: u = {u}, dv = {dv}")
        
        # Subpasos si existen
        if hasattr(steps, 'substeps'):
            for substep in steps.substeps:
                explicaciones.extend(render_integral_steps(substep, nivel + 1, use_latex))
    
    # Regla no reconocida
    else:
        explicaciones.append(f"{sangria}Regla aplicada: {steps.rule}")
    
    return explicaciones


def main():
    """Función principal para pruebas"""
    # Ejemplo de prueba
    class MockSteps:
        rule = 'PowerRule'
        integrand = 'x**2'
        variable = 'x'
        base = 'x'
        exp = 2
    
    steps = MockSteps()
    
    print("Sin LaTeX:")
    for line in render_integral_steps(steps):
        print(line)
    
    print("\nCon LaTeX:")
    for line in render_integral_steps(steps, use_latex=True):
        print(line)

if __name__ == "__main__":
    main()
