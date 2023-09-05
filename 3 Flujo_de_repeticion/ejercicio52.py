"""
Escribir un programa que permita un programa que permita ingresar la estatura (en metros con decimales) de cada jugador de un equipo de básquet La carga finalizará al ingresar cero. Calcular y mostrar la estatura promedio del equipo.

"""

estatura = []
contador = 0

#MI SOLUCION

while True:
    n = float(input("Ingrese la estatura del jugador: "))
    if n != 0:
        estatura.append(n)
        contador += 1
        suma = sum(estatura)
        promedio = suma / contador
        print(promedio)
    else:
        break

#ChatGPT
"""
estatura = []
suma = 0

while True:
    n = float(input("Ingrese la estatura del jugador (0 para finalizar): "))
    if n == 0:
        break
    estatura.append(n)
    suma += n
    promedio = suma / len(estatura)
    print("Estatura promedio:", promedio)

"""

        
        