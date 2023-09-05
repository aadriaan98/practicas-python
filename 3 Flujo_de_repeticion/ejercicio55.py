"""
Escribir un programa que permita para cada cliente que va al banco "Express".

Cada cliente indica su número de documento y aguarda a ser atendido, cuando finaliza la atención del día se ingresa -1 para indicar que no hay más clientes para ser atendidos. El banco desea saber quién fue el primer cliente atendido y quién fue el último.

"""
clientes = []

while True:
    
    cliente = input("Ingrese su DNI para ser atendido: ")
    if cliente == "-1":
        primer_cliente = clientes[0]
        ultimo_cliente = clientes[-1]
        break 
    else:
        clientes.append(cliente)
        
print(f"el primer cliente fue {primer_cliente} y el ultimo {ultimo_cliente}")
  
