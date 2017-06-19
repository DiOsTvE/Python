"""
Más metodos de cadenas
"""
cadena = 'Pa mi pa vos pa ninguno de los dos'
print(cadena.title())
print(str(len(cadena)))
print(cadena.center(40,"-"))
print(cadena.rjust(40,"-"))
print(cadena.ljust(40,"-"))
numero = 123
print(str(numero).zfill(10))
cadena1 = cadena.lower()
cantidad = cadena1.count("pa")
print(cantidad)
cadena2 = "mi carro me lo robaron"
posicion = cadena2.find("carro")
posicion2 = cadena2.find("carro",0,9)
print(posicion)
print(posicion2)