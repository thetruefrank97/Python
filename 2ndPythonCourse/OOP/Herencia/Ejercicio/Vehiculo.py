class Vehiculo:
    def __init__(self, nombre, marca, *valores, **terminos):
        self._nombre = nombre
        self._marca = marca
        self._terminos = terminos
        self._valores = valores

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def marca(self):
        return self._marca

    @marca.setter
    def marca(self, marca):
        self._marca = marca

    def __str__(self):
        return f'El vehiculo tiene estas caracteristicas: {self._nombre} {self._marca}  '


class Coche(Vehiculo):
    def __init__(self, nombre, marca,  cilindros,  *valores, **terminos):
        super().__init__(nombre, marca, *valores, **terminos)
        self._cilindros = cilindros


    @property
    def cilindros(self):
        return self._cilindros

    @cilindros.setter
    def cilindros(self, cilindros):
        self._cilindros = cilindros

    def __str__(self):
        return f'{super().__str__()}: Este es el color del auto: {self._cilindros}'


class Bicicleta(Vehiculo):
    def __init__(self, nombre, color, marca, *valores, **terminos):
        super().__init__(nombre,  marca, *valores, **terminos)
        self._color = color


    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = color

    def __str__(self):
        return f'{super().__str__()} Este es el color de la bicicleta: {self._color}'


muscleCar = Coche("Challenger", "Dodge", 6)
print(muscleCar)
triciclo = Bicicleta("triciclo", "Verde", "Donnay")
print(triciclo)