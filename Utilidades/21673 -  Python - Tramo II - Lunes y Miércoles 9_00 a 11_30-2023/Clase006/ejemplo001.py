"""
y = f(x)
y = x^2

"""

def cuadrado(x):
    return x*x


def main():
    print("Hola Función")
    resultado = cuadrado(5)
    print("Resultado :",resultado)
    a = 10
    resultado = cuadrado(a)
    print("Resultado :",resultado)
    resultado = cuadrado(cuadrado(2))
    print("Resultado :",resultado)

    print(cuadrado(55))
main() # PUNTO DE ENTRADA AL PROGRAMA










