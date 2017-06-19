"""
Funciones con paso de parámetros
"""
def sumar(n1, n2):
    rdo = n1 + n2
    print(rdo)
def restar(n1, n2):
    rdo = n1 - n2
    print(rdo)
def pedir():
    num1 = int(input("Ingrese un número: "))
    num2 = int(input("Ingrese otro número: "))
    sumar(num1, num2)
    restar(num1, num2)
pedir()
