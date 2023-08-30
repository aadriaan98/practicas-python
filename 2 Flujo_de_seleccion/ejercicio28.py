"""
Crear un programa que pida un número de mes (ejemplo 4) y escriba el nombre del mes en letras ("abril"). Verificar que el mes sea válido e informar en caso que no lo sea.

"""

numero_mes = int(input("Ingrese el numero de mes: "))


cadena = "El mes ingresado es "

if numero_mes < 1 or numero_mes > 12:
    print("mes no valido")
else:
    meses = ["enero", "febrero", "marzo", "abril", "mayo", "junio","julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
    numero_usuario = meses[numero_mes - 1]
    print(f"{cadena} {numero_usuario}")
