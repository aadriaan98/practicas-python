"""
Escribir un programa en Python que solicite al usuario ingresar dos valores que representen las medidas en grados de dos ángulos interiores de un triángulo. Luego, calcular y mostrar por pantalla el valor en grados del ángulo restante.

Es importante recordar que la suma de los ángulos interiores de todo triángulo es de 180 grados. Es decir, la suma de los ángulos internos de un triángulo siempre es igual a 180 grados. Por lo tanto, para calcular el ángulo restante es necesario restar la suma de los dos ángulos interiores ingresados al valor 180."

Para pensar:

¿Qué pasaría si se ingresan valores negativos como medidas de ángulos?
¿Qué sucedería si la suma de los dos ángulos ingresados es mayor o igual a 180 grados?
"""

angulo1 = int(input("Ingrese el 1° angulo: "))
angulo2 = int(input("Ingrese el 2° angulo: "))

suma = angulo1 + angulo2

angulo3 = 180 - suma

if angulo1 + angulo2 >= 0 and angulo1 + angulo2 < 180:
    print("El angulo restante mide:", angulo3,"°")
else: 
    print("La suma de los angulos no debe ser menor a 0° o mayor o igual que 180°")