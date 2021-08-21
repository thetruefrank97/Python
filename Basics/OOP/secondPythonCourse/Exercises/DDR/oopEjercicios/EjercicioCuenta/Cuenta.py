class Cuenta:
    def __init__(self, titular: str, cantidad: any):
        self.__titular = titular
        self.__cantidad = cantidad

    @classmethod
    def Cuenta(cls, cantidad=0, titular="Frank"):
        return cls(titular, cantidad)

    @property
    def titular(self):
        return self.__titular

    @titular.setter
    def titular(self, titular):
        self.__titular = titular

    @property
    def cantidad(self):
        return self.__cantidad

    @cantidad.setter
    def cantidad(self, cantidad):
        self.__cantidad = cantidad

    def ingresar(self, cantidad: float):
        if cantidad > 0:
            self.__cantidad += cantidad

    def retirar(self, cantidad: float):
        if self.__cantidad - cantidad < 0:
            self.__cantidad = 0
        else:
            self.__cantidad -= cantidad

    def toString(self):
        return "Titular: {}, Cantidad: {}".format(self.__titular, self.__cantidad)
