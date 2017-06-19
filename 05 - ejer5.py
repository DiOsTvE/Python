"""
Se piden dos números, si son iguales sumamos
si el primero es mayor que el segundo los restamos
si el segundo es mayor que el primero los multiplicamos
"""
n1 = float(input("Ingrese un número: "))
n2 = float(input("Ingrese otro número: "))
if n1==n2:
    rdo=n1+n2
else:
    if n1>n2:
        rdo=n1-n2
    else:
        rdo=n1*n2
print("Resultado: ")
print(rdo)

if n1==n2:
    rdo=n1+n2
elif n1>n2:
    rdo=n1-n2
else:
    rdo=n1*n2
