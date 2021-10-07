from Cuadrado import Cuadrado
from Rectangulo import Rectangulo
from FiguraGeometrica import FiguraGeometrica

#No se puede instancia una clase abstracta
# figura = FiguraGeometrica()

print("Creacion Objeto cuadrado".center(50, "-"))
cuadrado1 = Cuadrado(5, "verde")
print(f'Calculo area cuadrado: {cuadrado1.calcularArea()}')
print(cuadrado1)

print("Creacion Objeto rectangulo".center(50, "-"))
rectangulo1 = Rectangulo(3, 8, "Azul")
print(f'Calcula area rectangulo: {rectangulo1.area()}')
print(rectangulo1)

#MRO - method resolution order
# print(Cuadrado.mro())