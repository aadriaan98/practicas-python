"""
Escribir un programa que permita validar la nota de un examen. 

Se espera que la nota que el usuario ingrese sea un número comprendido entre 0 y 10.

La misma debe ser ingresada tantas veces como sea necesario hasta que quede comprendida dentro del rango indicado.

Las notas 1 y 3 no usan nunca.

La nota 0 se reserva para los ausentes.

Las notas válidas pueden ser un 2 o un valor entre 4 y 10.

"""
for n in range(0, 11):
    nota= int(input("Ingrese una nota: "))
    if nota == 0:
        print("El alumno tiene ausente.")
        break
    elif nota == 2:
        print("El alumno tiene 2")
        break
    elif nota == 1 or nota == 3:
        print("Nota invalida, ingrese nuevamente")
    elif nota >= 4 and nota <= 10:
        print("La nota es:", nota) 
        break
    else: 
        print("Las notas no pueden inferiores a 0 o mayores que 10")