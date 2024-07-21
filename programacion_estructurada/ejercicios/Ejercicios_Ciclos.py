# Enunciado del problema

# Solicitar números hasta que se ingrese -1. Imprimir la suma de todos los números impares.


# Dada una lista de números enteros no negativos calcule la suma de todos los números que son impares. El final de la lista lo señala el número -1



# Entrada

# Una lista de números enteros separados por un salto línea. El último número se asegura de que será un -1, el cual señalará el final de la lista. El valor -1 no se considera como parte de la entrada.


# Salida

# Un número entero, la suma de todos los números enteros positivos impares en la lista que se dio en la entrada.



# lista = []
# x = 0
# suma = 0
# while x != -1:
#     x = int(input())
#     lista.append(x)
#     for i in range(len(lista)):
#       i = lista[i]
#       if i == -1:
#         lista.remove(i)
# y = 0 
# for j in range(len(lista)):
#   y = lista[j]
#   if y % 2 != 0:
#     suma = suma + y
# print(suma)