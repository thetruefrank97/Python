class Persona:
    contador_personas = 0

    @classmethod
    def generar_siguiente_valor(cls):
        cls.contador_personas += 1
        return cls.contador_personas

    def __init__(self, nombre, edad):
        Persona.contador_personas += 1
        self._id_persona = Persona.generar_siguiente_valor()
        self._nombre = nombre
        self._edad = edad

    @property
    def id_persona(self):
        return self._id_persona

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
        return f'Persona [{self.id_persona} {self.nombre} {self.edad}]'


persona1 = Persona("Frank", 28)
print(persona1)
persona2 = Persona("Karla", 30)
print(persona2)
print(f'Valor contador personas: {Persona.contador_personas}')
persona3 = Persona("Juan", 40)
print(persona3)
Persona.generar_siguiente_valor()
persona4 = Persona("Maria", 35)
print(persona4)
print(f"Valor contador personas: {Persona.contador_personas}")
