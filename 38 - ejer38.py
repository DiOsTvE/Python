"""
Rellenar una lista de seis numeros, crear otra funcion donde se
envia la lista y contamos cuantos numeros mayores de 10 hay en
la lista
"""
def relleno():
    numeros = []
    for i in range(6):
        numeros.append(int(input("Escribe algún número: ")))
    return numeros

def contar(lista_numeros):
    contador = 0
    for i in range(len(lista_numeros)):
        if lista_numeros[i] > 10:
            contador = contador + 1
    return contador

almacen = relleno()
cantidad = contar(almacen)

print("Cantidad de numeros mayores de 10 en la lista: ",cantidad)