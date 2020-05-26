""" Ejercicio 8

Escribir una función reciba un diccionario con las asignaturas 
y las notas de un alumno y devuelva otro diccionario con 
las 

asignaturas en mayúsculas y 
las calificaciones correspondientes a las notas aprobadas. """

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


def verificar_nota(nota):
    '''
    Función que verifica si la nota es mayor que 5
    parametros:
        nota = Es una nota real de un alumno
    Devuelve:
        Devuelve True si la nota es mayor a 5
    '''
    return nota >= 5


def aplicar_funciones(notas_alumnos):
    '''
    Función que aplica funciones al diccionario
    parametros:
        notas_alumnos = Es un diccionario con los pares asignatura : nota
    Devuelve:
        Un diccionario con las calificaciones correspondientes a las notas aprobadas
    '''
    notas_aprobadas = {}

    for i,j in notas_alumnos.items():
        
        if verificar_nota(j):
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

    print(aplicar_funciones(notas_alumnos))