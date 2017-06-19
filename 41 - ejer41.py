nombre = ['sergio','david','alberto','esteban']
veces = []
frase = input("Ingrese frase: ")
for i in range(4):
    veces.append(frase.count(nombre[i]))
for i in range(4):
    print(nombre[i],": ",veces[i])