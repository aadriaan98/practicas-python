"""
Escribir un programa para resolver el siguiente problema:

Tres personas invierten dinero para fundar una empresa (no necesariamente en partes iguales). Calcular qué porcentaje invirtió cada una.

Como pensarlo:

Solicitar al usuario que ingrese las cantidades invertidas por cada persona en tres variables numéricas.

Calcular el total de la inversión sumando las cantidades de las tres personas.

Calcular el porcentaje que representa la inversión de cada persona en relación al total de la inversión.

Dividir la cantidad invertida por cada persona entre el total de la inversión y multiplicar por 100 para obtener el porcentaje. Almacenar el resultado en una variable correspondiente a cada persona. Opcionalmente, se puede redondear el resultado a un número determinado de decimales utilizando la función round().

Mostrar por pantalla el porcentaje de inversión de cada persona.

"""

p1 = float(input("Ingrese la inversion de la persona 1: "))
p2 = float(input("Ingrese la inversion de la persona 2: "))
p3 = float(input("Ingrese la inversion de la persona 3: "))

total_inversion = p1 + p2 + p3

pcj_persona1 = round((p1 / total_inversion)* 100)
pcj_persona2 = round((p2 / total_inversion)* 100)
pcj_persona3 = round((p3 / total_inversion)* 100)

cadena = f"""
Inversion de la persona 1: {p1}
Inversion de la persona 2: {p2}
Inversion de la persona 3: {p3}
Total de inversion: {total_inversion}
Porcentaje de inversion de la persona 1: {pcj_persona1}%
Porcentaje de inversion de la persona 2: {pcj_persona2}%
Porcentaje de inversion de la persona 3: {pcj_persona3}%
"""


print(cadena)