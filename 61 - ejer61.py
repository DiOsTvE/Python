archivo = open("archivos/prueba.txt","r")
linea1 = archivo.readline()
print(linea1)
print("----------------------------")
pos = archivo.tell()
print("Posicion: ",pos)
print("----------------------------")
archivo.seek(0)
contenido = archivo.read()
print(contenido)
print("----------------------------")
pos = archivo.tell()
print("Posicion: ",pos)
print("----------------------------")
archivo.seek(0)
for linea in archivo.readlines():
    print (linea)
print("----------------------------")
print("****************************")
print("----------------------------")
archivo = open("archivos/prueba.txt","r+")
contenido = archivo.read()
print(contenido)
print("----------------------------")
archivo.write("\nNueva linea escrita desde codigo.")
archivo.seek(0)
contenido = archivo.read()
print(contenido)
print("----------------------------")
print("----------------------------")
print("****************************")
print("----------------------------")
final_archivo = archivo.tell()
lista_añadir_archivos = ['\nElemento1\n','Elemento2\n']
archivo.writelines(lista_añadir_archivos)
archivo.seek(final_archivo)
print(archivo.readline())
print(archivo.readline())
print("----------------------------")
print("----------------------------")
print("****************************")
print("----------------------------")
"""
import os
from subprocess import call
os.system('cls')
"""
archivo.seek(0)
contenido = archivo.read()
archivo.close()
print(contenido)
