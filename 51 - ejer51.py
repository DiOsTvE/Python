# -*- coding: utf-8 *-*
"""
Crear dos clases, una clase se denomina Cliente, los atributos van a ser:
nombre, apellidos, saldo. Metodos: el metodo init, el metodo ingresar, el
metodo extraer, el metodo ver saldo, el metodo ver datos, con las siguientes
caracteristicas.
- En el metodo init: solicitamos el nombre y los apellidos, el saldo lo
inicializamos a 0.
- En el metodo ingresar: pedimos el importe a ingresar y se añadimos al
saldo.
- En el metodo extraer: cuanto dinero quiero extraer y restarselo al saldo.
Verificar que hay saldo suficiente.
- En el metodo ver saldo: mostrar el saldo que tiene el cliente.
- En el metodo ver datos: mostrar todos los datos del cliente.
La siguiente clase se denomina Banco, los atributos van a ser:
tres clientes. En el metodo init genera los tres clientes. Los metodos son:
- Operar: hacer deposito o extraer deposito.
- Saldo total del banco: sumar todos los saldos y mostrarlo.
"""
class Cliente:
    def __init__(self):
        self.nombre = input("Introduce nombre: ")
        self.apellidos = input("Introduce apellidos: ")
        self.saldo = 0
    def ingresar(self):
        dinero = float(input("Cuanto dinero quiere ingresar: "))
        self.saldo = self.saldo + dinero
        return  self.saldo
    def extraer(self):
        dinero = float(input("Cuanto dinero quiere extraer: "))
        if dinero > self.saldo:
            return "No hay suficiente saldo."
        else:
            self.saldo = self.saldo - dinero
            return self.saldo
    def mostrarSaldo(self):
        print("El cliente tiene el siguiente saldo: ", self.saldo)
    def mostrarDatos(self):
        print("Los datos del siguiente cliente son: ")
        print("Nombre: ", self.nombre)
        print("Apellidos: ", self.apellidos)
        print("Saldo: ", self.saldo)
class Banco:
    def __init__(self):
        self.cliente1 = Cliente()
        self.cliente2 = Cliente()
        self.cliente3 = Cliente()
        self.saldoTotales = 0
    def operacion(self):
        self.cliente1.ingresar()
        self.cliente2.ingresar()
        self.cliente3.ingresar()
        self.cliente1.extraer()
    def totalBanco(self):
        self.saldoTotales = self.saldoTotales + self.cliente1.saldo
        self.saldoTotales = self.saldoTotales + self.cliente2.saldo
        self.saldoTotales = self.saldoTotales + self.cliente3.saldo
        print("El saldo total en el banco asciende a: ", self.saldoTotales)

nuevo_cliente_1 = Cliente()
nuevo_cliente_1.ingresar()
print("Saldo: ", nuevo_cliente_1.extraer())
nuevo_cliente_1.mostrarSaldo()
nuevo_cliente_1.mostrarDatos()

clientes_Banco_1 = Banco()
clientes_Banco_1.operacion()
clientes_Banco_1.totalBanco()