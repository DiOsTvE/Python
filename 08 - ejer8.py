edad = int(input("Ingrese edad: "))
if edad >= 18 and edad <= 26:
    print("Puede acceder")
else:
    print("No puede acceder")
    
"""
Ingresan edad y altura y si es menor que 30 y la
altura superior a 1.80 puede jugar al baloncesto.
Si la altura es inferior a 1.80 o es mayor de 60
juega a la petanca
"""

edad =  int(input("Ingrese edad: "))
altura = float(input("Ingrese la altura: "))
if edad < 30 and altura > 1.80:
    print("Juegas al baloncesto")
if edad > 60 or altura < 1.80:
    print("Juegas a la petanca")
