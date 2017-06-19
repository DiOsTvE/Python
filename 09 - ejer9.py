"""
Ingresar una fecha (dd-mm-yyyy), decir si corresponde a alguna fecha
del primer trimestre.
"""
"""
dia = int(input("Introduce el día: "))
mes = int(input("Introduce el mes: "))
año = int(input("Introduce el año: "))

if mes >= 1 and mes <= 3:
    input("La fecha corresponde al primer trimestre")
else:
    input("La fecha no corresponde al primer trimestre")
"""
"""
Ingresar una fecha (dd-mm-yyyy), decir si es el primer día del año o no.
"""
"""
dia = int(input("Introduce el día: "))
mes = int(input("Introduce el mes: "))
año = int(input("Introduce el año: "))
if dia == 1 and mes == 1 and año == 2017:
    input("Es el primer día del año")
else:
    input("No es el primer día del año")
"""
"""
Solicitar las ventas mensuales y la antigüedad del vendedor, si las ventas
superan los 1000 y tiene más de 5 años de antigüedad, se le adjudican el 10%
de las ventas, si las ventas superan los 1000 y tiene menos de 5 años
de antigüedad le adjudicamos el 5% de las ventas. Si las ventas superan los
5000 o el vendedor supera los 10 años de antigüedad, le adjudicamos el 20% de
las ventas.
"""
bonificacion = 0
ventas_mes = float(input("Introduce las ventas mensuales: "))
antigüedad = float(input("Introduce la antigüedad(en años) del vendedor: "))

if ventas_mes > 1000 and ventas_mes < 5000 and antigüedad > 5:
    bonificacion = (ventas_mes * 10)/100

if ventas_mes > 1000 and antigüedad < 5:
    bonificacion = (ventas_mes * 5)/100

if ventas_mes > 5000 or antigüedad > 10:
    bonificacion = (ventas_mes * 20)/100

print("La bonificacion ha sido de: ")
print(bonificacion)
