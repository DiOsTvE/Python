"""
Crear una lista que esta compuesta por tres listas de tres, sus elementos
son números, mostrar el listado de los números
"""
"""
lista = [[4, 6, 8, 5], [1, 2, 5], [7, 8, 10, 7, 3]]
for h in range(len(lista)):
    print("Lista ", h+1)
    for i in range(len(lista[h])):
        print(lista[h][i])
    print("Fin de lista")
"""
"""
Crear una lista que contenga: nombre, apellidos, meses en el que trabajo
y mostrarlo
"""
lista = [["Fran", "García", ["Enero", "Febrero"]], ["Cesar", "Ramos", ["Marzo", "Abril", "Mayo"]], ["Javier", "Rodrigo", ["Septiembre", "Octubre"]]]

for h in range(len(lista)):
    print("Nombre del trabajador: ")
    for i in range(len(lista[h])-1):
        print(lista[h][i],end=" ")
    print("\nMeses en el que trabajó: ")
    for j in range(len(lista[h][2])):
        print(lista[h][2][j], end=". ")
    print("\n")