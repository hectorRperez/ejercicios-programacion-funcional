""" Ejercicio 1

Escribir una función que aplique un descuento a un precio 
y otra que aplique el IVA a un precio. 

Escribir una tercera función que reciba un diccionario con los precios 
y porcentajes de una cesta de la compra, y una de las funciones anteriores, 


y utilice la función pasada para aplicar los descuentos o el IVA a los productos 
de la cesta y devolver el precio final de la cesta. """

def aplicar_descuento(precio, descuento):
    '''
    Función que se encarga de aplicar un descuento a un precio
    parametros:
        precio = Precio real de un producto
        descuento = Descuento aplicar al producto
    Devuelve:
        El descuento total sobre un producto
    '''


    descuento = descuento / 100

    return precio - (descuento * precio)
    

def aplicar_iva(precio, porcentajes):

    '''
    Función que se encarga de aplicar el iva a un precio 
    parametros:
        precio = Precio real de un producto
        porcentaje = Porcentaje aplicar al precio
    
    Devuelve:
        Devuelve el total de iva del producto
    '''
    porcentajes = porcentajes / 100

    return precio + (precio * porcentajes)

def compras(compras, function):
    '''
    Función que recibe un diccionario con el par { precio : descuento }
    Parametros:
        compras = un diccionario con el par { precio : descuento }
        function = La función que se encarga de aplicar un descuento o aplicar el IVA
    Deveulve:
        El descuento aplicado
    '''
    descuento = 0

    for i,j in compras.items():
        descuento += function(i,j)
    
    return descuento


if __name__ == "__main__":
    
    #precios : porcetanjes 
    mi_compra = {

        1000 : 20,
        500  : 10,
        100  : 1,
    }

    print(compras(mi_compra,aplicar_descuento))
    print(compras(mi_compra, aplicar_iva))
