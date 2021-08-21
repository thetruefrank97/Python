class Libro:
    def __init__(self, ISBN, Titulo, Autor, numDePaginas):
        self.__ISBN = ISBN
        self.__Titulo = Titulo
        self.__Autor = Autor
        self.__numDePaginas = numDePaginas

    @property
    def ISBN(self):
        return self.__ISBN

    @ISBN.setter
    def ISBN(self, ISBN):
        self.__ISBN = ISBN

    @property
    def Titulo(self):
        return self.__Titulo

    @Titulo.setter
    def Titulo(self, Titulo):
        self.__Titulo = Titulo

    @property
    def Autor(self):
        return self.__Autor

    @Autor.setter
    def Autor(self, Autor):
        self.__Autor = Autor

    @property
    def numDePaginas(self):
        return self.__numDePaginas

    @numDePaginas.setter
    def numDePaginas(self, numDePaginas):
        self.__numDePaginas = numDePaginas



