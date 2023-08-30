"""
Escribir un programa que permita ingresar la cantidad de invitados a una fiesta y la cantidad de asientos disponibles en el salon. Debes indicar si alcanzan los asientos, Si los asientos no alcanzaran indicar cuántos faltan para que todos los invitados puedan sentarse.

"""

invitados = int(input("Ingrese la cantidad de invitados: "))
asientos = int(input("Ingrese la cantidad de asientos: "))
resto_asientos = (asientos - invitados)
resto_invitados = (invitados - asientos) 

alcanzan = (invitados == asientos)
sobran_asientos = (asientos > invitados)
faltan_asientos = (invitados > asientos)


if sobran_asientos:
    print(f"Sobran {resto_asientos} asientos")
elif faltan_asientos:
    print(f"Faltan {resto_invitados} asientos")
else:
    print("La cantidad alcanza")