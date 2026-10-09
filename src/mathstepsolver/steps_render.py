#!/usr/bin/env python3
"""
Módulo para renderizar pasos de integración en texto y LaTeX
"""

def render_integral_steps(steps, nivel=0, use_latex=False):
    """
    Renderiza los pasos de integración
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
    
    # Integración por partes (ejemplo)
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
    
    # Regla no reconocida
    else:
        if use_latex:
            explicaciones.append(f"{sangria}Regla aplicada: ${steps.rule}$")
        else:
            explicaciones.append(f"{sangria}Regla aplicada: {steps.rule}")
    
    return explicaciones
