""" 
Ejercicio 7

Escribir una función reciba un diccionario con las asignaturas 
y las notas de un alumno y devuelva otro diccionario con las asignaturas en mayúsculas 
y las calificaciones correspondientes a las notas. """

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


def aplicar_funcion(notas_alumnos):
    
    '''
    Función que se encarga de aplicar una función a un diccionario de notas
    parametros
        notas_alumnos = Un diccionario con el par Asignatura : notas
    Devuelve
        Un diccionario con el par asignatura : calificacion
    '''
    asignaturas = map(str.upper, notas_alumnos.keys())
    calificaciones = map(calificacion, notas_alumnos.values())

    return dict(zip(asignaturas, calificaciones))

if __name__ == "__main__":
    
    notas_alumnos = {

        'Matematicas' :6.5,
        'Fisica'      :5,
        'Quimica'     :3.4,
        'Economia'    :8.2,
        'Historia'    :9.7,
        'Programacion':10
    }

    print(aplicar_funcion(notas_alumnos))
