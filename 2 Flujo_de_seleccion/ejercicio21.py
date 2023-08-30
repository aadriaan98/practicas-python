"""
Escribir un programa que permita ingresar dos números enteros e indicar si el primero es mayor, menor o igual al segundo.

"""

num1 = int(input("Ingrese el 1° numero. "))
num2 = int(input("Ingrese el 2° numero. "))

if num1 == num2:
    print("Los numero son iguales")
elif num1 > num2:
    print("Numero 1 es mayor que numero 2")
else:
    print("Numero 2 es mayor que numero 1")
    