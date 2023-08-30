"""
Escribir un programa para calcular e imprimir la suma de los números comprendidos entre 42 y 176

"""
desde = 42
hasta = 177

suma = 0 

for n in range(desde, hasta):
    print(n)
    suma += n
    
print(f"La suma de los numeros comprendidos entre 42 y 176 es = {suma}")
