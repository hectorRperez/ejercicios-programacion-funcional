""" Ejercicio 9

Escribir una función que calcule el módulo de un vector. """


def calcular_modulo(v):
    '''
    Función que calcula el modulo de un vector
    parametros:
        v = Una tupla de números reales
    Devuelve:
        El modulo del vector v
    '''
    return sum([x ** 2 for x in v]) ** 0.5


if __name__ == "__main__":
    print(calcular_modulo((3,4)))
    print(calcular_modulo((1,2,3)))