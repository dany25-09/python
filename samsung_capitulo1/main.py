# #primera forma
# print("Calcule el factorial")
# fact = int(input("Ingrese el Número: "))
# result = 1
#
# for i in range(1, fact+1):
#     result = result * i
# print(f"el factorial de {fact}! es: {result}")




# segunda forma
# fact_5 = 5 * 4 * 3 * 2 * 1
# fact_10 = 10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1
#
# print("calcule el factorial")
# print(f"5! = {fact_5}")
# print("calcule el factorial")
# print(f"10! = {fact_10}")

#
# n = int(input("Ingrese la potencia a la que desea elevar los números: "))
# print("a\t n\t a**n")
# for numeros in range(2, 6+1):
#         print(f"{numeros}\t {n}\t {numeros ** n}")


# n = int(input("Ingrese el número: "))
# n = str(n)
#
# if n[0] == "3":
#     print(True)
# else:
#     print(False)


# print("Welcome to yummy restaurant. Here is the menu.")
# print("- Burger(enter b)")
# print("- Chicken(enter c)")
# print("- Pizza(enter p)")
# option = input("Choose a menu (enter b, c, p): ")
# if option == "b":
#     print("You chose Burger")
# elif option == "c":
#     print("You choose Chicken")
# elif option == "p":
#     print("You choose Pizza")
# else:
#     print("Ingrese al menú de nuevo")

# a, b = input("Ingrese los números: ").split()
# a = int(a)
# b = int(b)
# if a % b == 0:
#     print(f"{a} es multiplo de {b}")
# else:
#     print(f"{a} no es multiplo de {b}")


# print("1) Addition   2) Subtraction   3) Multiplication   4) Division")
# option = int(input("Enter the desired number of operation: "))
# print("Enter two numbers for operation.")
#
# num_1 = int(input("Ingrese el primer número: "))
# num_2 = int(input("Ingrese el segundo número: "))
#
#
# if option == 1:
#     result = num_1 + num_2
#     print(f"{num_1} + {num_2} = {result}")
#
# elif option == 2:
#     result = num_1 - num_2
#     print(f"{num_1} - {num_2} = {result}")
#
# elif option == 3:
#     result = num_1 * num_2
#     print(f"{num_1} x {num_2} = {result}")
#
# elif option == 4:
#     result = num_1 / num_2
#     print(f"{num_1} / {num_2} = {result}")
#
# else:
#     print("Entered an incorrect number.")


# n= int(input("Enter n: "))
#
#
# for fila in range(0, n):
#
#     if fila % 2 == 0:
#         for columna in range(1 , n + 1):
#             print(columna + n * fila,  "\t", end=" ")
#         print(" ")
#
#     if fila % 2 != 0:
#         for columna_2 in range(n, 0, -1):
#             print(columna_2 + n * fila, "\t", end=" ")
#         print(" ")




# n=int(input("Enter n: "))


# for fila in range(0, n):
#     for columna in range(0, n):
#         print(fila, columna)

#     if fila % 2 == 0:
#         for columna in range(1 , n + 1):
#             print(columna + n * fila,  "\t", end=" ")
#         print(" ")

# #     if fila % 2 != 0:
# #         for columna_2 in range(n, 0, -1):
# #             print(columna_2 + n * fila, "\t", end=" ")
# #         print(" ")


# name = float(input("ingrese un nombre: "))
#
# if name == str(name):
#     print("yeah")
# else:
#     print("No")



# dicc = {"messi" : 7, "CR7" : 5, "Modric" : 1}
#
#
# print(dicc.items())

# from collections import Counter
#
# numeros = [1, 2, 5, 4, 3, 2 , 1 , 9 , 9, 3, 7 , 3 , 9]
# contadores = Counter(numeros)
#
# numero_mas_repetido = max(n for n in contadores if contadores[n] == max(contadores.values()))
#
# print(f'El número más alto que se repite más es: {numero_mas_repetido}')
#



# tupla = (1, 2, 5, 4, 3, 2, 1, 9, 9, 3, 7, 3, 9)
# max_ocurrencias = 0
# elemento_frecuente = None
# for e in tupla:
#   ocurrencias = tupla.count(e)
#   if ocurrencias >= max_ocurrencias:
#     max_ocurrencias = ocurrencias
#     elemento_frecuente = e
#     if (e == None) > elemento_frecuente:
#       elemento_frecuente = e
# print("El elemento mas frecuente:", elemento_frecuente)


