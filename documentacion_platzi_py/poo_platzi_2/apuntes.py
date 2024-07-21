# class Jugador_futbol():
#     def __init__(self, nombre, edad, equipo, goles, asistencias):
#         self.nombre         = nombre
#         self.edad           = edad
#         self.equipo         = equipo
#         self.goles          = goles
#         self.asistencias    = asistencias
#
#     def precio_de_mercado(self):
#        x = self.edad * self.asistencias * self.goles
#        return x
#
#     def datos_por_posicion(self):
#         print(f"Estos son los datos por posición: ")
#
# class portero(Jugador_futbol):
#     def __init__(self, nombre, edad, equipo, goles, asistencias, goles_encajados):
#         self.goles_encajados = goles_encajados
#
#         super().__init__(nombre, edad, equipo, goles, asistencias)
#
#     def datos_por_posicion(self):
#         print(f"Estos son los datos por posición: {self.goles_encajados}")
#
#
#
# class defensa(Jugador_futbol):
#     def __init__(self, nombre, edad, equipo, goles, asistencias, recuperaciones):
#         self.recuperaciones = recuperaciones
#
#         super().__init__(nombre, edad, equipo, goles, asistencias)
#
#     def datos_por_posicion(self):
#         print(f"Estos son los datos por posición: {self.recuperaciones}")
#
#
# class mediocampista(Jugador_futbol):
#     def __init__(self, nombre, edad, equipo, goles, asistencias, pases):
#         self.pases = pases
#
#         super().__init__(nombre, edad, equipo, goles, asistencias)
#
#     def datos_por_posicion(self):
#         print(f"Estos son los datos por posición: {self.pases}")
#
# class delantero(Jugador_futbol):
#     def __init__(self, nombre, edad, equipo, goles, asistencias, tiros_al_arco):
#         self.tiros_al_arco = tiros_al_arco
#
#         super().__init__(nombre, edad, equipo, goles, asistencias)
#
#     def datos_por_posicion(self):
#         print(f"Estos son los datos por posición: {self.tiros_al_arco}")
#
#
# if __name__ == "__main__":
#     primer_jugador  = portero("Ter_Steguen", 30, "Barcelona", 0 , 0, 12)
#     primer_jugador.datos_por_posicion()
#
#     segundo_jugador = defensa("Van Dijk", 30, "Livepool", 2, 0, 30)
#     segundo_jugador.datos_por_posicion()
#
#     tercer_jugador  = mediocampista("Pedri", 19, "Barcelona", 2, 4, 50)
#     tercer_jugador.datos_por_posicion()
#
#     cuarto_jugador  = delantero("Messi", 34, "PSG", 20, 14, 80)
#     cuarto_jugador.datos_por_posicion()
#
#     print(cuarto_jugador.precio_de_mercado())



#FACTORIAL

# import time
#
# def factorial(n):
#     respuesta = 1
#
#     while n > 1:
#         respuesta = respuesta * n
#         n = n - 1
#
#     return respuesta
#
#
# def factorial_recursivo(n):
#
#     if n == 1:
#         return n
#     return n * factorial(n - 1)
#
#
# n = 100000
#
# inicio = time.time()
# factorial(n)
# final = time.time()
# print(final - inicio)
#
# inicio = time.time()
# factorial_recursivo(n)
# final = time.time()
# print(final - inicio)


#EJERCICIOS COMPLEJIDAD

#O(1) Constante:

# def constant_algo(items):
#     result = items[0] * items[0]
#     print (result)
#
# constant_algo([4, 5, 6, 8])


#O(n) Lineal

# def linear_algo(items):
#     for item in items:
#         print(item)
#
# linear_algo([4, 5, 6, 8])


#O(n²) Polinomial

# def quadratic_algo(items):
#     for item in items:
#         for item2 in items:
#             print(item, ' ' ,item2)
#
# quadratic_algo([4, 5, 6, 8])


#BUSQUEDA LINEAL

# import random
#
# def busqueda_lineal(lista, objetivo):
#     match = False
#
#     for elemento in lista: # O(n)
#         if elemento == objetivo:
#             match = True
#             break
#
#     return match
#
#
# if __name__ == '__main__':
#     tamano_de_lista = int(input('De que tamano sera la lista? '))
#     objetivo = int(input('Que numero quieres encontrar? '))
#
#     lista = [random.randint(0, 15) for i in range(tamano_de_lista)]
#
#     encontrado = busqueda_lineal(lista, objetivo)
#     print(lista)
#     print(f'El elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista')




