"""
Escribir un programa que permita validar la nota de un examen. Se espera que la nota que el usuario ingrese sea un número comprendido entre 0 y 10.

La misma debe ser ingresada tantas veces como sea necesario hasta que quede comprendida dentro del rango indicado.

"""

# MI SOLUCION
for n in range(1, 11):
    nota = int(input("Ingresa una nota: "))
    if nota >= 0 and nota <= 10:
        break
    else:
        print("Nota no valida, volve a ingresarla")

print("Nota:", nota)

# chatGPT

"""
nota_alumno = int(input("Ingrese la nota: "))

while nota_alumno < 0 or nota_alumno > 10:
    print("Nota no valida, volve a ingresarla")
    nota_alumno = int(input("Ingrese la nota"))

print("Nota:", nota_alumno)

"""