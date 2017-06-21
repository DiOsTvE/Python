# -*- coding: utf-8 *-*
"""
Crear la clase Producto, tiene los siguientes atributos:
nombre del producto, precio, iva aplicable, cantidades del
producto en stock. La clase debe contar con el metodo init
dentro del cual se solicitara los datos anteriormente mencionados.
Crear los siguientes metodos:
1 - Metodo para mostrar todos los datos del producto.
2 - Calcular el precio del producto con el iva incluido.
3 - Calcular cuanta inversion del producto existe.
4 - Permita modificar el tipo de iva de un producto.
5 - Metodo que reste stock cuando se vaya vendiendo productos.
Creamos cuatro productos.
"""
class Producto:
    def __init__(self):
        self.nombre = input("Introduce nombre del producto: ")
        self.precio = float(input("Introduce el precio del producto: "))
        self.iva = int(input("Introduce el iva del producto: "))
        self.stock = int(input("Introduce la cantidad de stock: "))
    def mostrar(self):
        print("El nombre del producto es: ",self.nombre)
        print("El precio del producto es: ",self.precio)
        print("El iva del producto es: ",self.iva)
        print("La cantidad de stock del producto es: ",self.stock)
    def precioTotal(self):
        total = self.precio * (1+(self.iva/100))
        return total
    def inversion(self):
        total_inversion = self.stock * (self.precio * (1+(self.iva/100)))
        return total_inversion
    def modificaIva(self):
        modIVA = int(input("Introduce el nuevo iva: "))
        self.iva = modIVA
    def disminuyeStock(self):
        ventas = int(input("Cuantas unidades se ha vendido: "))
        self.stock = self.stock - ventas
salir = 'n'
almacen = []

while salir == 'n':
    almacen.append(Producto())
    salir = input("Desea salir de la aplicacion (s/n)?: ").lower()

for producto in almacen:
    producto.mostrar()
    print("El precio con iva es: ",producto.precioTotal())
    print("La inversion en el almacen del producto es: ",producto.inversion())
    producto.modificaIva()
    producto.mostrar()
    print("El precio con iva es: ",producto.precioTotal())
    producto.disminuyeStock()
    producto.mostrar()
    print("La inversion en el almacen del producto es: ",producto.inversion())