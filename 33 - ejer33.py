"""
Pedir la base y altura del rectangulo, realizar una funcion
para calcular el área
"""
"""
def calcular_area(base, altura):
    rdo = base * altura
    return  rdo
def pedir(elemento):
    print("Ingrese la",elemento,end="")
    medida = float(input(": "))
    return medida

base = pedir('base')
altura = pedir('altura')
area = calcular_area(base, altura)
print("El área del rectangulo es:",area)
"""
"""
Realizar una funcion que reciba una cadena de caracteres y que
diga cuantas veces figura la letra a
"""
contador = 0
def repeticion(cadena):
    global contador
    for i in range(len(cadena)):
        if cadena[i] == 'a':
            contador = contador + 1
    return contador

cadena = input("Introduce una cadena: ")
cantidad = repeticion(cadena)
print("La cantidad de aes es: ",cantidad)