
if __name__ == "__main__":
    rango1_a_10 = []
    for i in range(10):
        rango1_a_10.append(i + 1)
    print(rango1_a_10)

    tupla = (1,2,3,4,5,6,7,8,9,10)
    indice = int((input(f"Dame un indice : ")))

    if indice >= 0 and indice < len(tupla):
        print(tupla[indice])
    else:
        print("Indice no valido")

    lista_numeros = []
    suma = 0
    media = 0
    numero = 0

    for i in range(10):
        numero = int(input(f"Dame un numero : "))
        lista_numeros.append(numero)
        suma += numero

    # for x in lista_numeros:
    #     print(i)

    media = suma / len(lista_numeros)

    print("La suma es ", suma)
    print("La media es ", media)