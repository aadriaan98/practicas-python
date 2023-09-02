"""
Ejercicio 046
Escribir un programa que a partir de un número entero cant ingresado por el usuario permita cargar por teclado cant números enteros. La computadora debe mostrar cuál fue el mayor número y en qué posición apareció.

numero random ==> 0.0  ....  0.9999999999999 

range(10) ==> [0,1,2,3,4,5,6,7,8,9]
posicion  ==>  0 1 2 3 4 5 6 7 8 9  ==> len() = 10 
"""

from random import randint 

posicion = 0
maximo = -float('inf')
cant = randint(1,10)
for x in range(cant):
    numero = randint(-1000,1000)
    print(f"Numero: {numero} posicion {x+1}")
    if numero > maximo:
        posicion = x+1
        maximo = numero
print(f"cantidad de numeros: {cant}")
print(f"Maximo: {maximo} posicion: {posicion}")


