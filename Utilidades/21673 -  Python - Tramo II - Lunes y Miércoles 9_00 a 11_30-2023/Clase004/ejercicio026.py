"""
Ejercicio 026
Escribir un programa que permita ingresar la cantidad de invitados 
a una fiesta y la cantidad de asientos disponibles en el salon. 
Debes indicar si alcanzan los asientos, 
Si los asientos no alcanzaran indicar cuántos faltan para que 
todos los invitados puedan sentarse.
"""



cantidad_invitados = int(input("ingrese la cantidad de invitados: "))
cantidad_asientos = int(input("ingrese la cantidad de asientos: "))

faltan = cantidad_invitados - cantidad_asientos
sobran = cantidad_asientos - cantidad_invitados
 
if cantidad_asientos < cantidad_invitados:
    print(f"Faltan {faltan} asientos")
elif cantidad_asientos > cantidad_invitados:
    print(f"Sobran {sobran} asientos")
else:
    print("Alcanzaron los asientos")

