"""
Escribir un programa que permita leer dos números A y B (enteros positivos). Calcular el producto A * B por sumas sucesivas e imprimir el resultado.

Ejemplo:

4*3 = 4 + 4 + 4 (4 sumado 3 veces).
3*4 = 3 + 3 + 3 + 3 (3 sumado 4 veces).

"""

num1 = int(input("Ingrese el 1° numero: "))
num2 = int(input("Ingrese el 2° numero: ")) 

producto = 0

#AMBOS CASOS FUNCIONAN

#MI SOLUCION
while num1 and num2 > 0:
    producto = num1 * num2
    break

#CHATGPT
"""for n in range(num2):
    producto+= num1"""

print("El producto de ",num1,"X", num2, "es =", producto)