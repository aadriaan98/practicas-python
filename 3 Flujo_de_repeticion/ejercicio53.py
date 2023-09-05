"""
Escribir un programa que permita ingresar nombre y edad de un grupo de personas (para cada una, nombre y edad). La carga termina cuando en el nombre de la persona se ingresa un asterisco ('*'). Mostrar al final cómo se llama la persona más joven.

"""
registro_personas = []

while True:
    #Se pide el nombre, si se ingresa * corta e imprime los nombres y edades ingresados
    nombre = input("Ingrese un nombre, (presione * para terminar): ")
    if nombre == "*":
        break
    else:
        #Se ingresa la edad y se almacenan con el nombre en la variable persona
        edad = int(input("Ingrese la edad de la persona: "))
        persona = (nombre, edad)
        #Se agrega persona a la lista con el metodo append
        registro_personas.append(persona)

#La funcion key= lambda se utiliza como argumento en la función min()
#En este caso específico, x representa una tupla dentro de la lista personas. x[1] accede al segundo elemento de la tupla, que en este caso es la edad de la persona. 
mas_joven = min(registro_personas, key=lambda x:x[1])

print(f"La persona mas joven es: {mas_joven}")