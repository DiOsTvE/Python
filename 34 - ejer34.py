"""
Introducir dos cadenas, decir si tienen la misma cantidad de
caracteres, decir si no son iguales y cual es la más grande en
longitud
"""
def pedir_cadena():
    texto = input("Introduce la cadena: ")
    return texto
def cuenta_caracteres(cadena1, cadena2):
    longitud1 = len(cadena1)
    longitud2 = len(cadena2)
    if longitud1 == longitud2:
        tamanio = 0
        return tamanio
    else:
        if longitud1 > longitud2:
            tamanio = 1
            return tamanio
        else:
            tamanio = 2
            return  tamanio
def solucion(tamanio):
    if tamanio == 0:
        print("Las cadenas son iguales.")
    elif tamanio == 1:
        print("Las cadenas son distintas. La cadena1 es más grande.")
    elif tamanio == 2:
        print("Las cadenas son distintas. La cadena2 es más grande.")

cadena1 = pedir_cadena()
cadena2 = pedir_cadena()
tamanio = cuenta_caracteres(cadena1, cadena2)
solucion(tamanio)