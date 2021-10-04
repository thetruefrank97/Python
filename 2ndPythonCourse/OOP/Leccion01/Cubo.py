class Cubo:

    def __init__(self, anchura, altura, profundidad):
        self.anchura = anchura
        self.altura = altura
        self.profundidad = profundidad

    def calcularVolumen(self):
        volumen = self.anchura * self.altura * self.profundidad
        return volumen


anchura = int(input("Pon la anchura porfa: "))
altura = int(input("Pon la altura porfa: "))
profundidad = int(input("Pon la profundidad porfa: "))
cubo1 = Cubo(anchura, altura, profundidad)
print(f'El volumen del cubo es: {cubo1.calcularVolumen()}')
