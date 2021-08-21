tupla = ("Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio"
         ,"Agosto","Septiembre","Octubre","Noviembre","Diciembre")
mes = 1

# Ejercicio 1
# while mes != 0:
#     numero = int(input("Dame un numero entre el 1 y 12 : "))
#     if 1 <= numero <= 12:
#         print(tupla[numero - 1])
#     else:
#         print("La cagaste compa ")
#         break

# Ejercicio 2

numero = int(input("Dame un numero : "))
lista = []
multiplo = 0

for i in range(1, 6):
    multiplo = numero * i
    lista.append(multiplo)
print(lista)
