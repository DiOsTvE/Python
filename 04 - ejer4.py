"""
Ingresar tres números reales(notas), calcular promedio y decir si han aprobado o no
"""
nota1 = float(input("Ingresa nota1: "))
nota2 = float(input("Ingresa nota2: "))
nota3 = float(input("Ingresa nota4: "))

promedio = (nota1+nota2+nota3)/3

print("La nota media ha sido: ")
print(promedio)

if promedio<5:
    print("Suspenso")
elif promedio<6:
    print("Suficiente")
elif promedio<7:
    print("Bien")
elif promedio<9:
    print("Notable")
elif promedio<10:
    print("Sobresaliente")
else:
    print("Error en la nota")
