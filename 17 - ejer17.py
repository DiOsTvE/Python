"""
Ingresar seis ventas de los primeros seis meses del año
y calcular el promedio de ventas del primer semestre.
"""
"""
ventas = []
money = 0
acum = 0
for i in range(6):
    money = float(input(f"Ingresa el importe de la venta {i+1}: "))
    ventas.append(money)
print("Se han introducido: ",len(ventas), " ventas")
for i in range(len(ventas)):
    acum = acum + ventas[i]
promedio = acum / len(ventas)
print("El promedio de ventas en el primer semestre es: ", promedio)
"""
"""
Idem del anterior, pero a la hora de pedir las ventas que
aparezca el mes correspondiente.
"""
"""
ventas = []
meses = ('Enero','Febrero','Marzo','Abril','Mayo','Junio')
money = 0
acum = 0
for i in meses:
    money = float(input(f"Ingresa el importe de la venta del mes de "+i+": "))
    ventas.append(money)
for i in ventas:
    acum = acum + i
promedio = acum / len(ventas)
print("El promedio de ventas en el primer semestre es: ", promedio)
"""
"""
Tenemos tres cursos: word, excel y access. Cada curso tiene
una cantidad de alumnos: word --> 4, excel --> 5, access --> 7,
el programa debe calcular el promedio de notas de cada curso.
"""

asignaturas = ("word", "excel", "access")
alumnos = (4, 5, 7)
nota_w = []
nota_e = []
nota_a = []
notas = [nota_w, nota_e, nota_a]

for h in range(len(asignaturas)):
    print("Notas de ", asignaturas[h])
    num_alumnos = alumnos[h]
    for i in range(num_alumnos):
        notas[h].append(float(input(f"Inserta la nota {i+1}: ")))

acum = 0
promedio = 0
for i in range(len(notas)):
    for j in range(len(notas[i])):
        acum = acum + notas[i][j]
    promedio = acum / len(notas[i])
    print("La nota media de ", asignaturas[i], " es de: ", promedio)
    acum = 0

