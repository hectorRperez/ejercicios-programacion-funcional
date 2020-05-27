""" Ejercicio 10

Una inmobiliaria de una ciudad maneja una lista de inmuebles como la siguiente:

[{'año': 2000, 'metros': 100, 'habitaciones': 3, 'garaje': True, 'zona': 'A'}, {'año': 2012, 'metros': 60, 'habitaciones': 2, 'garaje': True, 'zona': 'B'}, {'año': 1980, 'metros': 120, 'habitaciones': 4, 'garaje': False, 'zona': 'A'}, {'año': 2005, 'metros': 75, 'habitaciones': 3, 'garaje': True, 'zona': 'B'}, {'año': 2015, 'metros': 90, 'habitaciones': 2, 'garaje': False, 'zona': 'A'}]

Construir una función que permita hacer búsqueda de inmuebles en función de un presupuesto dado. 

La función recibirá como entrada la lista de inmuebles y un precio.

devolverá otra lista con los inmuebles cuyo precio sea menor o igual que el dado. Los inmuebles de la lista que se devuelva deben incorporar un nuevo par a cada diccionario con el precio del inmueble, donde el precio de un inmueble se calcula con las siguiente fórmula en función de la zona:

Zona A: precio = (metros x 1000 + habitaciones x 5000 + garaje x 15000) x (1 - antiguedad / 100)
Zona B: precio = (metros x 1000 + habitaciones x 5000 + garaje x 15000) x (1 - antiguedad / 100) x 1.5 """


def agregar_precio(pisos):
    '''
    Aplica la formula a cada elemento del diccionario

    Zona A: precio = (metros x 1000 + habitaciones x 5000 + garaje x 15000) x (1 - antiguedad / 100)
    Zona B: precio = (metros x 1000 + habitaciones x 5000 + garaje x 15000) x (1 - antiguedad / 100) x 1.5

    parametros:
        pisos = Un elemento de un diccionario

    Devuelve:
        Un elemento de un diccionario y se le agrego el par precio : precio


    '''
    if pisos['zona'] == 'A':
        precio = (pisos['metros'] * 1000 + pisos['habitaciones'] * 5000 + int(pisos['garaje']) * 15000) * (1 - (2020- pisos['año']) / 100)
        pisos['precio'] = round(precio,2)
    else:
        precio = (pisos['metros'] * 1000 + pisos['habitaciones'] * 5000 + (int(pisos['garaje']) * 15000)) * (1 - (2020 - pisos['año']) / 100) * 1.5
        pisos['precio'] = round(precio,2)
    
    return pisos


def buscar_inmueble(pisos, presupuesto):

    def filtro(pisos):
        '''
        Realiza la busqueda de apartamentos menores al presupuesto que se tiene
        '''
        return pisos['precio'] <= presupuesto

    return list(filter(filtro, map(agregar_precio, pisos)))


if __name__ == "__main__":

    mis_pisos = [

        {'año': 2000, 'metros': 100, 'habitaciones': 3, 'garaje': True, 'zona': 'A'}, 
        {'año': 2012, 'metros': 60, 'habitaciones': 2, 'garaje': True, 'zona': 'B'}, 
        {'año': 1980, 'metros': 120, 'habitaciones': 4, 'garaje': False, 'zona': 'A'}, 
        {'año': 2005, 'metros': 75, 'habitaciones': 3, 'garaje': True, 'zona': 'B'}, 
        {'año': 2015, 'metros': 90, 'habitaciones': 2, 'garaje': False, 'zona': 'A'}

        ]


    for i in buscar_inmueble(mis_pisos,100000):
        print(i)
        print('--------------------------')