from Libro import Libro

def main():
    Libro1 = Libro(2234, "Chucky", "Lozano", 50)
    Libro2 = Libro(2222, "HAHAHAHAH", "EHEHHEHEEH", 100)

    if Libro1.numDePaginas > Libro2.numDePaginas:
        print("El libro {} tiene mas paginas".format(Libro1.Titulo))
    else:
        print("El libro {} tiene mas paginas".format(Libro2.Titulo))


main()