# #Unidad 10 parte 1
# #Q1
# primos_lista = [2, 3, 5, 7]
# print(primos_lista[0])
#
# #Q2
# primos_lista2 = [2, 3, 5, 7]
# primos_lista2.append(11)
# print(primos_lista2)
#
#
# #Q3
#
# lista1 = [3, 5, 7]
# lista2 = [2, 3, 4, 5, 6]
#
# for i in lista1:
#     for j in lista2:
#         result = i * j
#         print(f"{i} * {j} = {result}")





#Unidad 10 parte 2
#Q1
# cadenas_lista = ['abc', 'bcd', 'bcdefg', 'abba', 'cddc', 'opq']
#
# pal_corta = ""
#
# for palabra in cadenas_lista:
#     if pal_corta == "" or (len(palabra) < len(pal_corta)):
#         pal_corta = palabra
#
# print(pal_corta)



#Q2
# cadenas_lista = ['abc', 'bcd', 'bcdefg', 'abba', 'cddc', 'opq']
# pal_larga = ""
#
#
# for palabra in cadenas_lista:
#     if (pal_larga == "") or (len(palabra) > len(pal_larga)):
#         pal_larga = palabra
#
# print(pal_larga)



#Q3
# cadenas_list = ['abc', 'bcd', 'bcdefg', 'abba', 'cddc', 'opq']
#
# cadenas_list = sorted(cadenas_list, key=len)
#
# palabras = ""
# lista = []
#
# for pal in cadenas_list:
#     if palabras == "" or len(pal) <= len(palabras):
#         palabras = pal
#         lista.append(palabras)
#
# print(lista)



#Unidad 11    Parte 1
#Q1
# pais_capital = {
#     "Corea": "Seoul",
#     "China": "Beijing",
#     "USA": "Wasshington D.C"
# }
#
# pais = input("Ingrese el pais: ")
#
# if pais in pais_capital:
#     print(pais_capital[pais])
# else:
#     print("País no encontrado")


#Q2
# frutas_dic = {
#     "Manzana":5000,
#     "Banano":4000,
#     "Uva": 5300,
#     "Melon":6500
# }
# for clave, valor in frutas_dic.items():
#     print(f"el precio de un/a {clave} es {valor} KRW")




#Unidad 11    Parte 2
#Q1
# frutas_dic = {
#     "manzana" : 6000,
#     "melon" : 3000,
#     "banano" : 5000,
#     "naranja" : 4000,
# }
# print(frutas_dic.keys())
#
# if "manzana" in frutas_dic:
#     print("manzana está en frutas_dic")
# if "mango" not in frutas_dic:
#     print("mango no está en frutas_dic")




#Unidad 12   Parte 1
#Q2
#Como lo hizo Kev y funciona y es entendible

# reg_ventas= (100, 121, 120, 130, 140, 120, 122, 123, 190, 3)
# contador = 0
#
# for venta in range(1, len(reg_ventas)):
#     if reg_ventas[venta] < reg_ventas[venta - 1]:
#         contador += 1
#
# print(f"En los últimos 11 días, {contador} días han reducido las ventas en comparación con el día anterior.")



#Unidad 12   Parte 2
#Q1  Como lo hizo Kev
# tupla = (1, 2, 5, 4, 3, 2, 1, 9, 9, 3, 7, 3, 9,)
# max_ocurrencias = 0  #2
# elemento_frecuente = None
# for e in tupla:
#     ocurrencias = tupla.count(e)
#
#     if ocurrencias >= max_ocurrencias:
#         max_ocurrencias = ocurrencias
#         elemento_frecuente = e
#
#     if (elemento_frecuente == None) or (e > elemento_frecuente):
#         print(elemento_frecuente)
#         elemento_frecuente = e
# print("El elemento mas frecuente:", elemento_frecuente)



#Forma más corta.
# tupla = (1, 2, 5, 4, 3, 2, 1, 9, 9, 3, 7, 3, 9,)
# elemento_frecuente = None
# for e in tupla:
#     if (elemento_frecuente == None) or (e > elemento_frecuente):
#         print(elemento_frecuente)
#         elemento_frecuente = e
# print("El elemento mas frecuente:", elemento_frecuente)



# t = [(), (1,), [], 'abc', (), (), (1,), ('a',), ('a', 'b'), ((),), '']
# lista = []
# # print(type(t))
#
# for objeto in t:
#     if len(objeto) != 0:
#         lista.append(objeto)
#
# print(lista)







# lista4x4 = []
# for i in range(4):
#     linea = []
#     for j in range(4):
#         linea.append(i * 4 + j + 1)
#     lista4x4.append(linea)
#
# for i in range(4):
#     for j in range(4):
#         print(lista4x4[i][j], '\t', end='')
#     print()





