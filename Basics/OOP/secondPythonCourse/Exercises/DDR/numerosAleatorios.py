import random


def generaNumeros(numero1, numero2):
    numeroRandom = random.randint(numero1, numero2)
    return numeroRandom


def main():
    numerosAleatorios = []
    rango = int(input("Cuantos numeros aleatorios quieres tener?: "))
    numeroInicial = int(input("Introducion el inicio de tus numero random: "))
    numeroFinal = int(input("Introducce el final de tus numero random: "))
    for numero in range(1, rango + 1):
        numerosAleatorios.append(generaNumeros(numeroInicial, numeroFinal))
    print(numerosAleatorios)


main()