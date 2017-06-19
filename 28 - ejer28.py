"""
Ingresar dos cadenas y que si existe una nueva cadena introducida en las
dos cadenas y en que posicion.
"""
"""
cadena1 = input("Introduce una cadena: ")
cadena2 = input("Introduce otra cadena: ")
texto = input("Introduce texto a buscar en las cadenas: ")

longitud_total_cadena1 = len(cadena1)
print("Tamaño total de la cadena1: ",longitud_total_cadena1)
longitud_total_cadena2 = len(cadena2)
print("Tamaño total de la cadena2: ",longitud_total_cadena2)

longitud_cadena_a_buscar = len(texto)
print("Tamaño de la subcadena: ",longitud_cadena_a_buscar)
maximo_cadena1 = longitud_total_cadena1-longitud_cadena_a_buscar
maximo_cadena2 = longitud_total_cadena2-longitud_cadena_a_buscar

print("Maximo a llegar en cadena1: ",maximo_cadena1)
print("Maximo a llegar en cadena2: ",maximo_cadena2)

contador_cadena1 = 0
contador_cadena2 = 0
print(maximo_cadena1)
print(maximo_cadena2)
primera_pos_cadena1 = -1
primera_pos_cadena2 = -1

for i in range(maximo_cadena1+1):
    existe_cadena1 = cadena1.find(texto,i,i+longitud_cadena_a_buscar)
    if existe_cadena1 != -1:
        contador_cadena1 = contador_cadena1 + 1
        if primera_pos_cadena1 == -1:
            primera_pos_cadena1 = existe_cadena1
print("Se repite ",contador_cadena1," veces")
print("La primera posicion encontrada es: ",primera_pos_cadena1)
for i in range(maximo_cadena2+1):
    existe_cadena2 = cadena2.find(texto,i,i+longitud_cadena_a_buscar)
    if existe_cadena2 != -1:
        contador_cadena2 = contador_cadena2 + 1
        if primera_pos_cadena2 == -1:
            primera_pos_cadena2 = existe_cadena2
print("Se repite ",contador_cadena2," veces")
print("La primera posicion encontrada es: ",primera_pos_cadena2)
if(primera_pos_cadena1 == primera_pos_cadena2):
    print("Se encuentran en la misma posición.")
"""
"""
Introducir las ventas realizadas en el primer trimestre de cada uno de 
los tres empleados de lo que consta la empresa. Las ventas se pedirán
mes a mes y por cada empleado. Decir el promedio de cada empleado y el
nombre del empleado que tenga mejor promedio de los tres.
"""
meses = ("Enero","Febrero","Marzo")
empleados = ("Fran","César","Nuria")
ventas = []
promedio = []

for h in empleados:
    print("Ventas del empleado: ",h)
    for i in meses:
        print("Ventas del mes de: ",i)
        ventas.append(float(input("Introduce las ventas: ")))

print(ventas)
acum = 0
corte = 2

for h in range(len(empleados)):
    for i in range(len(ventas)):
        acum = acum + i
        if i >= corte:
            promedio.append(acum)
            print("El promedio del empleado: ", h, " es: ",acum)
            acum = 0
            corte = corte + 3


