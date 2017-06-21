class Alumno:
    def constructor(self, nombre, dni, nota):
        self.nombre = nombre
        self.dni = dni
        self.nota = nota
    def mostrarDatos(self):
        print("Nombre: ", self.nombre)
        print("Dni: ", self.dni)
        print("Nota: ", self.nota)
    def verFinal(self):
        if self.nota >= 5:
            print("Aprueba")
        else:
            print("Suspenso")

alumno1 = Alumno()
alumno1.constructor('Juan','0676767-i',9)
alumno2 = Alumno()
alumno2.constructor('Ana','99999999-k',8)
alumno1.mostrarDatos()
alumno2.mostrarDatos()
alumno1.verFinal()