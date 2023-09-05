"""
Escribir un programa que permita al usuario ingresar números hasta que se introduzca un 0.

La computadora debe mostrar el número máximo y el número mínimo.

"""

numeros = []

while True:
    n = int(input("Ingrese un numero: "))
    if n != 0:
        numeros.append(n)
    else:
        break

if len(numeros) > 0:
    maximo = max(numeros)
    minimo = min(numeros)
    print(f"El numero maximo es, {maximo}, y el numero minimo es: {minimo}")
else:
    print("No se ingresaron numeros")