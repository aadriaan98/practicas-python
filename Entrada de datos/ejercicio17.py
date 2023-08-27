"""
¡Ayuda! Se me rompió el programa que convierte una cantidad de dinero en la cantidad mínima de billetes y monedas necesarios. Tengo todas las instrucciones necesarias, pero están todas mezcladas. ¿Podrías ayudarme a ordenarlas de manera correcta para que funcione el programa como debería? A lo mejor se me perdieron algunas instrucciones, ¿podrías agregarlas?

"""
cantidad_total = int(input("Ingrese la cantidad de dinero a convertir: "))
resto = cantidad_total
billetes_cien = resto // 100
#resto = resto % 100
billetes_cinco = resto // 5
billetes_mil = resto // 1000
billetes_cincuenta = resto // 50
billetes_doscientos = resto // 200
billetes_diez = resto // 10
#billetes_docientos = resto // 200
#resto = resto % 10
billetes_uno = resto // 1

cadena = f"""
Para la cantidad de {cantidad_total}, se necesitan: 
---------------------------------------------------
{billetes_mil} billetes de mil
---------------------------------------------------
{billetes_doscientos} billetes de doscientos
---------------------------------------------------
{billetes_cien} billetes de cien
---------------------------------------------------
{billetes_cincuenta} billetes de cincuenta
---------------------------------------------------
{billetes_diez} billetes de diez
---------------------------------------------------
{billetes_cinco} billetes de cinco
---------------------------------------------------
{billetes_uno} billetes de uno
"""
print(cadena)