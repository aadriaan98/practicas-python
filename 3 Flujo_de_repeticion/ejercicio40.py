"""
Escribir un programa que permita ingresar dos numeros enteros a y b. El programa debe mostrar:

La suma de los numeros pares entre a y b.
El producto de los numeros impares entre a y b.

"""

num1 = int(input("Ingrese el 1° numero: "))
num2 = int(input("Ingrese el 2° numero: "))

pares = 0
impar = 1

for n in range(num1, num2 + 1):
    if n % 2 == 0:
        pares+=n
    elif n % 2 != 0:
        impar *= n
        
print("La suma de los números pares entre", num1, "y", num2, "es:", pares)
print("El producto de los números impares entre", num1, "y", num2, "es:", impar)

