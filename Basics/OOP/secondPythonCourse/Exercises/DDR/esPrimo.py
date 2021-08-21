def esPrimo(numero):
    divisionesEven = 0
    if numero <= 1:
        return False
    for currentNumber in range(1, numero + 1):
        if numero % currentNumber == 0:
            divisionesEven += 1
            if divisionesEven > 2:
                return False
    return True


def main():
    numero = int(input("Cual es tu numero?: "))
    if esPrimo(numero):
        print("El numero {} es primo".format(numero))
    else:
        print("El numero {} no es primo".format(numero))


main()

