"""
Ingresar 5 números y decir si son múltiplos de 3 o no.
"""
"""
for i in range(5):
    numero = int(input(f"Ingresa el número {i}: "))
    if(numero % 3)==0:
        print("Es múltiplo de 3")
    else:
        print("No es múltiplo de 3")
"""
"""
Ingresar 10 números enteros y contar cuántos de esos
números son distintos de 0.
"""
"""
acum = 0
for i in range(10):
    numero = int(input(f"Ingresa el número {i}: "))
    if(numero != 0):
        acum = acum + 1
print("La cantidad de números enteros distintos de 0 son: ")
print(acum)
"""
"""
Realice un programa que muestre una cuenta regresiva desde el 20 al 0.
"""
"""
for i in range(20,-1,-1):
    print(i)
"""
"""
Realice un programa donde se ingresen una cantidad de compras diarias
y se muestre el total facturado ese día.
"""
"""
total = 0
importe = 0
compras = int(input("Cuantas compras has realizado en el día: "))

for i in range(compras):
    importe = float(input(f"Inserta el importe de la compra {i+1}: "))
    total = total + importe

print("El total facturado en el día es: ")
print(total)
"""
"""
Realice un programa que solicite los lados de 5 triángulos y especifique
qué tipo de triangulo es cada uno de ellos
"""
"""
aux = 0
aux2 = 0
cuenta = 1
lado = 0
for i in range(3):
    while lado == 0:
        lado = float(input(f"Introduce el lado {i+1}: "))
        if lado == 0:
            print("Valor no válido.")
    if aux == 0:
        aux = lado
    elif aux == lado:
        cuenta = cuenta + 1
        aux2 = lado
    elif aux == lado or aux2 == lado:
        cuenta = cuenta + 1
    lado=0
if cuenta == 1:
    print("El triangulo es escaleno")
elif cuenta == 2:
    print("El triangulo es isosceles")
elif cuenta == 3:
    print("El triangulo es equilatero")
else:
    print("No es un triangulo")
"""
"""
Realice un programa que escriba la tabla de multiplicar de
un número ingresado por el usuario. También debe indicar el
inicio y el fin de la tabla.
"""
"""
numero = int(input("Introduce un número para mostrar su tabla de multiplicar: "))
print("La tabla de multiplicar del", numero)
for i in range(11):
    print(numero,"*",i,"=",i*numero)
print("Fin de la tabla de multiplicar del", numero)
"""
"""
Desarrollar un programa que muestre la tabla del 5 (del 5 al 50)
"""
"""
print("La tabla de multiplicar del 5")
for i in range(11):
    print("5 *",i,"=",i*5)
print("Fin de la tabla de multiplicar del 5")
"""
"""
Se desea obtener una serie de promedios partiendo de:
a - Las notas de 5 estudiantes de física.
b - Las notas de 7 estudiantes de programación.
c - Las notas de 8 estudiantes de medicina.
Se debe: Obtener el promedio de notas por cada carrera y mostrar
cual es la carrera que presenta mejor promedio.
"""
prom_fis = 0
nota = 0

for i in range(5):
    nota = float(input(f"Introduce la nota {i+1} de física: "))
    prom_fis = prom_fis + nota
prom_fis = prom_fis / 5
print("La nota media de física es: ",prom_fis)

prom_pro = 0
nota = 0

for i in range(7):
    nota = float(input(f"Introduce la nota {i+1} de programación: "))
    prom_pro = prom_pro + nota
prom_pro = prom_pro / 7
print("La nota media de programación es: ",prom_pro)

prom_med = 0
nota = 0
for i in range(8):
    nota = float(input(f"Introduce la nota {i+1} de medicina: "))
    prom_med = prom_med + nota
prom_med = prom_med / 8
print("La nota media de medicina es: ",prom_med)

if prom_fis > prom_pro and prom_fis > prom_med:
    print("La carrera con mejor promedio es Física, con una nota media de ",prom_fis)
elif prom_pro > prom_fis and prom_pro > prom_med:
    print("La carrera con mejor promedio es Programación, con una nota media de ",prom_pro)
else:
    print("La carrera con mejor promedio es Medicina, con una nota media de ",prom_med)
