import urllib.request
from bs4 import  BeautifulSoup

pagina = urllib.request.urlopen("https://www.dia.es/compra-online/ofertas-DIA-online/")
soup = BeautifulSoup(pagina,"html.parser")#lxml ó lxml-xml ó xml ó html5lib
#for i in soup.find_all("p"):
    #print(i)
archi = open("c:/python/productos.csv","w")
productos = soup.find_all("span",{"class":"details"})
for i in productos:
    archi.write(i.get_text())
archi.close()