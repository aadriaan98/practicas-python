"""
Escribir un programa que permita al usuario ingresar dos números enteros. La computadora debe indicar si el mayor es divisible por el menor.

(Un número entero a es divisible por un número entero b cuando el resto de la división entre a y b es 0)

"""

num1 = int(input("Ingrese el 1° numero: "))
num2 = int(input("Ingrese el 2° numero: "))

numeros = [num1, num2]
maximo = max(numeros)
minimo = min(numeros)

es_divisible = (maximo % minimo) == 0
resultado = (maximo / minimo)

if es_divisible:
    print (f"""Son divisibles, el resultado es {resultado}""")
else:
    print("No son divisibles")



