class Product:
    def __init__(self,x,y):
        self._x = x
        self._y = y

    def methodA(self):
        pass

    def _methodB(self):
        pass

    @property
    def value(self):
       return self._x

    @value.setter
    def value(self,val):
        self._x = val


    @property
    def y(self):
        return self._y

    @y.setter
    def y(self,val):
        self._y = val


p = Product(12, 24)
print(p.y)