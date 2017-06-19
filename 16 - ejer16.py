#rellenar 10 notas de un alumno
lista=[]
"""
for i in range(10):
    nota = int(input("Ingrese nota: "))
    lista.append(nota)
print(lista)
"""
#y si fuesen datos distintos??
#quiero guardar materia, nombre y nota
tupla=('Materia','Nombre','Nota')
for i in range(3):
    dato = input("Ingresa el dato de la "+tupla[i]+": ")
    lista.append(dato)
