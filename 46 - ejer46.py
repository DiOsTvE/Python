lista1 = ['ana','juan','pedro','jacinto','david','alice']
lista2 = lista1[3:5]#Desde la posicion 3 hasta la 5(sin incluir)
print(lista2)
lista3 = lista1[2:]#Desde la posicion 2 hasta el final
print(lista3)
lista4 = lista1[:4]#Desde el inicio hasta el 4(sin incluir)
print(lista4)
lista4.append('fran')
print(lista4)
print(lista3)
del(lista1[:3])#Elimina desde el inicio hasta el 3(sin incluir)
print(lista1)
