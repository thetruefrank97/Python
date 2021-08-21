TIPO_DESC_FIJO = "Fijo"
TIPO_DESC_PORC =  "Porcentaje"

class Descuento:
    def __init__(self, tipo, valor):

        if not isinstance(valor,int):
            raise ValueError("constructor descuento: valor debe ser un numero")

        if not isinstance(tipo,str):
            raise ValueError("constructor descuento: tipo debe ser un string")

        if tipo != TIPO_DESC_PORC and tipo != TIPO_DESC_FIJO:
            raise ValueError("constructor descuento: el tipo debe ser fijo o porcentaje")

        if tipo == TIPO_DESC_FIJO and valor <= 0:
            raise ValueError("constructor descuento: el valor en el tipo fijo debe ser mayor que 0")

        if tipo == TIPO_DESC_PORC and (valor <= 0 or valor > 100):
            raise ValueError("constructor descuento: el valor en el tipo porcentaje debe estar entre 1 y 100 ")

        self.__tipo = tipo
        self.__valor = valor

    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, tipo):
        self.__tipo = tipo

    @property
    def valor(self):
        return self.__valor

    @valor.setter
    def valor(self, valor):
        self.__valor = valor

    def aplicar_descuento(self, precio):

        if self.__tipo == TIPO_DESC_FIJO:
            if precio > self.__valor:
                return precio - self.__valor
            else:
                return 0
        else:
            return precio - (precio * (self.__valor/100))

class Producto:

    def __init__(self, codigo, nombre, precio, descuento = None):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__precio = precio
        self.__descuento = descuento

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @property
    def precio(self):
        if self.__descuento == None:
            return self.__precio
        else:
            return self.__descuento.aplicar_descuento(self.__precio)


    @precio.setter
    def precio(self, precio):
        self.__precio = precio

    def calcular_total(self, unidades):
        return self.precio * unidades

    def __str__(self):
        return "Codigo: " + str(self.__codigo) + " nombre: " + self.__nombre + " precio: " + str(self.__precio)


class Pedido:

    def __init__(self):
        self.__productos = []
        self.__cantidades = []

    def anadir_producto(self, producto, cantidad):
        if not isinstance(producto, Producto):
            raise Exception("anadir producto: producto debe ser de la clase producto")

        if not isinstance(cantidad, int):
            raise Exception("anadir producto: cantidad debe ser un numero")

        if cantidad <= 0:
            raise Exception("anadir producto: cantidad debe ser mayor que 0")

        if producto in self.__productos:
            indice = self.__productos.index(producto)
            self.__cantidades[indice] = self.__cantidades[indice] + cantidad
        else:
            self.__productos.append(producto)
            self.__cantidades.append(cantidad)

    def eliminar_producto(self,producto):
        if not isinstance(producto, Producto):
            raise Exception("Eliminar producto: producto debe ser de la clase producto")

        if producto in self.__productos:
            indice = self.__productos.index(producto)
            del self.__productos[indice]
            del self.__cantidades[indice]
        else:
            raise Exception("eliminar producto: producto no existe")

    def total_pedido(self):
        total = 0

        for (p, c) in zip(self.__productos, self.__cantidades):
            total = total + p.calcular_total(c)
        return total

    def mostrar_pedido(self):
        for (p, c) in zip(self.__productos, self.__cantidades):
            print("Producto > ", p.nombre, ", Cantidad: " + str(c))


desc1 = Descuento(TIPO_DESC_FIJO, 5)
desc2 = Descuento(TIPO_DESC_PORC, 50)


p1 = Producto(1, "Producto 1", 5)
p2 = Producto(2, "Productos 2", 19, desc1)
p3 = Producto(3, "Producto 3", 99, desc2)

pedido = Pedido()

try:
    pedido.anadir_producto(p1, 5)
    pedido.anadir_producto(p2, 5)
    pedido.anadir_producto(p3, 5)

    print("Total pedido : " + str(pedido.total_pedido()))
    pedido.mostrar_pedido()

    pedido.eliminar_producto(p1)

    print("Total pedido : " + str(pedido.total_pedido()))
    pedido.mostrar_pedido()
except Exception as e:
    print(e)


