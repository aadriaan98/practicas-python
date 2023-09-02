
"""
Leer un numero y mostrar la cantidad de digitos.
numero = 123456789 -> 9

"""

def contar_digitos(x):
    z = 1
    while x >= 10:
        if x >= 10:
            z += 1
            x /= 10
    return z

def contar_los_digitos(numero):        
    cadena = str(numero)
    return len(cadena)

def test():
    # numero = int(input("Ingrese un numero: "))

    cantidad_digitos = contar_digitos(12345678999999999999999999999999999999999)


    print("Cantidad de digitos es: ",cantidad_digitos)




test() # PROGRAMA PRINCIPAL



