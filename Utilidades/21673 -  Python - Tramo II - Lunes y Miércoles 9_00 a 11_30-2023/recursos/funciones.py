"""
Este Módulo implementa funciones de uso general.

- es_entero(str_numero) 
- es_flotante(str_numero) 
- es_entero_entre(str_numero) 
- es_flotante_entre(str_numero) 

"""




def es_entero(str_numero):
    try:  # INTENTO
        int(str_numero)
    except:  # SI HAY ERROR
        return False
    else:   # SI NO HAY ERROR
        return True


def es_flotante(str_numero):
    try:  # INTENTO
        float(str_numero)
    except:  # SI HAY ERROR
        return False
    else:   # SI NO HAY ERROR
        return True


def es_numero(str_numero):
    return es_entero(str_numero) or es_flotante(str_numero)


def leer_entero(cartel_para_el_usuario):
    todo_ok = False
    while not todo_ok:  # mientras error
        cadena = input(cartel_para_el_usuario)
        if es_entero(cadena):
            todo_ok = True
        else:
            print("Error: Tiene que ingresar un numero entero.")
    numero = int(cadena)
    return numero


def leer_flotante(cartel_para_el_usuario):
    todo_ok = False
    while not todo_ok:  # mientras error
        cadena = input(cartel_para_el_usuario)
        if es_flotante(cadena):
            todo_ok = True
        else:
            print("Error: Tiene que ingresar un numero Float.")
    numero = float(cadena)
    return numero


def leer_entero_entre(cartel_para_el_usuario, desde, hasta):
    todo_ok = False
    while not todo_ok:  # mientras error
        cadena = input(cartel_para_el_usuario)
        if es_entero(cadena):
            numero = int(cadena)
            if desde <= numero <= hasta:  # if numero >= desde and numero <= hasta
                todo_ok = True
            else:
                print(
                    f"Error: El numero no esta en el rango: [{desde}..{hasta}].")
        else:
            print("Error: Tiene que ingresar un numero entero.")
    return numero


def leer_flotante_entre(cartel_para_el_usuario, desde, hasta):
    todo_ok = False
    while not todo_ok:  # mientras error
        cadena = input(cartel_para_el_usuario)
        if es_flotante(cadena):
            numero = float(cadena)
            if desde <= numero <= hasta:  # if numero >= desde and numero <= hasta
                todo_ok = True
            else:
                print(
                    f"Error: El numero no esta en el rango: [{desde}..{hasta}].")
        else:
            print("Error: Tiene que ingresar un numero float.")
    return numero


def test_funciones():

    print(f"El nombre es: {__name__}")
    cantidad_patas_perro = leer_entero_entre(
        "Ingrese la cantidad de patas que tiene su perro: ", 1, 4)
    dia = leer_entero_entre("Dia: ", 1, 31)
    mes = leer_entero_entre("Mes: ", 1, 12)
    print(leer_flotante_entre("Importe: ", 1, 9999999.99))
    

if __name__ == '__main__':
    test_funciones()
