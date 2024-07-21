# '''
#    Métodos de diccionarios
# '''
# colores = { "rojo":"red","amarillo":"yellow", "azul":"blue", "gris":"gray","verde":"green" }
# for clave, valor in colores.items():
#     print(clave, valor)

# # clear()	      Elimina todos los elementos de un dictionario

# # copy()	         Devuelve una copia de un diccionario
# copiaColores = colores.copy()
# print(copiaColores)

# # fromkeys()	   Crea un dictionario con llaves y valor específico para todas las llaves
# llaves = ('llave1', 'llave2', 'llave3')
# valores = (100)
# diccionario = dict.fromkeys(llaves,valores)
# print(diccionario)

# # get()	         Returns the value of the specified key
# print(colores.get('negro','no se encuentra'))

# # items()	      Returns a list containing a tuple for each key value pair
# print(colores.items())  # dict_items([('rojo', 'red'), ('amarillo', 'yellow'), ('azul', 'blue'), ('gris', 'gray'), ('verde', 'green')])

# # keys()	         Returns a list containing the dictionary's keys
# print(colores.keys())   # dict_keys(['rojo', 'amarillo', 'azul', 'gris', 'verde'])

# # pop()	         Removes the element with the specified key
# print(colores.pop("amarillo", "no se ha encontrado"))  # yellow
# print(colores.pop("negro","no se ha encontrado"))      # no se ha encontrado

# # popitem()	      Elimina la última llave:valor del diccionario
# print(colores.popitem())  #('verde', 'green')

# # setdefault()	   Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
# carro = {
#   "marca": "Audi",
#   "modelo": "A8",
#   "año": 2021
# }
# carro.setdefault("color", "plata")  # como la llave no existe entonces la inserta y si existe se acutualiza
# print(carro)   # {'marca': 'Audi', 'modelo': 'A8', 'año': 2021, 'color': 'plata'}

# # update()	      Actualiza (inserta) {Llave: Valor} a un diccionario
# carro = {
#   "marca": "Audi",
#   "modelo": "A8",
#   "año": 2021
# }
# carro.update({"cilindraje":"2000Cm3"})  # inserta llave:valor en el diccionario
# print(carro)   # {'marca': 'Audi', 'modelo': 'A8', 'año': 2021, 'cilindraje': '2000Cm3'}

# # values()	      Devuelve todos los valores de un diccionario
# print(colores.values()) # dict_values(['red', 'yellow', 'blue', 'gray', 'green'])


# '''
# Las tuplas sólo tienen dos métodos

# Método	      Descripción
# ======         ===========
# count()	      Devuelve el número de veces que un ítems se repite en una tupla
# index()	      Buca en una tupla un valor específico y devuelve la posicion en dónde lo encontró

# '''