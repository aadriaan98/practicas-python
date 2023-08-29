"""
Una remisería requiere un sistema que calcule el precio de un viaje a partir de la cantidad de km que desea recorrer el usuario.

Tiene la siguiente tarifa:

Viaje mínimo $50
Si recorre entre 0 y 10km: $20/km
Si recorre 10km o más: $15/km
Escribir un programa que permita ingresar la cantidad de km que desea recorrer el usuario y muestre el precio del viaje.

"""

cantidad_km = float(input("Ingrese la cantidad de km: "))
viaje_minimo = 50
tarifa1 = (cantidad_km * 20) + 50
tarifa2 = (cantidad_km * 15) + 50

if cantidad_km > 0 and cantidad_km < 10:
    print(f"""El Viaje cuesta {tarifa1}""")
elif cantidad_km >= 10:
    print(f"""El viaje cuesta {tarifa2}""")    