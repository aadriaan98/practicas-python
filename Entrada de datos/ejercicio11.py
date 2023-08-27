"""
Escribir un programa que permita resolver el siguiente problema:

Tres personas aportan diferente capital a una sociedad y desean saber el valor total aportado y qué porcentaje aportó cada una (indicando nombre y porcentaje).

Solicitar la carga por teclado del nombre de cada socio y su capital aportado, a partir de esto calcular e informar lo requerido previamente.

"""

p1 = input("Ingrese el nombre del 1° inversor: ")
aportep1 = float(input(p1 + ", aporta a la sociedad la suma de: "))

p2 = input("Ingrese el nombre del 2° inversor: ")
aportep2 = float(input(p2 + ", aporta a la sociedad la suma de: "))

p3 = input("Ingrese el nombre del 3° inversor: ")
aportep3 = float(input(p3 + ", aporta a la sociedad la suma de: "))

inversion_total = aportep1 + aportep2 + aportep3

porcentaje_p1 = round((aportep1 / inversion_total) * 100)
porcentaje_p2 = round((aportep2 / inversion_total) * 100)
porcentaje_p3 = round((aportep3 / inversion_total) * 100)


cadena = f"""
{p1} aporta: {aportep1} U$D
---------------------------
{p2} aporta: {aportep2} U$D
---------------------------
{p3} aporta: {aportep3} U$D
---------------------------
El capital total es de {inversion_total} U$D
--------------------------------------------
El porcentaje aportado por {p1} es de {porcentaje_p1}%
------------------------------------------------------
El porcentaje aportado por {p2} es de {porcentaje_p2}%
------------------------------------------------------
El porcentaje aportado por {p3} es de {porcentaje_p3}%
"""

print(cadena)