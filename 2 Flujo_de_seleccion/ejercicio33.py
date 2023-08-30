"""
La farmacia Sindical efectúa descuentos a sus afiliados según el importe de la compra con la siguiente escala:

Menor de $5500.0 el descuento es del 4.5%
Entre $5500.0 y $10000.0 el descuento es del 8%
Más de $10000.0 el descuento es del 10.5%
Escribir un programa que reciba un importe e informe: el descuento y el precio neto a cobrar, con mensajes aclaratorios.

"""

monto_abonado = float(input("Ingrese el monto a abonar: "))

desc1 = monto_abonado * 0.045
desc2 = monto_abonado * 0.08
desc3 = monto_abonado * 0.105

importe1 = monto_abonado - desc1
importe2 = monto_abonado - desc2
importe3 = monto_abonado - desc3

monto_ok = monto_abonado > 0

if monto_ok:
    if monto_abonado > 0 and monto_abonado < 5500:
        print(f"""
            Monto total: $ {monto_abonado}
            -------------------------------
            Su descuento es de: ${desc1}
            -------------------------------
            Importe a abonar: ${importe1}          
            """)
    elif monto_abonado >= 5500 and monto_abonado <= 10000:
        print(f"""
            Monto total: $ {monto_abonado}
            -------------------------------
            Su descuento es de: ${desc2}
            -------------------------------
            Importe a abonar: ${importe2}          
            """)
    else:
        print(f"""
            Monto total: $ {monto_abonado}
            -------------------------------
            Su descuento es de: ${desc3}
            -------------------------------
            Importe a abonar: ${importe3}          
            """)
else:
    print("Monto erroneo")      