"""
Escribir un programa que permita leer dos números naturales A y B. Calcular A elevado a la B mediante productos sucesivos y mostrar el resultado.

Ejemplo:

4^3 = 4 * 4 * 4 (4 multiplicado 3 veces).
3^4 = 3 * 3 * 3 * 3 (3 multiplicado 4 veces).

"""

num1 = int(input("Ingrese el 1° numero: "))
num2 = int(input("Ingrese el 2° numero: ")) 

elevado = 0
potencia = 1

#AMBOS CASOS FUNCIONAN

#MI SOLUCION
while num1 and num2 > 0:
    elevado = num1 ** num2
    break

#chatGPT
"""
for _ in range(num2):
    potencia *= num1

print("El numero ",num1,"^", num2, "es =", potencia)

"""


print("El numero ",num1,"^", num2, "es =", elevado)