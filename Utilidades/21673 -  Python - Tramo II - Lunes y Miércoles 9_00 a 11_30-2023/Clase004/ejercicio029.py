"""
Ejercicio 029
Escribir un programa que permita Ingresar las notas de los dos parciales de 
un alumno e indicar si promocionó, aprobó o debe recuperar. 
Si el valor de la nota no esta entre 0 y 10, debe informar un error.
Se promociona cuando las notas de ambos parciales son mayores o iguales a 7.
Se aprueba cuando las notas de ambos parciales son mayores o iguales a 4.
Se debe recuperar cuando al menos una de las dos notas es menor a 4.
"""

nota1 = 11
nota2 = 3

datos_ok = nota1 >=0 and nota1 <= 10 and nota2 >= 0 and nota2 <= 10

if datos_ok:
    # nota1 < 4 or nota2 < 4 <==> nota1 >= 4 and nota2 >= 4
    aprueba = nota1 >= 4 and nota2 >= 4
    promociona = nota1 >= 7 and nota2 >= 7
    # recupera = not aprueba 
    if aprueba:
        cartel = "Aprueba"
        if promociona:
            cartel += " con promoción"
    else:
        cartel = "Recupera" 

    print(f"[{nota1},{nota2}] ==> {cartel}")
else:
    print("Error de datos")
