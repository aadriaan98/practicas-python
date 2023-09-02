



def leer_entero(cartel_para_el_usuario):
    todo_ok = False
    while not todo_ok: # mientras error 
        cadena = input(cartel_para_el_usuario)
        if cadena.isnumeric():
            todo_ok = True
        else:
            print("Error: Tiene que ingresar un numero entero.")
    numero = int(cadena)    
    return numero

def leer_entero_entre(cartel_para_el_usuario,desde,hasta):
    todo_ok = False
    while not todo_ok: # mientras error 
        cadena = input(cartel_para_el_usuario)
        if cadena.isnumeric():
            numero = int(cadena)
            if desde <= numero <= hasta: # if numero >= desde and numero <= hasta
                todo_ok = True
            else:
                print(f"Error: El numero no esta en el rango: [{desde}..{hasta}].")    
        else:
            print("Error: Tiene que ingresar un numero entero.")        
    return numero


def test_funciones():
    cantidad_patas_perro = leer_entero_entre("Ingrese la cantidad de patas que tiene su perro: ",1,4)
    dia = leer_entero_entre("Dia: ",1,31)
    mes = leer_entero_entre("Mes: ",1,12)


test_funciones()













