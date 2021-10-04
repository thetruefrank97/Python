class Persona:
                                              #tuplas   #diccionarios
    def __init__(self,nombre, apellido, edad, *valores, **terminos):
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad
        self._valores = valores
        self._terminos = terminos


    def mostrar_detalle(self):
        print(f'Persona: {self._nombre} {self._apellido} {self._edad} {self._valores} {self._terminos}')


    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    def __del__(self):
        print(f'Persona: {self._nombre} {self._apellido} {self._edad} {self._valores} {self._terminos}')


if __name__ == "__main__":
    persona = Persona("Frank", "jajaajja", 123456789, "44455555555", 2, 3, 5, m='manzana', p='pera')
    persona.mostrar_detalle()
    print(persona.nombre)
    persona.nombre = "Loco"
    persona.mostrar_detalle()

