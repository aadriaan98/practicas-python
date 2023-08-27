"""
Definición del problema: Una inmobiliaria paga a sus vendedores un salario base, más una comisión fija por cada venta realizada, más el 5% del valor de esas ventas. Realizar un programa que imprima el nombre del vendedor y el salario que le corresponde en un determinado mes.

Se leen por teclado el nombre del vendedor, la cantidad de ventas que realizó y el valor total de las mismas.

¿Sobran datos? ¿Qué datos sobran?

"""
nombre_vendedor = input("Ingrese el nombre del vendedor: ")
salario_base = float(input("Ingrese el salario base: "))

cantidad_ventas = int(input("Ingrese la cantidad de ventas en el mes: "))
comision_fija = float(input("Ingrese comision fija por ventas: "))
comision = cantidad_ventas * comision_fija

premio = float(input("Ingrese el valor de las ventas: "))
valor_ventas = premio * 0.5

salario_total = salario_base + comision + valor_ventas


cadena = f"""
Nombre del vendedor: {nombre_vendedor}
--------------------------------------
Salario basico: {salario_base} U$D
--------------------------------------
Cantidad de ventas: {cantidad_ventas}
--------------------------------------
Comision por ventas: {comision} U$D
--------------------------------------
Premios: {valor_ventas} U$D
--------------------------------------
Salario Total: {salario_total} U$D
"""

print(cadena)