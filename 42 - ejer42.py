"""
Rellenamos una lista con el nombre de cinco alumnos,
rellenar otra lista con la nota final de esos cinco alumnos,
con array asociativo
"""
"""
nombres = []
notas = []

for i in range(4):
    nombres.append(input("Inserta el nombre del alumno: ").lower())
    notas.append(float(input("Ingresa la nota del alumno: ")))
for i in range(4):
    print("El alumno ",nombres[i],"tiene una nota de ",notas[i])
"""
"""
Con diccionario, solicitar las ventas mensuales del ultimo trimestre.
"""
diccionario = {'Octubre':0,'Noviembre':0,'Diciembre':0}
for i in diccionario:
    ventas = float(input("Ingresa las ventas mensuales del mes de "+i+": "))
    diccionario[i] = ventas

print(diccionario)