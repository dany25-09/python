# lenguajes = ["Python", "Java", "C", "C++"]  # Esto es una Lista
# print(lenguajes[0])
# print(lenguajes)
# 
# lenguajes = ("Python", "Java", "C", "C++")  # Esto es una Tupla
# print(lenguajes[0])
# print(lenguajes)
# 
# elmundo = {"Python": 1991, "C": 1972, "Java": 1996}  # Esto es un Diccionario
# print(elmundo["Python"])
# elmundo = {"Colombia": "Bogotá", "China": "Pekin", "USA": "washington"}  # Esto es un Diccionario
# print(elmundo["China"])
# print(elmundo)
# 
# 
# conjunto_1 = set('654')
# print(conjunto_1)
# 
conjunto_2 = {'1','5','2'}
# print(conjunto_2)
# 
# print(conjunto_1 & conjunto_2)
# 
# print(conjunto_1.intersection(conjunto_2))
# print(conjunto_1.union(conjunto_2))

# conjunto_1 = set('6546')  #sin duplicados
# print(conjunto_1)
# conjunto_1.add('11')
# print(conjunto_1)
# conjunto_1.remove('11') #discard
# print(conjunto_1)
# 
# conjunto_1 = set('Todos queremos')
# print(conjunto_1)
# 
# conjunto_1 = set({1,2,3})
# print(conjunto_1)
# 
# conjunto_1 = set(range(1,7))
# print(conjunto_1)

# print(5 in conjunto_1)  #si existe en el conjunto

# lista = list(("peras", "platanos", "uvas")) 
# print(lista)
# 
lista = ["peras", "platanos", "uvas"]
print(lista)

# lista.remove("platanos")
# print(lista)
# 
# lista.pop(1)
# lista.pop()
# print(lista)
# lista.pop()
# print(lista)
# lista.pop()
# print(lista)

# lista_2=[]
# print(lista_2)
# lista = list(("peras", "platanos", "uvas"))
# print(lista)
# del lista[0]
# print(lista)
# 
# lista.clear()
# print(lista)


lista = list(("peras", "platanos", "uvas")) 
print(lista)

for i in range(len(lista)):
      print(lista[i],end=' ')





#Crear una lista a partir de otra lista

# Crea un conjunto con una serie de elementos entre llaves
# Los elementos repetidos se eliminan
# c = {1, 3, 2, 9, 3, 1,2,9}
# print(c)    #{1, 2, 3, 9}


# Crea un conjunto a partir de un string
# Los caracteres repetidos se eliminan
# a = set('Hola Pythonista')
# print(a)     # {'a', 'H', 'h', 'y', 'n', 's', 'P', 't', ' ', 'i', 'l', 'o'}

# Crea un conjunto a partir de una lista
# Los elementos repetidos de la lista se eliminan
# unicos = set([3, 5, 6, 1, 5])
# print(unicos)    # {1, 3, 5, 6}


# lista = list(("cocos","peras", "melón","platanos", "uvas")) 
# nvalista = [x for x in lista if "a" in x]
# print(nvalista)

#anónimas o lambda   - lambda argumentos: expresión
 doble = lambda x: x * 2
 print(doble(7))
 
'''
filter crea una lista de elementos si usados en la llamada a una función devuelven True. 
Es decir, filtra los elementos de una lista usando un determinado criterio. 
'''
# Programa para filtrar los elementos pares de la lista
# lista = [2, 5, 4, 6, 8, 10, 3]
# nueva_lista = list(filter(lambda x: (x%2 == 0) , lista))
# print(nueva_lista)

# lista = range(-3, 5)
# menor_cero = list(filter(lambda x: x < 0, lista))
# print(menor_cero)

'''
El uso de map aplica una determinada función a todos los elementos de una entrada o lista.
forma: map(funcion_a_aplicar, lista_de_entradas)
'''
# nueva_lista = list(map(lambda x: x * 2 , lista))
# print(nueva_lista)