"""
import webbrowser
webbrowser.open_new_tab("http://www.elmundo.es")
webbrowser.open_new("http://www.elpais.es")
webbrowser.open_new("http://www.elmundo.es")
webbrowser.open_new_tab("http://www.noticias3d.com")
"""
import urllib.request

x = urllib.request.urlopen('https://www.google.com/')
contenido = x.read()
print(contenido)
