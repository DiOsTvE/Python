import  random
preguntas = ['Color del caballo de Santiago??','Capital de Groelandia??',
             '7+7+7 es igual a...','Gentilicio de Sonseca??',
             'Numero de camiseta de Iniesta en la seleccion']
respuestas = ['blanco','nuuk','21','sonsecano','6']

pregun = random.choice(preguntas)
posicion = preguntas.index(pregun)
resp = input(pregun).lower()
if resp == respuestas[posicion]:
    print("Correcto")
else:
    print("Incorrecto")
