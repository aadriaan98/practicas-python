"""
Realizá un programa que permita ingresar 3 notas pertenecientes
a tres trimestres distintos para cierto alumno de nivel secundario. 
Debe calcularse y mostrarse la nota promedio.

leer 3 numeros
    leer 1 numero
    leer 1 numero
    leer 1 numero
calcular promedio
mostrar resultado

"""


n1 = float(input("Numero 1: "))
n2 = float(input("Numero 2: "))
n3 = float(input("Numero 3: "))

promedio = (n1 + n2 + n3) / 3

print("Notas:","[",n1,",",n2,",",n3,"] ==> ","Promedio:",promedio)

cadena_formato = f"Notas: < {n1},{n2},{n3} > ==> Promedio: {promedio:.2}"
print(cadena_formato)



