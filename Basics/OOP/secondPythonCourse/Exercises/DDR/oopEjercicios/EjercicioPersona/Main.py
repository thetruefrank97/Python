from Persona import Persona

def main():
    def MuestraMensajePeso(persona):
        IMC = persona.calcularIMC()

        if  IMC == 0:
            print("La persona esta en su peso ideal")
            return
        elif IMC == -1:
            print("La persona esta por debajo de su peso ideal")
            return
        elif IMC == 1:
            print("La persona esta por encima de su peso ideal")
            return

    def muestraMayorDeEdad(persona):
        if persona.esMayorEdad():
            print("La persona es mayor de edad")
        else:
            print("La persona es menor de edad")

    nombre = input("Introduce el nombre: ")
    edad = int(input("Introduce la edad: "))
    texto = input("Introduce el sexo: ")
    sexo = texto[0]
    peso = float(input("Introduce el peso: "))
    altura = float(input("Introduce la altura: "))

    persona1 = Persona.todoDefecto()
    persona2 = Persona.nombreEdadSexoDefecto()
    persona3 = Persona(nombre, edad, sexo, peso, altura)

    persona1.nombre = "Laura"
    persona1.edad = 30
    persona1.sexo = "M"
    persona1.peso = 60
    persona1.altura = 160

    persona2.peso = 90.5
    persona2.altura = 185

    print("Persona 1")
    MuestraMensajePeso(persona1)
    muestraMayorDeEdad(persona1)
    print(persona1.toString())

    print("Persona 3")
    MuestraMensajePeso(persona3)
    muestraMayorDeEdad(persona3)
    print(persona3.toString())


main()



