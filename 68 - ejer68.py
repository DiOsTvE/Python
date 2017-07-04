import urllib.request
from bs4 import BeautifulSoup

abrir_pagina = urllib.request.urlopen("https://www.dia.es/compra-online/ofertas-DIA-online/")
pagina = abrir_pagina.read()

soup = BeautifulSoup(pagina, "html.parser")#lxml ó lxml-xml ó xml ó html5lib
"""
print(soup.title.text)  # Leer el titulo de la pagina
print(soup.title.string)  # Leer el titulo de la pagina

print(soup.title.parent.name)
print(soup.div)

parrafos = soup.find_all("p")

for i in parrafos:
    print(i)
"""
entradas = soup.find_all('p',{'class':'price'})

for i in entradas:
    print(i.get_text())