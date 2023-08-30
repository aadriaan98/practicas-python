"""
Escribir un programa que permita al usuario ingresar un período de tiempo en segundos. Luego, el programa debe convertir ese período de tiempo a una forma más legible y comprensible para el usuario, expresando el resultado en días, horas, minutos y segundos. El resultado se mostrará en pantalla en un mensaje que indique la cantidad de segundos ingresados y su equivalente en días, horas, minutos y segundos.

Ejemplo: 200000 segundos equivalen a 2 días, 7 horas, 33 minutos y 20 segundos. Usar en el programa las siguientes instrucciones:
"""

segundos = float(input("Ingrese una cantidad de segundos: "))

dias = round(segundos / 86400)

horas = round((segundos % 86400) / 3600 )
 
minutos = round((segundos % 3600) / 60 )

s_restantes = round((segundos) / 60)

cadena = f"""
{dias} dias {horas} horas {minutos} minutos {s_restantes} segundos
"""
print(cadena)