# Unidad 13
# lista_2d = [[x+4*y for x in range(1,5)]
#           for y in range(4)]
# for i in lista_2d:
#     for j in i:
#         print("{:3d}".format(j), end=' ')
#     print()

# n = int(input('Escoge el numero de filas:'))
# m = int(input('Escoge el numero de columnas:'))
# matriz = []
# for i in range(n):
#     linea = []
#     for j in range(m):
#         if (i+j)%2==0:
#             linea.append(0)
#         else:
#             linea.append(1)
#     matriz.append(linea)
#
# for i in range(n):
#     for j in range(m):
#         print(matriz[i][j], end='')
#     print()



#
# n = int(input("Ingrese la cantidad de filas: "))
# # m = int(input("Ingrese la cantidad de columnas: "))
# # print(rango_n)
# # rango_m = range(m)
# print(f"La matriz es {n} x {n}")
# matriz = []
# for i in range(n):
#     lista = []
#     for j in range(n):
#         if i % 2 == 0 and j % 2 == 0:
#             lista.append(1)
#         elif i % 2 == 0 and j % 2 != 0:
#             lista.append(0)
#         elif i % 2 != 0 and j % 2 == 0:
#             lista.append(0)
#         elif i % 2 != 0 and j % 2 != 0:
#             lista.append(1)
#     matriz.append(lista)
#
# for x in matriz:
#     for y in x:
#         print(y, end="")
#     print("")



#Unidad 14
#Quiz final

# items = {"Cafe": 7, "Puma": 3, "Vaso de papel": 2, "Leche": 1, "coca -cola": 4, "Libro": 5,}
#
# while True:
#
#     print("Selecione el menú")
#     print("1) comprobar existencia")
#     print("2) almacenamiento")
#     print("3) liberación")
#     print("4) salir")
#     print()
#
#     opcion = int(input("Seleccione la opciión del menú: "))
#     print()
#     if opcion == 1:
#         articulo = input("Introduzca el articulo: ")
#
#         if articulo in items:
#             print(f"Existencias: {items[articulo]}")
#             print()
#         else:
#             print("El articulo no se encuentra en el inventario")
#             print()
#
#     if opcion == 2:
#         print(items)
#         print()
#
#     if opcion == 3:
#         liberacion, cantidad = input("Ingrese el articulo y numero de unidades que desea liberar del inventario: ").split(" ")
#         cantidad = int(cantidad)
#
#         if liberacion in items:
#             items[liberacion] = items[liberacion] - cantidad
#
#         else:
#             print("El articulo no se encuentra en el inventario")
#             print()
#
#     if opcion == 4:
#         print("Programa terminado")
#         break


# Unidad 15
# estudiante_tup = (
#     ('211101', "David Doe", '010-1234-4500'),
#     ('211102', ' John Smith', '010-2230-6540'),
#      ('211103', ' Jane Carter', '010-3232-7788')
#      )
#
# identificacion = input("Ingrese el numero de identificación del estudiante: ")
# diccionario_estudiantes = {}
#
# for estudiante in estudiante_tup:
#     diccionario_estudiantes[estudiante[0]] = [estudiante[1], estudiante[2]]
#
#
# if identificacion in diccionario_estudiantes:
#     print(f"{identificacion} es el estudiante {diccionario_estudiantes[identificacion][0]} y su numero de telefono es {diccionario_estudiantes[identificacion][1]} ")
#
# else:
#     print("Identificacion no recocnocida")


# Unidad 16
# Quiz 1

# lst = ["manzana", "mango", "banana"]
# S1 = set(lst)
#
# print(S1)

#Quiz 2

# s1 = {10, 20, 30, 40}
# s2 = {30, 40, 50, 60, 70}
#
# # 1) s1 | s2 Unión: {10, 20, 30, 40, 50, 60, 70}
# # 2) s1 & s2 intersección: {30, 40}
# # 3) s1 – s2 diferenica: {10, 20}
# # 4) s1 ^ s2 diferencia simetrica: {10, 20, 50, 60, 70}
# # 5) s1.issubset(s2): False
# # 6) s1.issuperset(s2): False
# # 7) s1.isdisjoint(s2): False
#
# print(s1 | s2)
# print(s1 & s2)
# print(s1 - s2)
# print(s1 ^ s2)
# print(s1.issubset(s2))
# print(s1.issuperset(s2))
# print(s1.isdisjoint(s2))


x = [1,2,3,4,5]

# largo = len(x)

for i in rangw:
    print(i)