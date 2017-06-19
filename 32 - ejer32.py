"""
Mas funciones
"""
def sumar(n1, n2):
    rdo = n1 + n2
    print(rdo)
def restar(n1, n2):
    rdo = n1 - n2
    print(rdo)
def pedir():
    num = int(input("Ingrese un número: "))
    return num

num1 = pedir()
num2 = pedir()
sumar(num1, num2)
restar(num1, num2)