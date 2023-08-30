"""
Escribir un programa que lea números enteros hasta que se ingrese un 0, y muestre el máximo.

"""
num = int(input("Ingrese un numero: "))
maximo = num

while num != 0:
    num = int(input("Ingrese un numero: "))
    if num > maximo:
        maximo = num

print("El numero maximo es: ", maximo)