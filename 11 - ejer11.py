"""
Nos van a ingresar 10 compras, saber cuantas han superado los 1000 euros
"""
acum = 0
for i in range(10):
    compra = float(input(f"Introduce compra {i+1}: "))
    if compra>1000:
        acum = acum + 1
print("Las compras que han superado los 1000 euros son: ")
print(acum)
