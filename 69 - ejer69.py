import urllib.request
from bs4 import BeautifulSoup
import os
import time

while True:
    abrir_pagina = urllib.request.urlopen("http://www.aemet.es/xml/municipios/localidad_45163.xml")
    pagina = abrir_pagina.read()

    soup = BeautifulSoup(pagina, "lxml")#lxml ó lxml-xml ó xml ó html5lib

    dia = soup.find_all('dia',{'fecha':'2017-07-04'})

    for temperaturas in dia:
        maxima = temperaturas.find('maxima')
        print(maxima)

        minima = temperaturas.find('minima')
        print(minima)

    time.sleep(10)