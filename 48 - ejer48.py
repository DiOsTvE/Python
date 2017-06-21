# -*- coding: utf-8 *-*
"""
Crear una clase cuyo nombre va a ser Persona, los atributos de la
clase son: nombre, apellidos y edad. Debemos crear el metodo para
construir un objeto de tipo Persona, otro metodo para mostrar los
datos de la Persona, otro metodo para saber si es mayor de edad o
no. Creamos tres personas.
"""
class Persona:
    def constructor(self, nombre, apellidos, edad):
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad
    def mostrarDatos(self):
        print("Nombre: ", self.nombre)
        print("Apellidos: ", self.apellidos)
        print("Edad: ", self.edad)
    def mayoriaEdad(self):
        if self.edad >= 18:
            print(self.nombre, " es mayor de edad")
        else:
            print(self.nombre, " no es mayor de edad")

fuente_nombre = []

for i in range(3):
    nombre = input("Introduce nombre: ")
    apellidos = input("Introduce los apellidos: ")
    edad = int(input("Introduce la edad: "))

    fuente_nombre.append(nombre)

    fuente_nombre[i] = Persona()
    fuente_nombre[i].constructor(nombre,apellidos,edad)

for i in range(3):
    fuente_nombre[i].mostrarDatos()
    fuente_nombre[i].mayoriaEdad()


