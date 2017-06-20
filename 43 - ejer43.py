lista_nombres = []
lista_poblaciones = []
lista_provincias = []
for i in range(3):
    nombre = input("Ingrese un nombre: ")
    lista_nombres.append(nombre)
    poblacion = input("Ingresa una poblacion: ")
    lista_poblaciones.append(poblacion)
    provincia = input("Ingresa una provincia: ")
    lista_provincias.append(provincia)

diccionario = {}
diccionario['nombre'] = lista_nombres
diccionario['poblacion'] = lista_poblaciones
diccionario['provincia'] = lista_provincias
"""
print("Nombre: ",diccionario['nombre'][0])
print("Poblacion: ",diccionario['poblacion'][0])
print("Provincia: ",diccionario['provincia'][0])
"""
for i in range(3):
    print("Nombre: ", diccionario['nombre'][i])
    print("Poblacion: ", diccionario['poblacion'][i])
    print("Provincia: ", diccionario['provincia'][i])