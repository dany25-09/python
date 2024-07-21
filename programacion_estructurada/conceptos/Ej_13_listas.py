#append()
#
articulos = ["zapatos", "chaquetas", "corbatas", "sacos", "camisas","medias"]
nvos_articulos = []

for x in articulos:
  if "t" in x:
    nvos_articulos.append(x) # guarda los artículos que contienen una (t)

print(nvos_articulos)

#===================================================

"""
   Ordenamiento de listas
"""
#Ascendente 
# articulos = ["zapatos", "chaquetas", "corbatas", "sacos", "camisas"]
# articulos.sort() #altera la lista original
# print(articulos)

# numeros = [99, 34, 65, 7, 23, 44, 88,15]
# numeros.sort() #altera la lista original
# print(numeros)

#===================================================
#Descendente
# numeros = [99, 34, 65, 7, 23, 44, 88,15]
# numeros.sort(reverse = True) #altera la lista original
# print(numeros)

#===================================================
"""
   Copiar listas
"""

# articulos = ["zapatos", "chaquetas", "corbatas", "sacos", "camisas"]

# nvos_articulos = [x for x in articulos if "t" in x] #forma más corta que #___A

# print(nvos_articulos)


#===================================================

# articulos = ["zapatos", "chaquetas", "corbatas", "sacos", "camisas"]

# nvos_articulos = [x for x in articulos]

# print(nvos_articulos)

#===================================================

# articulos = ["zapatos", "chaquetas", "corbatas", "sacos", "camisas"]
# copia_lista = articulos.copy()
# print(copia_lista)

#===================================================
# articulos = ["zapatos", "chaquetas", "corbatas", "sacos", "camisas"]
# otros = articulos   # las variable comparte el mismo espacio de memoria
# print ("Direcciones iguales: ",id(articulos), id(otros)) #las direcciones son iguales
# copia_lista = list(articulos) # las variable tiene direcciones distintas
# print("Direcciones diferentes:",id(articulos),id(copia_lista))

#===================================================

"""
   Unión de listas
"""
# Método 1 con lista aparte
# lista_1 = ["a", "b", "c"]
# lista_2 = [1, 2, 3]

# lista_3 = lista_1 + lista_2
# print(lista_3)

#Método 2 sobre la misma lista
# lista_1 = ["a", "b" , "c"]
# lista_2 = [1, 2, 3]

# lista_1.extend(lista_2)
# print(lista_1)

#usando append

# for x in lista_2:
#       lista_1.append(x)

# print(lista_1)

#===================================================
#Otros métodos asociados

#clear() límpia toda la lista

# articulos = ["zapatos", "chaquetas", "corbatas", "sacos", "camisas"]
# print(articulos)
# articulos.clear()
# print(articulos)

#remove() elimina un elemento

# articulos = ["zapatos", "chaquetas", "corbatas", "sacos", "camisas"]
# print(articulos)
# articulos.remove("corbatas")
# print(articulos)

#index() devuelve el índice de un elemento

# lista = [10, 25, 8, 56, 11, 98]
# x = lista.index(8)
# print("El índice es:", x)

#insert(pos, elemento) un elemente de cualquier tipo (string, number, object, etc.)

# lista =[10, 25, 8, 56, 11, 98]
# print(lista)
# lista.insert(3,"valor insertado")
# print(lista)

#pop() remueve elemento de una posición dada, por default elimina el último [-1]

# lista =[10, 25, 8, 56, 11, 98]
# print(lista)
# lista.pop(2)
# print(lista)