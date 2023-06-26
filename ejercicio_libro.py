'''La ley de Stefan-Boltzmann se utiliza para estimar la velocidad de cambio de la energía H para una superficie, esto es,
H = AeσT 4
donde H está en watts, A = área de la superficie (m2), e = la emisividad que caracteriza la propiedad de emisión de la superficie (adimensional), σ = una constante universal llamada constante de Stefan-Boltzmann (= 5.67 x 10-8 W m-2 K-4) y T = temperatura absoluta (K). Determine el error de H para una placa de acero con A = 0.15 m2 , e = 0.90 y T = 650 ± 20. Compare los resultados con el error exacto. Repita los cálculos pero con T = 650 ± 40. Interprete los resultados
'''

from sympy import symbols, diff

def derivadas():
    a,e,sigma,t = symbols('a e sigma t')
    h = a * e * sigma * t ** 4
    
    lista_derivadas = []
    variables = [a,e,t]
    for var in variables:
        agregar_derivada = diff(h,var)
        lista_derivadas.append(agregar_derivada)
    return lista_derivadas

def calcular_errores_derivadas(derivadas, errores_variables):
    errores_abs = []
    errores_rel = []
    errores_porcent = []



