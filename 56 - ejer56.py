class Alumno():
    aprobados = []
    def __init__(self):
        self.dni = input("Ingrese dni: ")
        self.nombre = input("Introduce nombre: ")
    def aprobar(self):
        Alumno.aprobados.append(self.dni)
    def mostrarDatos(self):
        print("Nombre: ",self.nombre)
        print("Dni: ",self.dni)
    def estaAprobado(self):
        if self.dni in Alumno.aprobados:
            print("Esta aprobado")
        else:
            print("Esta suspenso")

alumno1 = Alumno()
alumno2 = Alumno()
alumno3 = Alumno()
alumno1.aprobar()
alumno3.aprobar()
alumno1.estaAprobado()
alumno2.estaAprobado()
alumno3.estaAprobado()