#BUSQUEDA BINARIA

# import random
#
# def busqueda_binaria(lista, comienzo, final, objetivo):
#     print(f'buscando {objetivo} entre {lista[comienzo]} y {lista[final - 1]}')
#     if comienzo > final:
#         return False
#
#     medio = (comienzo + final) // 2
#
#     if lista[medio] == objetivo:
#         return True
#     elif lista[medio] < objetivo:
#         return busqueda_binaria(lista, medio + 1, final, objetivo)
#     else:
#         return busqueda_binaria(lista, comienzo, medio - 1, objetivo)
#
#
# if __name__ == '__main__':
#     tamano_de_lista = int(input('De que tamano es la lista? '))
#     objetivo = int(input('Que numero quieres encontrar? '))
#
#     lista = sorted([random.randint(0, 50) for i in range(tamano_de_lista)])
#
#     encontrado = busqueda_binaria(lista, 0, len(lista), objetivo)
#
#     print(lista)
#     print(f'El elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista')



#ORDENAMIENTO DE BURBUJA

# import random
#
#
# def ordenamiento_de_burbuja(lista):
#     n = len(lista)
#
#     for i in range(n):
#         for j in range(0, n - i - 1): # O(n) * O(n) = O(n * n) = O(n**2)
#
#             if lista[j] > lista[j + 1]:
#                 lista[j], lista[j + 1] = lista[j + 1], lista[j]
#
#     return lista
#
# if __name__ == '__main__':
#     tamano_de_lista = int(input('De que tamano sera la lista? '))
#
#     lista = [random.randint(0, 100) for i in range(tamano_de_lista)]
#     print(lista)
#
#     lista_ordenada = ordenamiento_de_burbuja(lista)
#     print(lista_ordenada)




#ORDENAMIENTO POR INSEERCIÓN

# def ordenamiento_por_insercion(lista):
#
#     for indice in range(1, len(lista)):
#         valor_actual = lista[indice]
#         posicion_actual = indice
#
#         while posicion_actual > 0 and lista[posicion_actual - 1] > valor_actual:
#             lista[posicion_actual] = lista[posicion_actual - 1]
#             posicion_actual -= 1
#
#         lista[posicion_actual] = valor_actual







#ORDENAMIENTO POR MEZCLA

# import random
#
#
# def ordenamiento_por_mezcla(lista):
#     if len(lista) > 1:
#         medio = len(lista) // 2
#         izquierda = lista[:medio]
#         derecha = lista[medio:]
#         print(izquierda, '*' * 5, derecha)
#
#         # llamada recursiva en cada mitad
#         ordenamiento_por_mezcla(izquierda)
#         ordenamiento_por_mezcla(derecha)
#
#         # Iteradores para recorrer las dos sublistas
#         i = 0
#         j = 0
#         # Iterador para la lista principal
#         k = 0
#
#         while i < len(izquierda) and j < len(derecha):
#             if izquierda[i] < derecha[j]:
#                 lista[k] = izquierda[i]
#                 i += 1
#             else:
#                 lista[k] = derecha[j]
#                 j += 1
#
#             k += 1
#
#         while i < len(izquierda):
#             lista[k] = izquierda[i]
#             i += 1
#             k += 1
#
#         while j < len(derecha):
#             lista[k] = derecha[j]
#             j += 1
#             k += 1
#
#         print(f'izquierda {izquierda}, derecha {derecha}')
#         print(lista)
#         print('-' * 50)
#
#     return lista
#
#
# if __name__ == '__main__':
#     tamano_de_lista = int(input('De que tamano sera la lista? '))
#
#     lista = [random.randint(0, 100) for i in range(tamano_de_lista)]
#     print(lista)
#     print('-' * 20)
#
#     lista_ordenada = ordenamiento_por_mezcla(lista)
#     print(lista_ordenada)


# lista = []
# total_vals = int(input("Cuantos valores quieres graficar? "))
# for i in range(total_vals):
#     valors = int(input("Que valor quieres asignar: "))
#
#     lista.append(valors)
# print(lista)




