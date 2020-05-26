""" Ejercicio 6

Escribir una función reciba una lista de notas 
y devuelva la lista de calificaciones correspondientes a esas notas. """

def calificacion(nota):
    '''
    Funcioón que evalua una nota y se devuelve su correspondiente calificacion
    parametro:
        nota = Una nota real de un alumno
    Devuelve:
        La calificacion correspondiente a la nota
    '''
    if nota < 5:
        return 'SS'
    elif nota < 7:
        return 'AP'
    elif nota < 9:
        return 'NT'
    elif nota < 10:
        return 'SB'
    else:
        return 'MH'

def aplicar_notas(lista_notas):
    '''
    Función que devuelve la calificación correspondiente a la nota de la lista pasada
    parametros:
        lista_notas = Una lista de notas
    Devuelve:
        Una lista con las calificaciones correspondientes
    '''
    return list(map(calificacion, lista_notas))

if __name__ == "__main__":
    print(aplicar_notas([6.5, 5 , 3.4, 8.2 , 2.1 , 9.7, 10]))