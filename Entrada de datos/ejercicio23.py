"""
Escribir un programa que permita ingresar tres números enteros y mostrar el mayor el menor y el valor que esta en medio.

Ejemplo: Si se ingresan los números 5, 3 y 7, el programa debe mostrar el número 5 como el menor, el número 7 como el mayor y el número 3 como el que esta en medio.

Otra vez se mezclaron las instrucciones, ¿podrías arreglarlas?

"""
numero_uno = int(input("Ingrese el primer número: "))
numero_dos = int(input("Ingrese el segundo número: "))
numero_tres = int(input("Ingrese el tercer número: "))

mayor = numero_uno
medio = numero_dos
menor = numero_tres

if numero_dos > mayor:
    mayor = numero_dos
    medio = numero_uno
    menor = numero_tres

if numero_tres > mayor:
    mayor = numero_tres
    medio = numero_uno
    menor = numero_dos
    
if menor > medio:
    menor, medio = medio, menor
    
print("El mayor es: ", mayor)
print("El medio es: ", medio)
print("El menor es: ", menor)
