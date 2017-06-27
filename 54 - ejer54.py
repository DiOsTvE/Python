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
import random
class Personaje:
    def __init__(self):
        self.nombre = input("Cual es el nombre del personaje: ").lower()
        self.fuerza = random.randint(1, 12)
        self.altura = float(input("Cual es la altura del personaje: "))
        self.salud = random.randint(100, 200)
        self.posicion = 0
    def avanzar(self):
        if self.posicion > 10:
            self.posicion = 10
            return self.posicion
        else:
            self.posicion = self.posicion + random.randint(1,2)
            return self.posicion
    def retroceder(self):
        if self.posicion == 0:
            self.posicion = 0
            return self.posicion
        else:
            self.posicion = self.posicion - random.randint(1,2)
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
        self.ataco = self.fuerza * self.medallas
        return self.ataco
    def subenivel(self):
        self.contador = self.contador + 1
        if self.contador == 5:
            print("Has subido de nivel, Felicidades.")
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
        self.ataco = self.fuerza + self.maldad
        return self.ataco
    def mostrarPersonaje(self):
        super().mostrarPersonaje()
        print("Maldad: ",self.maldad)
class Menu:
    def __init__(self):
        self.opcion = -1
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
        print("+++   0. Volver                      +++")
        print("+++   1. Mostrar Personaje           +++")
        print("+++   2. Mostrar Heroe               +++")
        print("+++   3. Mostrar Villano             +++")
        print("+++                                  +++")
        print("+++                                  +++")
        print("+++                                  +++")
        print("+++                                  +++")
        print("+++                                  +++")
        print("++++++++++++++++++++++++++++++++++++++++")
    def avanzas(self):
        print("++++++++++++++++++++++++++++++++++++++++")
        print("+++                                  +++")
        print("+++   0. Volver                      +++")
        print("+++   1. Avanzar Personaje           +++")
        print("+++   2. Avanzar Heroe               +++")
        print("+++   3. Avanzar Villano             +++")
        print("+++                                  +++")
        print("+++                                  +++")
        print("+++                                  +++")
        print("+++                                  +++")
        print("+++                                  +++")
        print("++++++++++++++++++++++++++++++++++++++++")
    def retrocedes(self):
        print("++++++++++++++++++++++++++++++++++++++++")
        print("+++                                  +++")
        print("+++   0. Volver                      +++")
        print("+++   1. Retroceder Personaje        +++")
        print("+++   2. Retroceder Heroe            +++")
        print("+++   3. Retroceder Villano          +++")
        print("+++                                  +++")
        print("+++                                  +++")
        print("+++                                  +++")
        print("+++                                  +++")
        print("+++                                  +++")
        print("++++++++++++++++++++++++++++++++++++++++")
    def atacas(self):
        print("++++++++++++++++++++++++++++++++++++++++")
        print("+++                                  +++")
        print("+++   0. Volver                      +++")
        print("+++   1. Ataca Heroe                 +++")
        print("+++   2. Ataca Villano               +++")
        print("+++                                  +++")
        print("+++                                  +++")
        print("+++                                  +++")
        print("+++                                  +++")
        print("+++                                  +++")
        print("+++                                  +++")
        print("++++++++++++++++++++++++++++++++++++++++")
    def elegir(self):
        self.opcion = int(input("Elegir opcion: "))

personajes = []
heroes = []
villanos = []

mimenu = Menu()
while mimenu.opcion != 0:
    mimenu.menuInicio()
    mimenu.elegir()
    if mimenu.opcion == 0:
        print("Fin del juego. Game Over.")
    elif mimenu.opcion == 1:
        personaje1 = Personaje()
        personajes.append(personaje1)
    elif mimenu.opcion == 2:
        heroe1 = Heroe()
        heroes.append(heroe1)
    elif mimenu.opcion == 3:
        villano1 = Villano()
        villanos.append(villano1)
    else:
        print("Opcion incorrecta. Elige otra opción.")
        print("-------------------------------------")
    try:
        personaje1
        heroe1
        villano1
    except NameError:
        print("")
    else:
        if len(personajes) >= 1 and len(heroes) >= 1 and len(villanos) >= 1:
            break
