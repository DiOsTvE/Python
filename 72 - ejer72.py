"""
Abrir una pagina web, buscar una palabra que este en algun parrafo de la pagina web
y decir cuantas veces se repite.
"""
import urllib.request
from bs4 import BeautifulSoup

contador = 0
parrafos_en_mayusculas = []

pagina = urllib.request.urlopen(
    "https://www.xatakandroid.com/moviles-android/el-xiaomi-redmi-note-5-apunta-alto-en-su-primera-filtracion-snapdragon-660-y-carga-rapida-a-precio-imbatible")
html = BeautifulSoup(pagina, "html.parser")  # lxml ó lxml-xml ó xml ó html5lib

palabra = input("Escribe la palabra a buscar: ")
parrafos = html.find_all('p')

print(parrafos)
for parrafo in range(len(parrafos)):
    parrafos_en_mayusculas.append(parrafos[parrafo].get_text().upper())
    indice = parrafos_en_mayusculas[parrafo].find(palabra.upper())

    if indice != -1:
        contador = contador + 1

print("La palabra: ", palabra, " se ha repetido: ", contador, " veces")
