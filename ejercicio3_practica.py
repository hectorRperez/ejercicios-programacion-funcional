""" Ejercicio 3

Escribir una función que reciba otra función y una lista, 
y devuelva otra lista con el resultado de aplicar la función dada 
a cada uno de los elementos de la lista """


def cuadrado(n):
    '''
    Función que aplica a un numero su cuadrado
    parametros:
        n = Un numero
    Devuelve
        El cuadrado de n
    '''
    return n * n

def aplicar_funcion(function, lista_numero):
    '''
    Función que se encarga de aplicar funciones especificas a una lista de elementos
    paramatros:

        function = Es una función con un funcionamiento especifico
        lista_numero = Una lista de numeros
        
    Devuelve:
        Una lista de con el resultado de aplicar la función a los valores de la lista
    '''
    lista = []

    for i in lista_numero:
        lista.append(function(i))
    
    return lista

if __name__ == "__main__":

    print(aplicar_funcion(cuadrado, [1,2,3,4,5]))