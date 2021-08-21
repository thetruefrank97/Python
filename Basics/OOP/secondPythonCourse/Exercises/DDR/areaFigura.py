
PI = 3.14


def circulo(radio):
    areaCirculo = (radio**2) * PI
    return areaCirculo


def triangulo(base, altura):
    areaTriangulo = (base * altura) / 2
    return areaTriangulo


def cuadrado(lado):
    areaCuadrado = lado * lado
    return areaCuadrado


def main():
    eleccion = input("Introduce una figura: circulo, triangulo, cuadrado o F para salir: ")

    while eleccion != "F":
        if eleccion == "circulo":
            radio = float(input("Cual es el radio del circulo?: "))
            print("El area del circulo es {}".format(circulo(radio), ",.2f"))
        elif eleccion == "triangulo":
            base = float(input("Cual es la base del triangulo?: "))
            altura = float(input("Cual es la altura del triangulo?: "))
            print("El area del triangulo es {}".format(triangulo(base, altura), ",.2f"))
        elif eleccion == "cuadrado":
            lado = float(input("Cual es la longitud del lado del cuadrado: "))
            print("El area del cuadrado es {}".format(cuadrado(lado), ",.2f"))
        eleccion = input("Introduce una figura: circulo, triangulo, cuadrado o F para salir: ")


main()