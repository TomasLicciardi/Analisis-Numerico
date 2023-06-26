'''Un vehículo parte del reposo y se mueve con movimiento uniformemente acelerado, recorre 900 metros en medio minuto. Sabiendo que el tiempo se determinó con un cronómetro de 1/10segs. Y que su contribución al error de la aceleración es de 1/4 del error total, halle:
a) El error absoluto, relativo y porcentual cometidos al determinar la aceleracion.
b) Los errores bsoluto, relativo y porcentual del espacio.'''
from sympy import symbols, diff, lambdify
import time

#Funcion para calcular las derivadas parciales
def calcular_derivada(): 

    x, t = symbols('x t',real=True) 
    a = (2 * x) / t ** 2
    print(f'Tenemos la funcion de la aceleracion a={a}, vamos a obtener las derivadas')
    time.sleep(1.5)
    print('Calculando derivadas...')
    time.sleep(2)
    da_dx = diff(a, x)
    da_dt = diff(a, t)
    print(f'La derivada respecto del espacio es:\n {da_dx}')
    time.sleep(2)
    print(f'La derivada respecto del tiempo es:\n {da_dt}')
    return [da_dx,da_dt]

#Funcion para obtener los valores de la derivada en sus respectivos puntos
def calcular_errores():

    x, t = symbols('x t',real=True)
    valor_x = 900
    valor_t = 30

    derivadas = calcular_derivada()
    derivada_x = derivadas[0]
    derivada_t = derivadas[1]

    funcion_x = lambdify([t],derivada_x)
    funcion_t = lambdify([x,t],derivada_t)

    valor_da_dx = abs(funcion_x(valor_t))
    valor_da_dt = abs(funcion_t(valor_x,valor_t))

    return [valor_da_dx,valor_da_dt]

#Funcion para calcular los errores de aceleracion y de espacio
def aceleracion_espacio():
    valor_x = 900
    valor_t = 30
    error_tiempo = 0.1
    error_contribucion = 1/4
    error_contribucion2 = 3/4
    valor_a = (2 * valor_x) / valor_t ** 2

    valores_derivadas = calcular_errores()

    #Calcular errores aceleracion
    print('Calculando errores de la aceleracion...')
    time.sleep(2)
    print('Listo')
    error_abs_aceleracion = (error_contribucion) ** (-1) * valores_derivadas[1] * error_tiempo
    error_relativo_aceleracion = error_abs_aceleracion / valor_a
    error_porcentual_aceleracion = error_relativo_aceleracion * 100

    print('Calculando errores del espacio...')
    time.sleep(2)
    print('Listo')
    #Calcular errores espacio
    error_abs_espacio = error_contribucion2 * error_abs_aceleracion * (valores_derivadas[0] ** (-1))
    error_relativo_espacio = error_abs_espacio / valor_x
    error_porcentual_espacio = error_relativo_espacio * 100

    return error_abs_aceleracion, error_relativo_aceleracion, error_porcentual_aceleracion, error_abs_espacio, error_relativo_espacio, error_porcentual_espacio

# Ejecutar la función para obtener los errores
errores = aceleracion_espacio()

print("Errores en la aceleración:")
print(f"{'Error absoluto':<20} {'Error relativo':<20} {'Error porcentual':<20}")
print(f"{errores[0]:<20.4f} {errores[1]:<20.4f} {errores[2] :<20.4f}")

print("\nErrores en el espacio:")
print(f"{'Error absoluto':<20} {'Error relativo':<20} {'Error porcentual':<20}")
print(f"{errores[3]:<20.4f} {errores[4]:<20.4f} {errores[5] :<20.4f}")