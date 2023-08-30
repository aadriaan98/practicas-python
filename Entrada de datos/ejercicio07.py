"""
Escribir un programa que permita ingresar un número entero. Debe mostrarse el número ingresado:

a. Multiplicado por 10. (utilizar el operador *) a. Dividido por 10. (utilizar el operador /) a. Elevado al cuadrado. (utilizar el operador **)

Cada resultado debe mostrarse en una línea distinta.

Ejemplo de ejecución:

Ingrese un número entero: 5
5 * 10 = 50
5 / 10 = 0.5
5 ** 2 = 25
"""

numero = int(input("Ingrese un numero entero: "))
division = numero / 10
producto = numero * 10
potencia = numero ** 2

cadena = f"""
numero: {numero}
division en 10: {division}
producto por 10: {producto}
cuadrado del numero {potencia}
"""

print(cadena)