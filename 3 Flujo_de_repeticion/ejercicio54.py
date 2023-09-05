"""
Escribir un programa que permita controlar con validación el ingreso a un sitio web. Teniendo dos constantes con un nombre de usuario ("admin") y una contraseña ("123456"), el programa debe permitir al usuario ingresar sus credenciales. Si las mismas son erróneas, se volverán a pedir hasta un máximo de 3 intentos. Finalmente, la computadora debe mostrar alguno de los siguientes mensajes según sea el caso: "Acceso concedido" o "Se ha bloqueado la cuenta"

"""
user_correcto = "admin"
pass_correcta = "123456"
intentos = 3


#Se pone la condicion que "mientras los intentos sean mayores que 0"
while intentos > 0:
    #se piden usuario y contraseña
    user = input("Ingrese el usuario: ")
    password = input("Ingrese la contraseña: ")
    #Se comparan usuario y contraseña, si es exitosa, se accede a la cuentta
    if user == user_correcto and password == pass_correcta:
        print("Acceso concedido")
        break
    #si es incorrecta, se resta un intento y se vuelve a preguntar y comparar
    else:
        print(f"Contraseña erronea, numero de intentos {intentos - 1}")
        intentos -= 1
        
#si se acaban los intentos se bloquea la cuenta
if intentos == 0:
        print("Cuenta bloqueada")
