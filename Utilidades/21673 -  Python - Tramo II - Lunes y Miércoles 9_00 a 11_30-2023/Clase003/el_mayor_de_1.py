
a,b,c = 5,10,5


maximo = a
medio = b
minimo = c

if b > maximo:
    maximo = b
    medio = a
    minimo = c

if c > maximo:
    maximo = c
    medio = a
    minimo = b


if minimo > medio:
    aux = minimo
    minimo = medio
    medio = aux
       
    medio,minimo = minimo,medio

print(f"{maximo},{medio},{minimo}")




