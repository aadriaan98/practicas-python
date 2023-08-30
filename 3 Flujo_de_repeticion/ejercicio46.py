"""
Escribir un programa que a partir de un número entero cant ingresado por el usuario permita cargar por teclado cant números enteros. La computadora debe mostrar cuál fue el mayor número y en qué posición apareció.

"""

cantidad_num = int(input("Ingrese la cantidad de numeros que va a ingresar: "))
numeros = []


for n in range(cantidad_num):
    num = int(input("Ingrese un numero entero: "))
    numeros.append(num)
 
posicion = 0
mayor_numero = numeros[0]
    
for n in range(1, cantidad_num):
    if numeros[n] > mayor_numero:
        mayor_numero = numeros[n]
        posicion = n+1

print("El mayor numero es: ", mayor_numero, " y esta en la posicion: ", posicion)