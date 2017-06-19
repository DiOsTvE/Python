"""
Nos ingresa un número, si es de una, dos, tres o cuatro cifras,
si tiene más de cuatro cifras, decir tiene más de cuatro cifras
"""
numero = int(input("Introduce un numero: "))
if numero < 0:
    print("El número es negativo")
elif numero < 10:
    print("El número es de una cifra")
elif numero < 100:
    print("El número es de dos cifras")
elif numero < 1000:
    print("El número es de tres cifras")
elif numero < 10000:
    print("El número es de cuatro cifras")
else:
    print("El número tiene más de cuatro cifras")
