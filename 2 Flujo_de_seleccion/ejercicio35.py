"""
Existen dos reglas que identifican dos conjuntos de valores:

a) El número es de un solo dígito.
b) El número es impar.
A partir de estas reglas, escribir un programa que permita ingresar un número entero.

Debe asignar el valor que corresponda a las variables booleanas:

esDeUnSoloDigito
esImpar
estaEnAmbos
noEstaEnNinguno
el valor Verdadero o Falso, según corresponda, para indicar si el valor número ingresado pertenece o no a cada conjunto. Definir un lote de prueba de varios números y probr el algoritmo, escribiendo los resultados.

"""

numero = int(input("Ingrese un numero: "))
un_digito = numero <= 9 and numero >= -9
es_impar = (numero % 2) != 0
esta_en_ambos = un_digito and es_impar
no_esta_en_ninguno = not un_digito and not es_impar

cadena = f"""
numero: {numero}
es de un digito: {un_digito}
es impar: {es_impar}
esta en ambos: {esta_en_ambos}
no esta en ninguno: {no_esta_en_ninguno}
"""
print(cadena)