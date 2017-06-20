"""
Crear un diccionario normal, donde van a ingresar 4 provincias de
España, las cuales van a ser las claves y dentro de esas claves
cuanta poblacion tiene esas provincias.
"""
"""
diccionario = {}
for i in range(4):
    provincia = input("Ingrese una provincia: ").title()
    poblacion = int(input("Ingrese la cantidad de poblacion de la provincia: "))
    diccionario[provincia] = poblacion
print(diccionario)
"""
"""
Crear un diccionario y dentro se crean listas, con cada distinto codigo
de producto y para cada codigo de producto, se incluye el nombre
de producto, el precio y la cantidad.
"""
almacen_productos = {}
caracteristicas_producto = []

for i in range(2):
    codigo_producto = input("Inserta el codigo de producto: ")
    caracteristicas_producto.append(input("Inserta el nombre del producto: "))
    caracteristicas_producto.append(float(input("Inserta el precio del producto: ")))
    caracteristicas_producto.append(int(input("Inserta la cantidad del producto: ")))
    copia = caracteristicas_producto[:]
    almacen_productos[codigo_producto] = copia
    for j in caracteristicas_producto[:]:
        caracteristicas_producto.remove(j)

constante = ('Nombre: ','Precio: ','Cantidad: ')

for i in almacen_productos:
    print("Código: ",i)
    for j in range(len(almacen_productos[i])):
        print(constante[j], almacen_productos[i][j],end=" ")
    print("\n")