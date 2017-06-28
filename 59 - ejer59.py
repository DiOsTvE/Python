"""
Crear la clase jugador.
Atributos:
- nick
- posicion
Metodos:
- mostrarDatos
- avanzar
- retroceder
Crear menu:
1. Turno Jugador 1 --> Genera numero aleatorio entre 0 y 3. Si sale de 1 a 3, es lo que avanza.
Si saca 0, retrocede 1.
2. Turno Jugador 2 --> Genera numero aleatorio entre 0 y 3. Si sale de 1 a 3, es lo que avanza.
Si saca 0, retrocede 1.
Gana el que ha llegado mas lejos cuando llegue a los 10 turnos.
"""
import random
class Jugador():
    turnos = 0
    def __init__(self):
        self.nick = input("Introduce nick: ")
        self.posicion = 0
    def mostrarDatos(self):
        print("Nick: ",self.nick)
        print("Posicion: ",self.posicion)
        print("------------------------")
    def avanzar(self):
        pasos = random.randint(0,3)
        if pasos > 0:
            self.posicion = self.posicion + pasos
        else:
            self.retroceder()
        self.totalTurnos()
    def retroceder(self):
        if self.posicion > 0:
            self.posicion = self.posicion - 1
        else:
            self.posicion = 0
        self.totalTurnos()
    def totalTurnos(self):
        Jugador.turnos = Jugador.turnos + 1
        print("Turno: ",Jugador.turnos)
        print("----------------------")
class CorredorA(Jugador):
    def __init__(self):
        super().__init__()
        self.jugadoA = 0
class CorredorB(Jugador):
    def __init__(self):
        super().__init__()
        self.jugadoB = 0
class Menu():
    def __init__(self):
        self.opcion = 0
    def mostrarMenu(self):
        print("++++++++++++++++++++++++++++")
        print("++                        ++")
        print("++  1.TURNO JUGADOR 1     ++")
        print("++                        ++")
        print("++  2.TURNO JUGADOR 2     ++")
        print("++                        ++")
        print("++++++++++++++++++++++++++++")
    def opcionMenu(self):
        self.opcion = int(input("Elige opcion: "))

corredorA = CorredorA()
corredorB = CorredorB()
corredorA.mostrarDatos()
corredorB.mostrarDatos()
menu_juego = Menu()
while menu_juego.opcion != -1:
    menu_juego.mostrarMenu()
    menu_juego.opcionMenu()
    if menu_juego.opcion == 1:
        if corredorA.jugadoA == 0:
            if Jugador.turnos < 20:
                corredorA.avanzar()
                corredorA.jugadoA = 1
                corredorB.jugadoB = 0
                corredorA.mostrarDatos()
                corredorB.mostrarDatos()
            else:
                corredorA.mostrarDatos()
                corredorB.mostrarDatos()
                if corredorA.posicion > corredorB.posicion:
                    print("El corredor A ha ganado la partida.")
                elif corredorB.posicion > corredorA.posicion:
                    print("El corredor B ha ganado la partida.")
                else:
                    print("Los corredores has llegado a la vez.")
                menu_juego.opcion = -1
        else:
            print("Turno del corredor B.")
    else:
        if Jugador.turnos < 20:
            if corredorB.jugadoB == 0:
                corredorB.avanzar()
                corredorB.jugadoB = 1
                corredorA.jugadoA = 0
                corredorA.mostrarDatos()
                corredorB.mostrarDatos()
            else:
                print("Turno del corredor A.")
        else:
            corredorA.mostrarDatos()
            corredorB.mostrarDatos()
            if corredorA.posicion > corredorB.posicion:
                print("El corredor A ha ganado la partida.")
            elif corredorB.posicion > corredorA.posicion:
                print("El corredor B ha ganado la partida.")
            else:
                print("Los corredores has llegado a la vez.")
            menu_juego.opcion = -1