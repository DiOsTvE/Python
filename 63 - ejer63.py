"""
try:
    archivo = open("archivos/record.txt","w")
    archivo.write('pruebasssss')
    print("Vete a ver si lo ha creado alma candida")
    archivo.close()
except:
    print("Llama al fabricante")
"""
"""
try:
    num1 = float(input("Ingrese un numero: "))
    num2 = float(input("Ingrese otro numero: "))
    rdo = num1/num2
    print(rdo)
except ZeroDivisionError:
    print("No se puede dividir por cero.")
except:
    print("No se ha podido realizar la division...")
    print("revise los datos")
"""
try:
    archivo = open("archivos/record.txt","w")
    archivo.write('agregando texto')
    print("Vete a ver si lo ha creado alma candida")
    archivo.close()
except:
    print("Error al abrir el archivo")
try:
    archivo = open("archivos/record.txt","r")
    print("Contenido del archivo: ")
    print(archivo.read())
    archivo.close()
except:
    print("Error al leer el archivo")