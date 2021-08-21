from Cuenta import Cuenta


def main():
    cuenta1 = Cuenta("Chucky", 100)
    cuenta2 = Cuenta.Cuenta(200)

    cuenta1.ingresar(40000)
    cuenta1.retirar(20)
    print(cuenta1.toString())

    cuenta2.ingresar(300000)
    cuenta2.retirar(300500)
    print(cuenta2.toString())


main()