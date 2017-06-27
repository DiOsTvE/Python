"""
Crear la clase deportista, atributos:
- Nombre
- Edad
- Tiempo
Metodos:
- init
- mostrarDatos
Crear tres deportistas, tambien crear una variable
que nos muestre la media de los tiempos, ver si esta
por encima o por debajo de la media de los tiempos
"""
class Deportista():
    totalTiempo = 0
    contador = 0
    def __init__(self):
        self.nombre = input("Escribe tu nombre: ")
        self.edad = int(input("Escribe la edad: "))
        self.tiempo = float(input("Escribe el tiempo realizado(segundos): "))
        Deportista.totalTiempo = Deportista.totalTiempo + self.tiempo
        Deportista.contador = Deportista.contador + 1
    def mostrarDatos(self):
        print("Nombre: ", self.nombre)
        print("Edad: ",self.edad)
        print("Tiempo: ",self.tiempo)
    def calculoMedia(self):
        media = float(Deportista.totalTiempo / Deportista.contador)
        if self.tiempo > media:
            print("El deportista llamado ",self.nombre," esta por encima de la media, con una media de ",media)
        elif self.tiempo < media:
            print("El deportista llamado ",self.nombre," esta por debajo de la media, con una media de ",media)
        else:
            print("El deportista llamado ",self.nombre," esta en la media, con una media de ",media)

salir = 'n'
deportistas = []
while salir != "s":
    depor = Deportista()
    deportistas.append(depor)
    salir = input("Desea salir(s/n): ")

for corredor in deportistas:
    corredor.mostrarDatos()
    corredor.calculoMedia()
"""

"""