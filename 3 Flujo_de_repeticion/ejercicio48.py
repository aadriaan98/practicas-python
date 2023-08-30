"""
Escribir un programa que permita realizar varias operaciones matemáticas ingresando un caracter por cada una la operación a realizar (‘+’, ‘-’, ‘*’, ‘/’, ‘F’) 

y dos números enteros en el caso que no haya elegido ‘F’. 

La computadora debe mostrar el resultado para la operación ingresada. 

Considerar que no se puede dividir por cero. 

Cuando la operación ingresada sea ‘F’ nos indicará que no se desean calcular más operaciones.

"""

while True:
    operacion = input("Que operacion desea realizar? ")
    if operacion == "F" or operacion == "f":
        break
    
    num1 = int(input("Ingrese el 1° numero: "))
    num2 = int(input("Ingrese el 2° numero: "))
    
    if operacion == "+":
        resultado= num1 + num2
        print("El resultado es:", resultado)
    elif operacion == "-":
        resultado= num1 - num2
        print("El resultado es:", resultado)
    elif operacion == "*" or operacion == "x":
        resultado= num1 * num2
        print("El resultado es:", resultado)
    elif operacion == "/":
        if num2 != 0:
            resultado = num1 / num2
            print("El resultado es:", resultado)
        else:
            print("No se puede dividir por 0")
    else:
        print("Operacion no valida.")




    

