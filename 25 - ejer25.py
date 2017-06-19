"""
Preguntas cuantos alumnos hay en el grupo, y a esos alumnos
preguntarle el nombre del padre, el nombre de la madre y la
cantidad de miembros que forman la unidad familiar, los datos
guardarlos en una lista llamada curso
"""
alumnos = int(input("Cuantos alumnos hay en el grupo?: "))
curso = []
for i in range(alumnos):
    curso.append(i)
    curso.append(input("Nombre del padre: "))
    curso.append(input("Nombre de la madre: "))
    curso.append(input("Miembros de la unidad familiar: "))

print("Para visualizar la opcion correspondiente, elige el número: ")
print("1 --> Visualiza los nombres de los padres.")
print("2 --> Visualiza los nombres de las madres.")
print("3 --> Visualiza los miembros de la unidad familiar.")
print("4 --> Muestra todos los datos")

opcion = int(input("Ingresa opcion para visualizar: "))

if opcion == 1:
    for i in range(1,len(curso),4):
        print(curso[i])
elif opcion == 2:
    for i in range(2,len(curso),4):
        print(curso[i])
elif opcion == 3:
    for i in range(3,len(curso),4):
        print(curso[i])
elif opcion == 4:
    for i in curso:
        print(i, end=", ")