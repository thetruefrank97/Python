from OOP.polimorfismo.Empleado import Empleado
from OOP.polimorfismo.Gerente import Gerente


def imprimir_detalles(objeto):
    # print(objeto)
    print(type(objeto))
    print(objeto.mostrar_detalles())


empleado = Empleado("Frank", 50000)
imprimir_detalles(empleado)


gerente = Gerente('Karla', 60000, "Sistemas")
imprimir_detalles(gerente)