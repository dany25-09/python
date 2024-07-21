"""
 METODOS QUE ACTUAN SOBRE OBJETOS (Cadenas) INMUTABLES 
 POR LO QUE SU CONTENIDO NO CAMBIA
"""

''' Encuentra una subcadena dentro de una cadena y 
    devuelve el índice donde lo encuentra
'''
# s = "El mundo está hecho de pequeños mundos"
# print(s.find("mundo"))
# print(s.index("mundo"))

''' Si la subcadena no existe dentro de la cadena
    el método (find) devuelve -1
    y el método (index) da un error de valor:
    ValueError: substring not found
'''
# s = "El mundo está hecho de pequeños mundos"
# print(s.find("otros"))
# print(s.index("otros"))

''' la búsqueda ocurre de izquierda a derecha. 
    Para buscar un conjunto de caracteres desde el final, 
    se utilza el método rfind() y rindex().
'''
# s = "El mundo está hecho de pequeños mundos"
# print(s.find("mundo"))  # Retorna la primera ocurrencia
# print(s.rfind("mundo"))  # Retorna la última

''' startswith() y endswith() indican si una cadena comienza o termina 
    con el conjunto de caracteres pasados como argumento, 
    y retornan True o False en función de ello.
'''
# s = "Hola mundo"
# print(s.startswith("Hola"))  #True
# print(s.endswith("mundo"))   #True
# print(s.endswith("world"))   #False

''' Los métodos isdigit(), isnumeric() e isdecimal() 
    determinan si todos los caracteres de la cadena 
    son dígitos, números o números decimales 
'''
# print("1234".isnumeric()) #True
# print("1234".isdecimal()) #True
# print("abc123".isdigit()) #False

''' Cadenas auto explicadas'''
# # Determina si todos los caracteres son alfanuméricos.
# print("abc123".isalnum()) #True
# # Determina si todos los caracteres son alfabéticos.
# print("abcdef".isalpha()) #True
# print("abc123".isalpha()) #False
# # Determina si todas las letras son minúsculas.
# print("abcdef".islower()) #True
# # Mayúsculas.
# print("ABCDEF".isupper()) #True
# # Determina si la cadena contiene todos caracteres imprimibles.
# print("Hola \t mundo!".isprintable()) #False
# # Determina si la cadena contiene solo espacios.
# print("Hola mundo".isspace()) #False
# print("    ".isspace()) #True

""" MÉTODOS DE TRANSFORMACIÓN """

''' Los métodos center(), ljust() y rjust() alinean una cadena
    en el centro, la izquierda o la derecha respectivamente. 
'''
# #La cadena se formatea a 10 caracteres
# print("Hola".center(10))  # '   Hola   '
# print("Hola".ljust(10))   # 'Hola      '
# print("Hola".rjust(10))   # '      Hola'


# """ MÉTODOS DE SEPARACIÓN """
# print("Hola mundo!\nHello world!".split())
# ['Hola', 'mundo!', 'Hello', 'world!']

# #El separador puede indicarse como argumento
# print("Hola mundo!\nHello world!".split(" "))   # ['Hola', 'mundo!\nHello', 'world!']

# ''' Para separar únicamente según saltos de línea:
#     Equivalente a split("\n")
# '''
# print("Hola mundo!\nHello world!".splitlines()) #['Hola mundo!', 'Hello world!']

# ''' Un segundo argumento en split() indica cuál es el máximo de divisiones 
#     que se requieren (-1) por defecto para representar una cantidad ilimitada
# '''
# print("Hola mundo hello world".split(" ", 2))  #['Hola', 'mundo', 'hello world']
"""
 METODOS QUE ACTUAN SOBRE OBJETOS (Cadenas) INMUTABLES 
 POR LO QUE SU CONTENIDO NO CAMBIA
"""

''' Encuentra una subcadena dentro de una cadena y 
    devuelve el índice donde lo encuentra
'''
# s = "El mundo está hecho de pequeños mundos"
# print(s.find("mundo"))
# print(s.index("mundo"))

''' Si la subcadena no existe dentro de la cadena
    el método (find) devuelve -1
    y el método (index) da un error de valor:
    ValueError: substring not found
'''
# s = "El mundo está hecho de pequeños mundos"
# print(s.find("otros"))
# print(s.index("otros"))

''' la búsqueda ocurre de izquierda a derecha. 
    Para buscar un conjunto de caracteres desde el final, 
    se utilza el método rfind() y rindex().
'''
# s = "El mundo está hecho de pequeños mundos"
# print(s.find("mundo"))  # Retorna la primera ocurrencia
# print(s.rfind("mundo"))  # Retorna la última

''' startswith() y endswith() indican si una cadena comienza o termina 
    con el conjunto de caracteres pasados como argumento, 
    y retornan True o False en función de ello.
'''
# s = "Hola mundo"
# print(s.startswith("Hola"))  #True
# print(s.endswith("mundo"))   #True
# print(s.endswith("world"))   #False

''' Los métodos isdigit(), isnumeric() e isdecimal() 
    determinan si todos los caracteres de la cadena 
    son dígitos, números o números decimales 
'''
# print("1234".isnumeric()) #True
# print("1234".isdecimal()) #True
# print("abc123".isdigit()) #False

''' Cadenas auto explicadas'''
# # Determina si todos los caracteres son alfanuméricos.
# print("abc123".isalnum()) #True
# # Determina si todos los caracteres son alfabéticos.
# print("abcdef".isalpha()) #True
# print("abc123".isalpha()) #False
# # Determina si todas las letras son minúsculas.
# print("abcdef".islower()) #True
# # Mayúsculas.
# print("ABCDEF".isupper()) #True
# # Determina si la cadena contiene todos caracteres imprimibles.
# print("Hola \t mundo!".isprintable()) #False
# # Determina si la cadena contiene solo espacios.
# print("Hola mundo".isspace()) #False
# print("    ".isspace()) #True

""" MÉTODOS DE TRANSFORMACIÓN """

''' Los métodos center(), ljust() y rjust() alinean una cadena
    en el centro, la izquierda o la derecha respectivamente. 
'''
# #La cadena se formatea a 10 caracteres
# print("Hola".center(10))  # '   Hola   '
# print("Hola".ljust(10))   # 'Hola      '
# print("Hola".rjust(10))   # '      Hola'


# """ MÉTODOS DE SEPARACIÓN """
# print("Hola mundo!\nHello world!".split())
# ['Hola', 'mundo!', 'Hello', 'world!']

# #El separador puede indicarse como argumento
# print("Hola mundo!\nHello world!".split(" "))   # ['Hola', 'mundo!\nHello', 'world!']

# ''' Para separar únicamente según saltos de línea:
#     Equivalente a split("\n")
# '''
# print("Hola mundo!\nHello world!".splitlines()) #['Hola mundo!', 'Hello world!']

# ''' Un segundo argumento en split() indica cuál es el máximo de divisiones 
#     que se requieren (-1) por defecto para representar una cantidad ilimitada
# '''
# print("Hola mundo hello world".split(" ", 2))  #['Hola', 'mundo', 'hello world']
