"""
Rellenamos una lista con nombres, que nos digan una posicion y
elimina el nombre de dicha posicion.
"""
"""
lista = ["Juan","Fran","Javi","Cesar","Manuel"]
print(lista)
pos = int(input("Dime una posición: "))
nombre_eliminado = lista[pos]
lista.pop(pos)
print(lista)
print("El nombre eliminado ha sido: ",nombre_eliminado)
"""
"""
Rellenamos una lista con nombres, nos dicen un nombre y
eliminamos dicho nombre de la lista.
"""
lista = ["Juan","Fran","Javi","Cesar","Manuel"]
print(lista)
nombre = input("Dime un nombre a eliminar: ").capitalize()
print(nombre)
for i in lista:
    if i == nombre:
        nombre_eliminado = nombre
lista.remove(nombre)
print(lista)
print("El nombre eliminado ha sido: ", nombre_eliminado)