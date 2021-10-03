
nombres = ["Juan", "jajajaaj", "geranimo", "xd"]
print(nombres)

# acceder a los elementos de una lista
print(nombres[0])
print(nombres[1])


# acceder a elementos de manera inversa
print(nombres[-1])


#imprimir un rango
print(nombres[0:2]) # Sin incluir el indice 2

#Ir del inicio de la lista al indice (sin incluirla)
print(nombres[:3])

#Desde el indice indicado hasta el final
print(nombres[1:])


# iterar una lista
for nombre in nombres:
    print(nombre)
else:
    print("No existen mas nombres en la lista")


# preguntar el largo de una lista
print(len(nombres))

#agregar un elemento
nombres.append("Lorenzo")
print(nombres)

#Insertar un elemento en un indice en especifico
nombres.insert(1, "insigne")
print(nombres)

#remover un elemento
nombres.remove("Lorenzo")
print(nombres)

#remover el ultimo valor agregado
nombres.pop()
print(nombres)

#eliminar un indice
del nombres[1]
print(nombres)


#Limpiar la lista
nombres.clear()
print(nombres)

#borrar la lista por completo
del nombres
print(nombres)


