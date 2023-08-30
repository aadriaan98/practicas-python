"""
Escribir un programa que permita ingresar tres números enteros e indicar cual es el mayor.

"""
num1 = int(input("Ingrese el 1° numero: "))
num2 = int(input("Ingrese el 2° numero: "))
num3 = int(input("Ingrese el 3° numero: "))

lista = [num1, num2, num3]

mayor = num1

if num2 > mayor:
    mayor = num2
    
if num3 > mayor:
    mayor = num3

print(mayor)        

print(max(lista))
