"""
Escribir un programa que solicite al usuario su nombre y su edad, después pida una cantidad de años y muestre por pantalla un mensaje que indique cuántos años tendrá la persona después de sumarle a su edad la cantidad de años ingresada. El mensaje debe tener el siguiente formato: 'Hola, [nombre]. Dentro de [cantidad] años tendrás [edad + cantidad] años'".

Ejemplo: Si el usuario ingresa "Juan" y "20" y luego ingresa "5", el programa debe mostrar por pantalla "Hola, Juan. Dentro de 5 años tendrás 25 años".
"""

nombre = input("¿Cómo te llamas?: ")
edad = int(input("¿Cúantos años tenés?: "))
cAnios = int(input("ingrese una cantidad de años aleatoria: "))
suma = edad + cAnios

print(f"Hola {nombre}. Ténes {edad} años de edad. y dentro de {cAnios} años, vas a tener {suma} años de edad")