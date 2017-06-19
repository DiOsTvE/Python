"""
Realizar algoritmo de busqueda con palabras compuestas
"""
cadena = input("Ingrese una frase: ")
cadena_a_buscar = input("Ingrese palabra a buscar: ")

longitud_total = len(cadena)
print("Tamaño total de la cadena: ",longitud_total)
longitud_cadena_a_buscar = len(cadena_a_buscar)
print("Tamaño de la subcadena: ",longitud_cadena_a_buscar)
maximo = longitud_total-longitud_cadena_a_buscar
print("Maximo a llegar: ",maximo)

contador = 0
print(maximo)

for i in range(maximo+1):
    existe = cadena.find(cadena_a_buscar,i,i+longitud_cadena_a_buscar)
    if existe != -1:
        contador = contador + 1
print("Se repite ",contador," veces")