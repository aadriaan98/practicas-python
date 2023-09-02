"""
Ejercicio 040
Escribir un programa que permita ingresar dos numeros enteros a y b. 
con a <= b.
El programa debe mostrar:

La suma de los numeros pares entre a y b.
El producto de los numeros impares entre a y b.

"""

a = int(input("Ingrese a:"))
b = int(input("Ingrese b:"))
while a > b: # mientras error
    print(f"Error: {a} <= {b} ")
    b = int(input("Ingrese b:"))

producto_impares = 1
suma_pares = 0
for numero in range(a,b+1):
    if numero%2 == 0: 
        suma_pares += numero
    else:
        producto_impares *= numero

print(f"Prod. impares: {producto_impares}")
print(f"Suma pares: {suma_pares}")

