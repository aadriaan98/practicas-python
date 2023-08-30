"""
Escribir un programa que permita validar una opción ingresada.

Se le preguntará al usuario si desea continuar con alguna operación de la forma "¿Deseás continuar? [S/N]". Se espera que el usuario ingrese una 'S' o una 'N' (incluir las minúsculas). 

La opción debe ser ingresada tanto como sea necesario hasta que quede comprendida dentro de las posibilidades esperadas.

"""

while True:
    cadena = input("¿Deseás continuar? [S/N]: ")
    if cadena == "s" or cadena == "S":
        print("Seleccionó, Si")
        break
    elif cadena == "n" or cadena == "N":
        print("Selecciono, No")
        break
    else: 
        print("No se selecciono una opcion valida")
