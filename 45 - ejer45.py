agenda = {}
dato = []
seguir = 's'
while seguir == 's':
    fecha = input("Ingrese la fecha de la reunion(dd/mm/aaaa): ")
    hora = input("Ingrese la hora de la reunion(hh:mm): ")
    cita = input("¿Con quien te reunes?: ")
    lugar = input("¿Donde te reunes?: ")
    agenda[fecha] = (hora,cita,lugar)
    seguir = input("¿Desea seguir metiendo datos?(s/n): ")
while seguir == 's':
    dia = input("Ingresa la fecha que quieres consultar(dd/mm/aaaa): ")
    if dia in agenda:
        print("Hora de la cita: ",agenda[dia][0])
        print("Contacto: ",agenda[dia][1])
        print("Lugar: ",agenda[dia][2])
    else:
        print("No tienes cita ese dia")
    seguir = input("¿Deseas seguir consultando datos?(s/n): ")
print("Hasta pronto!!!")