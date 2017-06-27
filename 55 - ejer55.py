class Persona():
    acum = 0
    def __init__(self,nom,ed):
        self.nombre = nom
        self.edad = ed
        Persona.acum = Persona.acum + self.edad
    def esMayor(self):
        if self.edad >= 18:
            print("Es mayor")
        else:
            print("Es menor")
    def encimaMedia(self):
        media = int(Persona.acum/2)
        if self.edad > media:
            print(self.nombre, " esta por encima de la media")
        elif self.edad < media:
            print(self.nombre, " esta por debajo de la media")
        else:
            print(self.nombre, " coincide con la media")


n = input("Ingrese un nombre: ")
e = int(input("Ingrese su edad: "))
persona1 = Persona(n,e)
persona1.esMayor()

n = input("Ingrese un nombre: ")
e = int(input("Ingrese su edad: "))
persona2 = Persona(n,e)
persona2.esMayor()

persona1.encimaMedia()