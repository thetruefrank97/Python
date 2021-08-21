def numeroDeCifras(numero):
    Cifras = 0
    while numero != 0:
        numero //= 10
        Cifras += 1
    return Cifras


def main():
    numero = int(input("Ingresa tu numero: "))
    print("Tu numero tienes esta cantidad de digitos {}".format(numeroDeCifras(numero)))


main()
