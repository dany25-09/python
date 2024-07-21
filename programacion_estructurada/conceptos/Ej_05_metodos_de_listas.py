"""
 METODOS QUE ACTUAN SOBRE OBJETOS (listas) MUTABLES 
 POR LO QUE SU CONTENIDO PUEDE SER MODIFICADO, ELIMINADO O INSERTADO
"""

# Append()
''' Este método permite agregar nuevos elementos al final de una lista
'''
# lista = [4, 1, 'Soy un texto', 3.1416, 0, True]
# print(lista)           # [4, 1, 'Soy un texto', 3.1416, 0, True]
# lista.append(10)
# print(lista)           # [4, 1, 'Soy un texto', 3.1416, 0, True, 10]
# lista.append([2,5])    
# print(lista)           # [4, 1, 'Soy un texto', 3.1416, 0, True, 10, [2, 5]]



''' El métdo Extend() también permite agregar elementos dentro de una lista, 
    pero a diferencia de append() al momento de agregar una lista, cada elemento
    de esta lista se agrega como un elemento más dentro de la otra lista
'''
# lista = [4, 1, 'Soy un texto', 3.1416, 0, True, 10, [2, 5]]
# print(lista)         # [4, 1, 'Soy un texto', 3.1416, 0, True, 10, [2, 5]]
# lista.extend(['yo','tú','él'])
# print(lista)         # [4, 1, 'Soy un texto', 3.1416, 0, True, 10, [2, 5], 'yo', 'tú', 'él']

''' El método remove(parámetro) remueve un elemento (parémetro) dentro de una lista, elemento que se 
    le pasa como parámentro
'''
# lista = [4, 1, 'Soy un texto', 3.1416, 0, True, 10, [2, 5]]
# lista.remove('Soy un texto')
# print(lista)      # [4, 1, 3.1416, 0, True, 10, [2, 5]]

''' El método index(parámetro), devuelve el número del índice de
    la lista en dónde se encuentra el parámetro
'''
# lista = [4, 1, 'Soy un texto', 3.1416, 0]
# print(lista.index('Soy un texto'))   # 2


''' El método reverse() sirve para invertir los elementos de una lista
    El método sort() sirve para ordenar los elementos de una lista
'''
# lista = [4, 1,  7, 0]
# print(lista)
# lista.reverse()  # La lista se vuelve un objeto iterable
# for i in lista:
#    print(i,end=' ')
# print()
# lista.sort()     # La lista se vuelve un objeto iterable
# for i in lista:
#    print(i,end=' ')

print(pow(2, 3))
print(abs(-10))