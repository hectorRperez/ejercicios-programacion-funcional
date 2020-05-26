from math import sin, cos , tan , exp , log


""" Ejercicio 2

Escribir una función que simule una calculadora científica que permita 
calcular el:

1)seno 
2)coseno 
3)tangente 
4)exponencial
5)logaritmo neperiano.


La función preguntará al usuario el valor y la función a aplicar, 
y mostrará por pantalla una tabla con los enteros de 1 al valor introducido 
y el resultado de aplicar la función a esos enteros. """

#TODO documentar las funciones
#TODO agregar a git 
def aplicar_funcion(f, n):
    
    '''
    Funcion que se encarga de aplicar las funciones matematicas
    parametros:
        f = Es la función matematica seleccionada por el usuario
        n = Entero ingresado por el usuario, la funcion elegida se aplicara a los numeros de 1 al n
    Devuelve:
        Un diccionario con los pares i:f(i) para cada valor entero 
    '''

    funciones_matematicas = {1:sin, 2:cos, 3:tan, 4:exp, 5:log}
    result = { }

    for i in range(1, n+1):
        result[i] = funciones_matematicas[f](i)

    return result


def calculadora():
    '''
    Función que aplica una función matematica (seno, cose , tangente, exponencial , logaritmo neperiano)
    a una lista de numeros de 1 hasta n

    La función muestra por pantalla el resultado 

    Parametros:
        No recibe nada
    Devuelve:
        No devuelve nada
    '''
    n = int(input('Ingrese un numero enetero positivo: '))

    funcion_matematica = int(input('Ingrese una opción: \n1)Seno'\
                    '\n2)Cose \n3)Tangente \n4)Exponencial \n5)Logaritmo neperiano'\
                    '\nOpcion: '))
    
    for i, j in aplicar_funcion(funcion_matematica,n).items():
        print(i,j)


if __name__ == "__main__":

    calculadora()