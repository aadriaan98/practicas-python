"""
Ejercicio 035
Existen dos reglas que identifican dos conjuntos de valores:

a) El número es de un solo dígito.
b) El número es impar.

A partir de estas reglas, escribir un programa que permita ingresar un número 
entero.
Debe asignar el valor que corresponda a las variables booleanas:

esDeUnSoloDigito
esImpar
estaEnAmbos
noEstaEnNinguno

el valor Verdadero o Falso, según corresponda, para indicar si el valor 
número ingresado pertenece o no a cada conjunto. 
Definir un lote de prueba de varios números y probr el algoritmo, 
escribiendo los resultados.
"""

numero = 15

# a) El número es de un solo dígito.
esDeUnSoloDigito =  -9 <= numero <= 9
# b) El número es impar.
esImpar = (numero%2) != 0 

estaEnAmbos = esDeUnSoloDigito and esImpar
noEstaEnNinguno =  not estaEnAmbos


print(
f"""
El numero {numero} tiene un solo digito: {esDeUnSoloDigito}
El numero {numero} es impar: {esImpar}
El numero {numero} esta en ambos: {estaEnAmbos}
El numero {numero} no esta en ninguno: {noEstaEnNinguno}"""
)

print(f"""

{numero} 
estaEnAmbos {estaEnAmbos} 
noEstaEnNinguno {noEstaEnNinguno}
esDeUnSoloDigito {esDeUnSoloDigito}
esImpar {esImpar}""")