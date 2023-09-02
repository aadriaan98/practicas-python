"""
Leer una lista de numeros hasta que se ingrese un cero. 
Mostrar la suma  

grupo ==> 1,5,4,7,8,5,4,5,8,74,5,8,7,0
grupo ==> 4,5,8,74,5,8,7,0
grupo ==> 0

"""
# ANTES (PARA TODOS)
suma = 0
numero = int(input("Numero: "))
while numero != 0:
    # DURANTE (PARA CADA DATO)
    suma += numero # suma = suma + numero (No nos gusta!!!!)
    numero = int(input("Numero: "))
# DESPUES (TOTALES)
print(f"Suma: {suma}")
