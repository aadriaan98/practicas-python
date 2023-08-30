"""
Escribir un programa que lea números enteros hasta que se ingrese un 0, y muestre el promedio de los números ingresados.

""" 
contador = 0
suma = 0

while True:
    num = int(input("Ingrese un numero: "))
    if num == 0:
        break
    else:
        suma += num
        contador += 1
    
if contador > 0:
    promedio = suma / contador
    print("El promedio de los numeros ingresados es: ", promedio)
else:
    print("No se ingresaron numeros")