import math
import random


class Persona:
    def __init__(self, nombre, edad, sexo, peso, altura):
        self.__nombre = nombre
        self.__edad = edad
        self.__DNI = self.generarDni()
        self.__sexo = sexo
        self.__peso = peso
        self.__altura = altura

    @classmethod
    def nombreEdadSexoDefecto(cls, nombre="Frank", edad=23, sexo="Hombre", peso=0, altura=0):
        return cls(nombre, edad, sexo, peso, altura)

    @classmethod
    def todoDefecto(cls, nombre="", edad=0, sexo="H", peso=0, altura=0):
        return cls(nombre, edad, sexo, peso, altura)

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self, edad):
        self.__edad = edad

    @property
    def sexo(self):
        return self.__sexo

    @sexo.setter
    def sexo(self, sexo):
        self.__sexo = sexo

    @property
    def peso(self):
        return self.__peso

    @peso.setter
    def peso(self, peso):
        self.__peso = peso

    @property
    def altura(self):
        return self.__altura

    @altura.setter
    def altura(self, altura):
        self.__altura = altura

    def calcularIMC(self):
        INFRAPESO = -1
        PESO_IDEAL = 0
        SOBREPESO = 1
        pesoActual = self.__peso / math.pow(self.__altura, 2)
        if pesoActual >= 20 and pesoActual <= 25:
            return PESO_IDEAL
        elif pesoActual < 20:
            return INFRAPESO
        else:
            return SOBREPESO

    def comprobarSexo(self):
        if self.__sexo != "H" and self.__sexo != "M":
            self.__sexo = "H"

    def esMayorEdad(self):
        if self.__edad >= 18:
            return True
        else:
            return False

    def generarDni(self):
        divisor = 23

        # Generamos un numero de 8 digitos
        numDNI = int(random.randint(100000000000, 999999999999))
        res = int(numDNI - (numDNI/divisor * divisor))

        # Calculamos la letra del DNI
        letraDNI = self.generaLetraDNI(res)

        # Pasamos el DNI a String
        DNI = str(numDNI) + letraDNI
        return DNI

    def generaLetraDNI(self, res):
        letras = ["T", "R", "W", "A", "G", "M", "Y", "F", "P", "D", "X", "B", "N", "J", "Z",
                  "S", "Q", "V", "H", "L", "C", "K", "E"
                  ]
        return letras[res]

    def toString(self):
        if self.__sexo == "H":
            sexo = "Hombre"
        else:
            sexo = "Mujer"

        return "Informacion de la persona\n" \
                + "Nombre: " + self.__nombre + "\n" \
                + "Edad: " + str(self.__edad) + "anos \n" \
                + "Sexo: " + sexo + "\n" \
                + "DNI: " + str(self.__DNI) + "\n" \
                + "Peso: " + str(self.__peso) + "kg\n" \
                + "Altura: " + str(self.__altura) + "cm\n"
