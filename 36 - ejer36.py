"""
En el programa principal se solicita un numero, al numero en una funcion
lo elevamos al cuadrado, en otra funcion al numero elevado al cuadrado se
le suma 10
"""
def doblar(n1):
    rdo = n1 * n1
    return rdo
def sumar_10(dobla):
    rdo = dobla + 10
    print(rdo)

numero = int(input("Ingrese un numero: "))
doblado = doblar(numero)
sumar_10(doblado)
