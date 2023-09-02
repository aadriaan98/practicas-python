"""
Realizá un programa que permita ingresar el monto total de las ventas realizadas por un
vendedor durante el mes, de quien se sabe que gana un sueldo fijo de 44000 pesos más el 16
por ciento del monto total vendido. Con tales datos debes calcular y mostrar el importe a
cobrar por el vendedor.
"""

SUELDO_FIJO = 44000
PORCENTAJE_COMISION = 0.16

total_ventas = float(input("Ingrese el total ventas del mes del vendedor: "))

comision_ventas = total_ventas * PORCENTAJE_COMISION

sueldo_a_cobrar = SUELDO_FIJO + comision_ventas

recibo_de_sueldo = f"""
-----------------------------------------------------
Liquidacion Vendedor
-----------------------------------------------------
Sueldo fijo:                         ${SUELDO_FIJO:15,.2f}
Comision por ventas:                 ${round(comision_ventas, 2):15,.2f}
-----------------------------------------------------
Total a cobrar:                      ${round(sueldo_a_cobrar, 2):15,.2f}
-----------------------------------------------------
"""


print(recibo_de_sueldo)


