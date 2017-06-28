import random #importacion de modulos

numerito = random.randint(1,50) #Numero aleatorio entre 1 y 50 (ambos inclusive)
print(numerito)

numerito2 = random.randrange(10) #Numero aleatorio entre 0 y 9 (numero no inclusive)
numerito3 = random.randrange(2,5) #Numero aleatorio entre 2 y 4 (ultimo numero no inclusive)
numerito4 = random.randrange(0,11,2) #Numero aleatorio entre 0 y 10 con salto 2 (ultimo numero no inclusive)
numerito5 = random.randrange(0,11,3) #Numero aleatorio entre 0 y 10 con salto 3 (ultimo numero no inclusive)
print(numerito2)
print(numerito3)
print(numerito4)
print(numerito5)

opcion = random.choice(['real madrid','barcelona','atletico de madrid','valencia']) #Elemento aleatorio entre una lista de ellos
print(opcion)

lista = ['ELEMENTO1','ELEMENTO2','ELEMENTO3'] #Elemento aleatorio entre una lista de ellos
opcion1 = random.choice(lista)
print(opcion1)

numerito6 = random.random() #Numero aleatorio float entre 0 y 1 (ambos inclusive)
print(numerito6)

numerito7 = random.uniform(1,9) #Numero aleatorio float entre 1 y 9 (ambos inclusive)
print(numerito7)

random.shuffle(lista) #Ordenacion aleatorio de una lista
print(lista)

