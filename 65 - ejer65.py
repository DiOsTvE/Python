"""
Pedimos datos (numeros) y lo sumamos, guardamos en un archivo.
Abrimos archivo y leemos el dato, vemos si el numero es mayor
 de 100 o no.
"""
try:
    salir = 'n'
    num = 0

    while salir != 's':
        num = num + int(input("Introduce numeros: "))
        salir = input("Desea salir(s/n): ")

    print("La suma de los numeros ha sido de: ",num)

    archivo = open('archivos/sumatorio.txt', 'w')
    archivo.write(str(num))
    archivo.close()
except:
    print("Error acceder al archivo")

try:
    archivo = open('archivos/sumatorio.txt','r')
    linea = int(archivo.read())
    if linea > 100:
        print("El numero es mayor de 100")
    elif linea < 100:
        print("El numero es menor de 100")
    else:
        print("El numero es igual a 100")
    archivo.close()
except:
    print("Error al leer el archivo")
