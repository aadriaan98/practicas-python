"""
Escribir un programa que permita Ingresar las notas de los dos parciales de un alumno e indicar si promocionó, aprobó o debe recuperar. Si el valor de la nota no esta entre 0 y 10, debe informar un error.

Se promociona cuando las notas de ambos parciales son mayores o iguales a 7.
Se aprueba cuando las notas de ambos parciales son mayores o iguales a 4.
Se debe recuperar cuando al menos una de las dos notas es menor a 4.

"""
nota1 = int(input("Ingrese la nota del 1° parcial: "))
nota2 = int(input("Ingrese la nota del 2° parcial: "))
notas_ok = nota1 >= 0 and nota1 <=10 and nota2 >= 0 and nota2 <= 10
aprueba = nota1 >= 4 and nota2 >= 4
promociona = nota1 >= 7 and nota2 >= 7
recupera = nota1 < 4 or nota2 < 4

print(F"""
      1° parcial: {nota1}
      2° parcial: {nota2}
""")

if not notas_ok:
    print("Notas incorrectas, los valores deben ser mayores que 0 y menores o iguales que 10")
elif aprueba:
    print("Aprueba")
elif promociona:
    print("Aprueba con promocion")
else:
    print("recupera")        