class Persona:

    def __init__(self, nombre, edad, *valores, **terminos):
        self._nombre = nombre
        self._edad = edad
        self._valores = valores
        self._terminos = terminos

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, edad):
        self._edad = edad

    def __str__(self):
        return f'La persona tiene estas caracteristicas: {self._nombre} {self._edad} {self._valores} {self._terminos} '


class Empleado(Persona):
    def __init__(self, nombre, edad, sueldo, *valores, **terminos):
        super().__init__(nombre, edad, *valores, **terminos)
        self._sueldo = sueldo

    def __str__(self):
        return f'{super().__str__()} Sueldo: {self._sueldo}'
