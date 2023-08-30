"""
Escribir un programa que permita ingresar el valor monetario de una hora de trabajo y la cantidad de horas trabajadas por día, para calcular el salario semanal de un trabajador que trabaja todos los días hábiles y la mitad de las horas del día hábil los sábados, suponiendo que todas las horas tienen el mismo valor."

Como pensarlo:

Pedir al usuario que ingrese el valor monetario de una hora de trabajo y almacenarlo en una variable valor_hora.

Pedir al usuario que ingrese la cantidad de horas trabajadas por día por el trabajador y almacenarla en una variable horas_trabajadas_por_dia.

Calcular el salario diario del trabajador multiplicando valor_hora por horas_trabajadas_por_dia.

Calcular el salario semanal del trabajador multiplicando el salario diario por la cantidad de días hábiles de la semana. Para esto, puedes utilizar la constante dias_habiles definida como 5.

Calcular la cantidad de horas trabajadas por el trabajador el sábado, que es la mitad de la cantidad de horas trabajadas por día hábil. Para esto, se puede utilizar la vaiable horas_sabado definida como horas_trabajadas_por_dia / 2.

Calcular el salario del trabajador por las horas trabajadas el sábado multiplicando valor_hora por horas_sabado.

Sumar el salario semanal con el salario del sábado para obtener el salario total semanal del trabajador.

Mostrar el resultado del salario semanal en la pantalla.
"""

valor_hora = float(input("Ingrese el valor de 1hs trabajada: "))
h_t_por_dia = int(input("Ingrese las horas trabajadas: "))
salario_diario = valor_hora * h_t_por_dia
dias_habiles = 5
salario_semanal = salario_diario * dias_habiles
horas_sabado = h_t_por_dia / 2
salario_sabado = horas_sabado * valor_hora
total_semanal = salario_semanal + salario_sabado

cadena = f"""
Valor de 1h de trabajo: {valor_hora}
Horas trabajadas por dia: {h_t_por_dia}
Salario diario: {salario_diario}
Salario semanal: {salario_semanal}
Horas trabajadas el dia sabado: {horas_sabado}
Salario del dia sabado: {salario_sabado}
Salario total semanal: {total_semanal}
"""

print(cadena)



