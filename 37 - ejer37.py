def rellenar_lista():
    lista=[]
    for i in range(5):
        nombre = input("Ingrese nombre: ")
        lista.append(nombre)
    return lista
def listado_personas(lista):
    for i in lista:
        print(i)

listado = rellenar_lista()
listado_personas(listado)