while mimenu.opcion != 0:
    mimenu.menuCompleto()
    mimenu.elegir()
    if mimenu.opcion == 0:
        print("Fin del juego. Game Over.")
    elif mimenu.opcion == 1:
        personaje1 = Personaje()
        personajes.append(personaje1)
    elif mimenu.opcion == 2:
        heroe1 = Heroe()
        heroes.append(heroe1)
    elif mimenu.opcion == 3:
        villano1 = Villano()
        villanos.append(villano1)
    elif mimenu.opcion == 4:
        while mimenu.opcion != 0:
            mimenu.mostrarPersonaje()
            mimenu.elegir()
            print("-----------------------------------")
            if mimenu.opcion == 1:
                for muestropersonas in personajes:
                    muestropersonas.mostrarPersonaje()
                    print("-----------------------------------")
            elif mimenu.opcion == 2:
                for muestroheroes in heroes:
                    muestroheroes.mostrarPersonaje()
                    print("-----------------------------------")
            elif mimenu.opcion == 3:
                for muestrovillanos in villanos:
                    muestrovillanos.mostrarPersonaje()
                    print("-----------------------------------")
            else:
                print("Opcion incorrecta. Elige otra opción.")
                print("-------------------------------------")
        mimenu.opcion = -1
    elif mimenu.opcion == 5:
        while mimenu.opcion != 0:
            mimenu.avanzas()
            mimenu.elegir()
            if mimenu.opcion == 1:
                for muestropersonas in personajes:
                    muestropersonas.mostrarPersonaje()
                    print("-----------------------------------")
                nombreperso = input("Elige el personaje por el nombre: ").lower()
                for elegir in range(len(personajes)):
                    if personajes[elegir].nombre == nombreperso:
                        movimiento = personajes[elegir].avanzar()
                        print("El Personaje se ha movido ",movimiento," pasos")
                        print("----------------------------------------------")
            elif mimenu.opcion == 2:
                for muestroheroes in heroes:
                    muestroheroes.mostrarPersonaje()
                    print("-----------------------------------")
                nombreperso = input("Elige el heroe por el nombre: ").lower()
                for elegir in range(len(heroes)):
                    if heroes[elegir].nombre == nombreperso:
                        movimiento = heroes[elegir].avanzar()
                        print("El Heroe se ha movido ",movimiento," pasos")
                        print("----------------------------------------------")
            elif mimenu.opcion == 3:
                for muestrovillanos in villanos:
                    muestrovillanos.mostrarPersonaje()
                    print("-----------------------------------")
                nombreperso = input("Elige el villano por el nombre: ").lower()
                for elegir in range(len(villanos)):
                    if villanos[elegir].nombre == nombreperso:
                        movimiento = villanos[elegir].avanzar()
                        print("El Villano se ha movido ",movimiento," pasos")
                        print("----------------------------------------------")
            else:
                print("Opcion incorrecta. Elige otra opción.")
                print("-------------------------------------")
        mimenu.opcion = -1
    elif mimenu.opcion == 6:
        while mimenu.opcion != 0:
            mimenu.retrocedes()
            mimenu.elegir()
            if mimenu.opcion == 1:
                for muestropersonas in personajes:
                    muestropersonas.mostrarPersonaje()
                    print("-----------------------------------")
                nombreperso = input("Elige el personaje por el nombre: ").lower()
                for elegir in range(len(personajes)):
                    if personajes[elegir].nombre == nombreperso:
                        movimiento = personajes[elegir].retroceder()
                        print("El Personaje ha retrocedido ",movimiento," pasos")
                        print("------------------------------------------------")
            elif mimenu.opcion == 2:
                for muestroheroes in heroes:
                    muestroheroes.mostrarPersonaje()
                    print("-----------------------------------")
                nombreperso = input("Elige el heroe por el nombre: ").lower()
                for elegir in range(len(heroes)):
                    if heroes[elegir].nombre == nombreperso:
                        movimiento = heroes[elegir].retroceder()
                        print("El Heroe ha retrocedido ",movimiento," pasos")
                        print("------------------------------------------------")
            elif mimenu.opcion == 3:
                for muestrovillanos in villanos:
                    muestrovillanos.mostrarPersonaje()
                    print("-----------------------------------")
                nombreperso = input("Elige el villano por el nombre: ").lower()
                for elegir in range(len(villanos)):
                    if villanos[elegir].nombre == nombreperso:
                        movimiento = villanos[elegir].retroceder()
                        print("El Villano ha retrocedido ",movimiento," pasos")
                        print("------------------------------------------------")
            else:
                print("Opcion incorrecta. Elige otra opción.")
                print("-------------------------------------")
        mimenu.opcion = -1
    elif mimenu.opcion == 7:
        while mimenu.opcion != 0:
            mimenu.atacas()
            mimenu.elegir()
            if mimenu.opcion == 1:
                for muestroheroes in heroes:
                    muestroheroes.mostrarPersonaje()
                    print("-----------------------------------")
                nombreperso = input("Elige el heroe por el nombre: ").lower()
                for elegir in range(len(heroes)):
                    if heroes[elegir].nombre == nombreperso:
                        villano_azar = random.randint(0,(len(villanos)-1))
                        print("El villano seleccionado es: ")
                        villanos[villano_azar].mostrarPersonaje()
                        if heroes[elegir].posicion == villanos[villano_azar].posicion:
                            print("El heroe puede atacar al villano, estan en la misma posicion.")
                            ostia = heroes[elegir].atacar()
                            if villanos[villano_azar].salud > 0:
                                print("La ostia del heroe ha sido de: ",ostia)
                                villanos[villano_azar].salud = villanos[villano_azar].salud - ostia
                                print("La salud del villano se queda en: ",villanos[villano_azar].salud)
                            elif villanos[villano_azar].salud <= 0:
                                print("El villano capú.")
                        else:
                            print("No puede atacar, no esta en la misma posicion.")
                        print("-------------------------------------------------------------")
            elif mimenu.opcion == 2:
                for muestrovillanos in villanos:
                    muestrovillanos.mostrarPersonaje()
                    print("-----------------------------------")
                nombreperso = input("Elige el villano por el nombre: ").lower()
                for elegir in range(len(villanos)):
                    if villanos[elegir].nombre == nombreperso:
                        heroe_azar = random.randint(0, (len(heroes) - 1))
                        print("El heroe seleccionado es: ")
                        heroes[heroe_azar].mostrarPersonaje()
                        if villanos[elegir].posicion == heroes[heroe_azar].posicion:
                            print("El villano puede atacar al heroe, estan en la misma posicion.")
                            ostia = villanos[elegir].atacar()
                            if heroes[heroe_azar].salud > 0:
                                print("La ostia del villano ha sido de: ",ostia)
                                heroes[heroe_azar].salud = heroes[heroe_azar].salud - ostia
                                print("La salud del heroe se queda en: ",heroes[heroe_azar].salud)
                            elif heroes[heroe_azar].salud <= 0:
                                print("El heroe capú.")
                        else:
                            print("No puede atacar, no esta en la misma posicion.")
                        print("-------------------------------------------------------------")
            else:
                print("Opcion incorrecta. Elige otra opción.")
                print("-------------------------------------")
        mimenu.opcion = -1
    else:
        print("Opcion incorrecta. Elige otra opción.")
        print("-------------------------------------")