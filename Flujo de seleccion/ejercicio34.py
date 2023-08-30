"""
Escribir un programa que calcule y muestre el sueldo neto de un empleado en base a su sueldo básico y su antigüedad en años. 

Si es soltero se le incrementa el sueldo en 5% del salario bruto por cada año de antigüedad

si es casado se le incrementa el sueldo en 7% del salario bruto por cada año de antigüedad. 

También se le realizan los siguientes descuentos:

Jubilación: 11%

Obra Social: 3%

Sindicato: 3%

Como datos de entrada se ingresa por teclado el sueldo básico, antigüedad y estado civil (S: Soltero / C: Casado). Se debe informar: (reemplazando los 9 por los valores que correspondan)

Estado Civil: Soltero/Casado 

Sueldo básico: $ 999.99 

Antigüedad: 99 años

Descuentos:

Jubilación - 999,99

Obra Social - 999,99

Sindicato - 999,99

Sueldo Neto 999,99

"""

sueldo_basico = float(input("Ingrese el sueldo basico: "))
antiguedad = int(input("Ingrese la antiguedad "))
estado_civil = input("Ingrese el estado civil (S/s: Soltero, C/c: Casado) ")

plus_soltero = sueldo_basico * 0.05 
aporte_soltero = antiguedad * plus_soltero

plus_casado = sueldo_basico * 0.07
aporte_casado = antiguedad * plus_casado

jubilacion = sueldo_basico * 0.11

obra_social = sueldo_basico * 0.03

sindicato = sueldo_basico * 0.03

if estado_civil == "S" or estado_civil == "s":
    sueldo_neto = sueldo_basico + aporte_soltero - jubilacion - obra_social - sindicato    
    cadena = f"""
    Datos
    --------------------------------------
    Estado Civil: Soltero
    Antiguedad: {antiguedad}
    --------------------------------------
    Beneficios
    --------------------------------------
    Sueldo basico = ${sueldo_basico}
    Plus por antiguedad = ${aporte_soltero}
    --------------------------------------
    Descuentos
    --------------------------------------
    Jubilacion: -${jubilacion}
    Obra social: -${obra_social}
    Sindicato: -${sindicato}
    --------------------------------------
    Sueldo Neto: ${sueldo_neto}
    """
    print(cadena)
elif estado_civil == "C" or estado_civil == "c":
    sueldo_neto = sueldo_basico + aporte_casado - jubilacion - obra_social - sindicato    
    cadena = f"""
    Datos
    --------------------------------------
    Estado Civil: Casado
    Antiguedad: {antiguedad}
    --------------------------------------
    Beneficios
    --------------------------------------
    Sueldo basico = ${sueldo_basico}
    Plus por antiguedad = ${aporte_casado}
    --------------------------------------
    Descuentos
    --------------------------------------
    Jubilacion: -${jubilacion}
    Obra social: -${obra_social}
    Sindicato: -${sindicato}
    --------------------------------------
    Sueldo Neto: ${sueldo_neto}
    """
    print(cadena)
else:
    print("estado civil no valido")
    


