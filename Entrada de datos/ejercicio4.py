"""
Escribir un programa que solicite al usuario ingresar tres numeros enteros.El programa debe mostrar por pantalla el resultado de sumar los tres numeros de la siguiente manera: "[numero1] + [numero2] + [numero3] = [suma]".

Ejemplo: Si el usuario ingresa 1, 2 y 3, el programa debe mostrar por pantalla: "1 + 2 + 3 = 6".
"""

numero1 = int(input("ingrese el primer valor: "))
numero2 = int(input("ingrese el segundo valor: "))
numero3 = int(input("ingrese el tercer valor: "))

suma = numero1 + numero2 + numero3

print(f"{numero1} + {numero2} + {numero3} = {suma}")

