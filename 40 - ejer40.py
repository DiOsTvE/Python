diccionario = {'sergio':0,'alberto':0,'david':0,'esteban':0}
cadena = input("Ingrese cadena: ").lower()

for j in diccionario:
    longitud_total = len(cadena)
    print("Tamaño total de la cadena: ", longitud_total)
    longitud_cadena_a_buscar = len(j)
    print("Tamaño de la subcadena: ", longitud_cadena_a_buscar)
    maximo = longitud_total - longitud_cadena_a_buscar
    print("Maximo a llegar: ", maximo)

    contador = 0
    print(maximo)

    for i in range(maximo + 1):
        existe = cadena.find(j, i, i + longitud_cadena_a_buscar)
        if existe != -1:
            contador = contador + 1

    print("Se repite ", contador, " veces")
    diccionario[j] = contador

print(diccionario)
print(cadena.title)