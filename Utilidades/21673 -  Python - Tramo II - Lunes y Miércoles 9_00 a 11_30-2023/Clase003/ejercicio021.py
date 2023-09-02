"""
Ejercicio 021
Escribir un programa que permita ingresar dos números enteros e indicar si el primero es mayor, 
menor o igual al segundo.
"""

num1 = 10
num2 = 21

if num1 > num2:
    print(f"{num1} > {num2}")
else:
    if num1 < num2:
        print(f"{num1} < {num2}")
    else:
        print(f"{num1} == {num2}")
