"""
Escribir un programa que lea números enteros hasta que la suma de éstos sea mayor que 100, y muestre la cantidad de números ingresados.

"""

suma = 0
contador = 0

"""
while suma < 100:
    num = int(input("Ingrese un numero: "))
    suma += num
    contador += 1
    
print("La cantidad de numeros ingresados es de: ", contador)

"""


for n in range(1, 101):
    num = int(input("Ingrese un numero: "))
    suma += num
    contador += 1
    if suma > 100:
        break

print("La cantidad de números ingresados es:", contador)

