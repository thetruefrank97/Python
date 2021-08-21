meses = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
         "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")

lista = []

# Ejercicio 1
# mes = 1
# while mes != 0:
#     mes = int(input("Dame un numero entre 1 y 12 : "))
#
#     if 1 <= mes <= 12:
#         print(meses[mes - 1])

# Ejercicio 2

numero = int(input("Dame un numero: "))

for i in range(1, 6):
    resultado = i * numero
    print(numero, "* ", i, "= ", resultado)
    lista.append(i * numero)
print(lista)
