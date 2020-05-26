""" Ejercicio 4

Escribir una función que reciba otra función booleana y una lista, 
y devuelva otra lista con los elementos de la lista que devuelvan True 
al aplicarles la función booleana. """

def numero_par(n):
    return n % 2 == 0
        

def aplicar_funcion(function , lista):
    
    '''
    Función que se encarga de aplicar una función a los elementos de una lista
    parametros
        function = Es una funcion
        lista = Una lista de numeros
    Devuelve
        Una lista con el resultado tras aplicar una funcion
    '''

    lista_numero = []

    for i in lista:
        if numero_par(i):
            lista_numero.append(i)
    
    return lista_numero

if __name__ == "__main__":

    print(aplicar_funcion(numero_par, [1,2,3,4,5,6,7,8,9,10]))