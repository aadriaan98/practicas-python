"""
Escribir un programa que solicite al usuario ingresar tres notas de un alumno. El programa debe mostrar por pantalla las notas separadas por comas en un renglón y el promedio de las notas en el siguiente renglon.

Ejemplo de ejecución:

    Ingrese la nota 1: 7
    Ingrese la nota 2: 8
    Ingrese la nota 3: 9
    Notas: 7, 8, 9
    Promedio: 8.0
"""

nota1 = int(input("Ingrese la 1° nota: "))
nota2 = int(input("Ingrese la 2° nota: "))
nota3 = int(input("Ingrese la 3° nota: "))

promedio = nota1 + nota2 + nota3

cadena = f"""
Nota 1: {nota1}
Nota 2: {nota2}
Nota 3: {nota3}
Promedio: {promedio}
"""
print(cadena)
