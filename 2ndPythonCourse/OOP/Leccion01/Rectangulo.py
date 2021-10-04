class Rectangulo:

    def __init__(self, Base, Altura):
        self.Base = Base
        self.Altura = Altura

    def calcularArea(self):
        Area = self.Base * self.Altura
        return Area


base = int(input("Proporciona la base: "))
altura = int(input("Proporciona la altura: "))
rectangulo1 = Rectangulo(base, altura)
print(f'El area del rectangulo es: {rectangulo1.calcularArea()}')