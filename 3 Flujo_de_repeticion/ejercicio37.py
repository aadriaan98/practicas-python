"""
Escribir un programa que muestre todos los números enteros del 1 al 5, y luego los mismos números pero en orden inverso.

"""

cantidad = 5

# Del 1 al 5

for n in range(1, cantidad + 1):
    print(n)

print("-----------------")

# Del 5 al 1

for n in range(cantidad, 0, -1):
    print(n)
