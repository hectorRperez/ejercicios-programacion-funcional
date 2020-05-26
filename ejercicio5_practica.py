""" Ejercicio 5

Escribir una función que reciba una frase y 
devuelva un diccionario con las palabras que contiene y su longitud. 

diccionario = { palabra : longitud}

"""

def aplicar_funcion(frase):
    
    palabras = frase.split()
    longitud = map(len, palabras)
    
    return dict(zip(palabras, longitud))


if __name__ == "__main__":
    frase = 'Welcome to Python'
    print(aplicar_funcion(frase))


