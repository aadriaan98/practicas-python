numero = int(input("Ingrese un numero  "))

esDeUnSoloDigito = -9 <= numero <= 9
esImpar = (numero%2) != 0
estaEnAmbos = esDeUnSoloDigito and esImpar
noEstaEnNinguno = not esDeUnSoloDigito and not esImpar

print(f"""
      El numero {numero} 
      esDeUnSoloDigito= {esDeUnSoloDigito} 
      esImpar {esImpar} 
      estaEnAmbos {estaEnAmbos} 
      noEstaEnNinguno {noEstaEnNinguno} """)