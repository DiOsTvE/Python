lista = ['Lunes','Martes','Jueves','Viernes']
lista.insert(2,'Miércoles')
print(lista)
lista2 = ['Sábado','Domingo']
lista.extend(lista2)
print(lista)
"""
y si quiero eliminar?
"""
lista.pop()#elimina el último elemento de la lista
print(lista)
lista.pop(2)#elimina el elemento en la posición indicada
print(lista)
lista.remove('jueves')#elimina el elemento por su contenido
print(lista)