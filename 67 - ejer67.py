"""
Metodo para ver contenido de un objeto --> str
"""
class Persona():
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
    def mostrarDatos(self):
        print("Nombre: ",self.nombre)
        print("Edad: ",str(self.edad))
    def __str__(self):
        #print("Nombre: ", self.nombre)
        #print("Edad: ", str(self.edad))
        cadena  = "Nombre: " + self.nombre + ", Edad: " + str(self.edad) + " años."
        return cadena
    def __eq__(self, p2):
        if self.edad == p2.edad:
            return True
        else:
            return False

persona1 = Persona('Martin',39)
print(persona1)

persona2 = Persona('Pepito Perez',40)
print(persona2)

if persona1 == persona2:
    print("Son de la misma edad.")
else:
    print("No son de la misma edad.")

!=_ __ne__(self,objeto2)
>=_ __ge__(self,objeto2)
<=_ __le__(self,objeto2)
>_  __gt__(self,objeto2)
<_  __lt__(self,objeto2)

suma __add__(self,objeto2)
resta __sub__(self,objeto2)
multi __mul__(self,objeto2)
divi __divi__(self,objeto2)