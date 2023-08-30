"""
Escribir un programa que permita ingresar dos números enteros y la operación a realizar('+', '-', '*', '/'). Debe mostrarse el resultado para la operación ingresada. Considerar que no se puede dividir por cero (en ese caso mostrar el texto 'ERROR').

"""

num1 = int(input("Ingrese el 1° numero: "))
num2 = int(input("Ingrese el 2° numero: "))
operacion = input("Ingrese la operacion logica: ")

if operacion == "+":
    resultado = num1 + num2
    print(resultado)
elif operacion == "-":
    resultado = num1 - num2
    print(resultado)
elif operacion == "*" or operacion == "x":
    resultado = num1 * num2
    print(resultado)
elif operacion == "/":
    if num1 <= 0 or num2 <= 0:
        print("No se puede dividir por 0")
    else:
        resultado = num1 / num2
        print(resultado)