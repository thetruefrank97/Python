if __name__ == "__main__":
    lista = []

    # Ejercicio 1
    cadena = input("Dame una cadena : ")

    for i in cadena:
         if i != " ":
            lista.append(i)

    print(lista)

    # Ejercicio 2
    for c in cadena:
        if (c not in lista) and (c != " "):
            lista.append(c)

    print(lista)
