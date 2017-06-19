"""
Realizar una aplicación que realice la suma, la resta, la multiplicación
y la división. Que pida dos números y realizar un menú con las operaciones,
todo en funciones.
"""
opcion = 0
n1 = 'nulo'
n2 = 'nulo'
def menu():
    print("****************************")
    print("** OPERACIONES A REALIZAR **")
    print("** 1. Pide los números    **")
    print("** 2. Suma                **")
    print("** 3. Resta               **")
    print("** 4. Multiplicacion      **")
    print("** 5. Division            **")
    print("** 6. Salir               **")
    print("****************************")
    opcion = int(input("Introduce opcion: "))
    return opcion

def uno():
    numero = float(input("Introduce el numero: "))
    return  numero

def opera(operacion,numero1,numero2):
    if operacion == 2:
        return numero1 + numero2
    elif operacion == 3:
        return numero1 - numero2
    elif operacion == 4:
        return  numero1 * numero2
    elif operacion == 5:
        return  numero1 / numero2

def imprime(resultado):
    print("El resultado de la operacion, ha sido: ",resultado)

while opcion < 1 or opcion > 7 and opcion != 6:
    opcion = menu()
    if opcion == 1:
        n1 = uno()
        n2 = uno()
        opcion = menu()
        if opcion == 1:
            print("Error. Ya habias introducido los numeros.")
            n1 = 'nulo'
            n2 = 'nulo'
            opcion = 0
        elif opcion == 2 and (n1 != 'nulo' and n2 != 'nulo'):
            print("Has elegido la operacion suma.")
            resultado = opera(opcion,n1, n2)
        elif opcion == 3 and (n1 != 'nulo' and n2 != 'nulo'):
            print("Has elegido la operacion resta.")
            resultado = opera(opcion,n1, n2)
        elif opcion == 4 and (n1 != 'nulo' and n2 != 'nulo'):
            print("Has elegido la operacion multiplicacion.")
            resultado = opera(opcion,n1, n2)
        elif opcion == 5 and (n1 != 'nulo' and n2 != 'nulo'):
            print("Has elegido la operacion division.")
            resultado = opera(opcion,n1, n2)
        if n1 != 'nulo' and n2 != 'nulo':
            imprime(resultado)
            opcion = 0
    elif opcion == 6:
        print("Fin de la aplicacion.")
    else:
        print("Operacion no valida.")
        print("Debes introducir primero los numeros o elegir la opcion correcta.")
        opcion = 0