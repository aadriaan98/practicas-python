"""
Una editorial determina el precio de un libro según la cantidad de páginas que contiene. 

El costo básico del libro es de $1000, más $35,10 por página con encuadernación rústica.

Si el número de páginas supera las 300 la encuadernación debe ser especial, lo que incrementa el costo en $1200. 

Además, si el número de páginas sobrepasa las 600 se hace necesario otro procedimiento de encuadernación que incrementa el costo en $880. 

Desarrollar un programa que calcule el costo de un libro dado el número de páginas.
"""
num_paginas = int(input("Ingrese el número de páginas del libro: "))

COSTO_BASICO = 1000
COSTO_POR_PAGINA = 35.10
COSTO_ENC_RUSTICA = 1200
COSTO_ENC_ESPECIAL = 880

costo = COSTO_BASICO + (COSTO_POR_PAGINA * num_paginas)

if num_paginas <= 300:
    COSTO_BASICO
elif num_paginas > 300:
    COSTO_ENC_RUSTICA
elif num_paginas > 600:
    COSTO_ENC_ESPECIAL    


print("El costo del libro es: $", costo)