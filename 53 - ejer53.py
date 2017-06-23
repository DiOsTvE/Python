class Persona:
    def __init__(self):
        self.dni = input("Ingrese dni: ")
        self.nombre = input("Ingrese nombre: ")
        self.edad = int(input("Ingrese su edad: "))
    def esMayor(self):
        if self.edad >= 18:
            print("Es mayor de edad.")
        else:
            print("No es mayor de edad.")
    def mostrar(self):
        print("Dni: ",self.dni)
        print("Nombre: ",self.nombre)
        print("Edad: ",self.edad)

class Empleado(Persona):
    def __init__(self):
        super().__init__()
        self.sueldo = float(input("Ingrese el sueldo: "))
        self.cargo = input("Ingrese el puesto de trabajo: ")
    def mostrar(self):
        super().mostrar()
        print("Sueldo: ",self.sueldo)
        print("Cargo: ",self.cargo)
    def calcularSueldo(self):
        anio = self.sueldo * 12
        return anio

persona1 = Persona()
persona1.mostrar()
persona1.esMayor()
empleado1 = Empleado()
empleado1.mostrar()
sueldoanual = empleado1.calcularSueldo()
print("El sueldo al año es: ", sueldoanual)