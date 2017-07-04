import urllib.request
from bs4 import BeautifulSoup
import re

ofertas = urllib.request.urlopen("https://www.dia.es/compra-online/ofertas-DIA-online/?q=%3Arelevance&page=0&disp=")
pagina = ofertas.read()

html = BeautifulSoup(pagina, "html.parser")#lxml ó lxml-xml ó xml ó html5lib
productos = html.find_all('div',{'class':'span-3'})
#caract_producto = html.find_all('a',{'class':'productMainLink'})

caract_producto = html.find_all('span',{'class':'details'})

for i in caract_producto:
    print(i.text)

caract_producto = html.find_all('a',{'class':'productMainLink'},href=re.compile("compra"))
for i in caract_producto:
    print(i.get('href'))