"""
Ingresar una cadena de caracteres en minúsculas y cuente
cuantas vocales hay.
"""
"""
laa = 0
lae = 0
lai = 0
lao = 0
lau = 0

cadena = input("Ingresa una cadena: ")
for i in cadena:
    if i == 'a':
        laa = laa + 1
    elif i == 'e':
        lae = lae + 1
    elif i == 'i':
        lai = lai + 1
    elif i == 'o':
        lao = lao + 1
    elif i == 'u':
        lau = lau + 1
print("De la vocal a --> ", laa)
print("De la vocal e --> ", lae)
print("De la vocal i --> ", lai)
print("De la vocal o --> ", lao)
print("De la vocal u --> ", lau)
"""
"""
Ingresar una cadena de caracteres en minúsculas o mayúsculas
 y cuente cuantas vocales hay.
"""
"""
laa = 0
lae = 0
lai = 0
lao = 0
lau = 0

cadena = input("Ingresa una cadena: ")
for i in cadena.lower():
    if i == 'a':
        laa = laa + 1
    elif i == 'e':
        lae = lae + 1
    elif i == 'i':
        lai = lai + 1
    elif i == 'o':
        lao = lao + 1
    elif i == 'u':
        lau = lau + 1
print("De la vocal a --> ", laa)
print("De la vocal e --> ", lae)
print("De la vocal i --> ", lai)
print("De la vocal o --> ", lao)
print("De la vocal u --> ", lau)
"""
"""
Ingresar dos cadenas de caracteres y saber si son iguales.
"""
"""
error = 0
longitud = 0
cadena1 = input("Ingresa una cadena: ")
cadena2 = input("Ingresa otra cadena: ")

if len(cadena1) != len(cadena2):
    print("Las cadenas no son iguales")
else:
    for i in range(len(cadena1)):
        if cadena1[i].lower() != cadena2[i].lower():
            error = 1
    if error == 1:
        print("Las cadenas no son iguales")
    else:
        print("Las cadenas son iguales")
"""
"""
Ingresar una cadena de caracteres y veamos si puede ser un
 correo electrónico o no.
"""
"""
fin = 0
cant_arroba = 0
cant_punto = 0
pos_arroba = 0
pos_punto = 0
correo = input("Escribe un correo electrónico: ").lower()
for i in range(len(correo)):
    if correo[i] == '@':
        if i == 0:
            fin = 1
        else:
            cant_arroba = cant_arroba + 1
            if cant_arroba == 1:
                pos_arroba = i
            else:
                pos_arroba = 0
    elif correo[i] == '.':
        if i == 0:
            fin = 1
        else:
            if cant_arroba == 1:
                cant_punto = cant_punto + 1
                if cant_punto == 1:
                    pos_punto = i
                else:
                    pos_punto = 0
if fin == 1:
    print("No es un correo electrónico correcto")
elif cant_arroba == 0 or cant_punto == 0:
    print("No es un correo electrónico correcto")
elif cant_punto >= 2 or cant_arroba >= 2:
    print("No es un correo electrónico correcto")
elif pos_punto == pos_arroba + 1:
    print("No es un correo electrónico correcto")
else:
    print("Es una dirección de correo electrónico correcta")
"""
"""
Ingresar una cadena de caracteres y tenemos que decir si es
 válida o no. Se considerara válida si contiene entre 10 y 25
 caracteres, si no, no es válida.
"""
"""
acum = 0
cadena = input("Ingresa una cadena para saber si es válida: ")
for i in cadena:
    acum = acum + 1
if acum >= 10 and acum <= 25:
    print("La cadena es válida")
else:
    print("La cadena no es válida")
"""
"""
Realiza un programa para saber si en una cadena hay un caracter 'Z'.
"""
"""
cadena = input("Ingresa una cadena: ")
print(cadena)
for i in cadena:
    if i == 'z':
        print("aparecio la z")
    else:
        print("no es la z")
"""
"""
Decir si una frase ingresada por el usuario y debemos decir si dicha
frase comienza por la letra D.
"""
"""
correcto = 0
cadena = input("Ingresa una cadena: ")
if cadena[0].upper() == 'D':
    print("La frase comienza por D.")
else:
    print("La frase no comienza por D.")
"""
