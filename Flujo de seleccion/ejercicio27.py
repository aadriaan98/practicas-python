"""
Escribir un programa que permita ingresar una edad (entre 1 y 120 años)

un género ('F'para mujeres, 'M' para hombres) y un nombre. 

En caso de haber ingresado valores erróneos (edad fuera de rango o género inválido) informar tal situación indicando el nombre de la persona. 

Si los datos están bien ingresados el programa debe indicar, sabiendo que las mujeres se jubilan con 60 años o más y los hombres con 65 años o más, si la persona está en edad de jubilarse.

"""

nombre = input("Ingrese el nombre: ")
edad = int(input("Ingrese la edad: "))
rango_edad = edad >= 1 and edad <= 120
edad_correcta = rango_edad

sexo = input("Ingrese sexo: ")
rango_sexo = sexo == "M" or sexo == "F"
sexo_ok = rango_sexo

jubilacion_m = edad >= 65
jubilacion_f = edad >= 60

if not edad_correcta:
    print("La edad debe estar entre 1 a 120 años")
    
if not sexo_ok:
    print("Sexo incorrecto, los valores deben indicarse como M o F")

if sexo == "M":
    if jubilacion_m:
        print("Esta en edad de jubilacion")
    else:
        print("No estas en edad de jubilarte")
        
if sexo == "F":
    if jubilacion_f:
        print("Esta en edad de jubilacion")
    else:
        print("No estas en edad de jubilarte")
        
