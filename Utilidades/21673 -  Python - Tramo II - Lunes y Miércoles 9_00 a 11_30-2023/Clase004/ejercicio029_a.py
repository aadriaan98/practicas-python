n1 = int(input("Ingrese nota parcial 1: "))
n2 = int(input("Ingrese nota parcial 2: "))

if n1<0 or n1>10 or n2<0 or n2>10:
    print('Error nota no valida')
elif n1 >= 7 and n2 >= 7:
    print("promociono")
elif n1 >= 4 and n2 >= 4:
    print("Aprobado")
else:
    print("recupera")