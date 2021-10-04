class Aritmetica:
    """
    Clase aritmetica para realizar las operaciones de sumar, restar, etc
    """

    def __init__(self, operandoA, operandoB):
        self.operandoA = operandoA
        self.operandoB = operandoB

    def sumar(self):
        resultado = self.operandoA + self.operandoB
        return resultado

    def restar(self):
        resultado = self.operandoA - self.operandoB
        return resultado

    def multiplicar(self):
        resultado = self.operandoA * self.operandoB
        return resultado

    def dividir(self):
        resultado = self.operandoA / self.operandoB
        return resultado


aritmetica1 = Aritmetica(20, 40)
print(f'Suma: {aritmetica1.sumar()}')
print(f'Resta: {aritmetica1.restar()}')
print(f'Multiplicacion: {aritmetica1.multiplicar()}')
print(f'Division: {aritmetica1.dividir()}')



