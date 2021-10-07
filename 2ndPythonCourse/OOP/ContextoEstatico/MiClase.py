class MiClase:

    variables_clase = "Valor variable clase"

    def __init__(self, variable_instancia):
        self.variable_instancia = variable_instancia

    @staticmethod
    def metodo_estatico():
        print("aahhaahha")

    @classmethod
    def metodo_de_clase(cls):
        print(cls.variables_clase)

    def metodo_instancia(self):
        self.metodo_estatico()
        self.metodo_de_clase()
        print(self.variables_clase)
        print(self.variable_instancia)


MiClase.metodo_estatico()
MiClase.metodo_de_clase()
miObjeto1 = MiClase("Variable_instancia")
miObjeto1.metodo_de_clase()
miObjeto1.metodo_instancia()
