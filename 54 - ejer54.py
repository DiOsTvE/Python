"""
Clase Padre Personaje:
- Nombre. Preguntar el nombre.
- Fuerza. Preguntar la fuerza (Al azar).
- Altura. Preguntar la altura (Al azar).
- Salud. Preguntar la salud (Al azar).
- Posicion. = 0.
    * Avanzar. Avanza 2 en su posicion.
    * Retroceder. Retrocede 1 en su posicion.
Clase Hija Heroe:
- Medallas. Preguntar cuantas medallas posee (Al azar).
    * Atacar. Equivale a Fuerza por Medalla.
- Cuando un Heroe ha realizado 5 ataques se le da una medalla.
Clase Hija Villano:
- Maldad. Preguntar la Maldad del Villano (Al azar).
    * Atacar. Equivale Maldad mas Fuerza.
"""
class Personaje:
    def __init__(self):
        self.nombre = input("Cual es el nombre del personaje: ")
        self.fuerza = int(input("Cual es la fuerza del personaje: "))
        self.altura = float(input("Cual es la altura del personaje: "))
        self.salud = int(input("Cual es la salud del personaje: "))
        self.posicion = 0
    def avanzar(self):
        if self.posicion > 10:
            self.posicion = 10
            return self.posicion
        else:
            self.posicion = self.posicion + 2
            return self.posicion
    def retroceder(self):
        if self.posicion == 0:
            self.posicion = 0
            return self.posicion
        else:
            self.posicion = self.posicion - 1
            return self.posicion
    def mostrarPersonaje(self):
        print("Nombre: ",self.nombre)
        print("Fuerza: ",self.fuerza)
        print("Altura: ",self.altura)
        print("Salud: ",self.salud)
        print("Posicion: ",self.posicion)
class Heroe(Personaje):
    def __init__(self):
        super().__init__()
        self.medallas = int(input("Cuantas medallas tiene el heroe: "))
        self.contador = 0
    def atacar(self):
        self.subenivel()
        self.ataco = super().fuerza * self.medallas
        return self.ataco
    def subenivel(self):
        self.contador = self.contador + 1
        if self.contador == 5:
            self.medallas = self.medallas + 1
            self.contador = 0
    def mostrarPersonaje(self):
        super().mostrarPersonaje()
        print("Medallas: ",self.medallas)
        print("Nivel: ",self.contador)
class Villano(Personaje):
    def __init__(self):
        super().__init__()
        self.maldad = int(input("Introduce la maldad del personaje: "))
    def atacar(self):
        self.ataco = super().fuerza + self.maldad
        return self.ataco
    def mostrarPersonaje(self):
        super().mostrarPersonaje()
        print("Maldad: ",self.maldad)
class Menu:
    def __init__(self):
        self.opcion = -1
        self.personajes = {}
        self.heroes = {}
        self.villanos = {}
        self.cuenta_personajes = 0
        self.cuenta_heroes = 0
        self.cuenta_villanos = 0
    def menuInicio(self):
        print("++++++++++++++++++++++++++++++++++++++++")
        print("+++                                  +++")
        print("+++   0. Salir                       +++")
        print("+++   1. Crea Personaje              +++")
        print("+++   2. Crea Heroe                  +++")
        print("+++   3. Crea Villano                +++")
        print("+++                                  +++")
        print("+++                                  +++")
        print("+++                                  +++")
        print("+++                                  +++")
        print("+++                                  +++")
        print("++++++++++++++++++++++++++++++++++++++++")
    def menuCompleto(self):
        print("++++++++++++++++++++++++++++++++++++++++")
        print("+++                                  +++")
        print("+++   0. Salir                       +++")
        print("+++   1. Crea Personaje              +++")
        print("+++   2. Crea Heroe                  +++")
        print("+++   3. Crea Villano                +++")
        print("+++   4. Mostrar Personaje           +++")
        print("+++   5. Avanzar                     +++")
        print("+++   6. Retroceder                  +++")
        print("+++   7. Atacar                      +++")
        print("+++                                  +++")
        print("++++++++++++++++++++++++++++++++++++++++")
    def mostrarPersonaje(self):
        print("++++++++++++++++++++++++++++++++++++++++")
        print("+++                                  +++")
        print("+++   0. Salir                       +++")
        print("+++   1. Mostrar Personaje           +++")
        print("+++   2. Mostrar Heroe               +++")
        print("+++   3. Mostrar Villano             +++")
        print("+++                                  +++")
        print("+++                                  +++")
        print("+++                                  +++")
        print("+++                                  +++")
        print("+++                                  +++")
        print("++++++++++++++++++++++++++++++++++++++++")
    def elegir(self):
        self.opcion = int(input("Elegir opcion: "))
        return self.opcion
    def opciones(self):
        if self.opcion == 1:
            self.personaje1 = Personaje()
            self.cuenta_personajes = self.cuenta_personajes + 1
            self.personajes[self.cuenta_personajes] = self.personaje1
        elif self.opcion == 2:
            self.heroe1 = Heroe()
            self.cuenta_heroes = self.cuenta_heroes + 1
            self.heroes[self.cuenta_heroes] = self.heroe1
        elif self.opcion == 3:
            self.villano1 = Villano()
            self.cuenta_villanos = self.cuenta_villanos + 1
            self.villanos[self.cuenta_villanos] = self.villano1
        elif self.opcion == 4:
