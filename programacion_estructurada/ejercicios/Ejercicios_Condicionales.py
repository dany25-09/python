# Enunciado del problema

# Para su trabajo se necesita que programe una herramienta de diagnóstico, esta herramienta determinará la hora en la que el servidor estuvo fuera de servicio o reportara que todo estaba en orden. (Client error, Server error)


# Recibirá cuatro enteros que representan la respuesta del servidor a una petición que realizó con otro programa. Estas peticiones fueron realizadas a la 1:00am, 1:30am, 2:00am, 2:30am, respectivamente.

# ENTRADA
# Cuatro números enteros, separados por salto de línea. Estos números representan códigos de estado del servidor.

# SALIDA
# Imprimir la palabra ‘Error’ seguido por la hora en que ocurrió el problema. En el caso de que no haya ocurrido ningún error imprimir la palabra ‘OK’.

# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# if a < 400 and b < 400 and c < 400 and d< 400 or a == b and b == c and c == d:
#     print("OK")
# if a >= 400:
#     print("Error 1:00am")
# if b >= 400:
#     print("Error 1:30am")
# if c >= 400:
#     print("Error 2:00am")
# if d >= 400:
#     print("Error 2:30am")








#Enunciado del problema
#Dado dos intervalos de números determinar la longitud de su intersección.


#Entrada
#4 números enteros que representan los intervalos. Los primeros dos representan el primer intervalo [n1,n2]. Los dos siguientes representan el segundo intervalo [n3,n4].

#Salida
#Un número entero l, la longitud de la intersección de estos intervalos.

# n1 = int(input())
# n2 = int(input())
# n3 = int(input())
# n4 = int(input())
# if(n1>=n3):
#     contador=n1
#     contadorAux=n1
# else:
#     contador = n3 
#     contadorAux = n3 
# if(n1>n2 or n3>n4):
#     print(0)
# else: 
#     while(contador<n2 and contador<n4):
#         contador += 1
#     print((contador)-(contadorAux))






# Enunciado del problema
# Dado dos esquinas cualquiera que representan un rectángulo. Determinar si un punto (x, y) está dentro de este rectángulo o está por fuera.



# Entrada
# 6 números reales, los cuatro primero son dos esquinas opuestas de un rectángulo. Los siguientes dos representan un punto en el plano.


# Salida
# Una cadena "dentro" o "fuera", dependiendo del caso

# x1 = float(input())
# y1 = float(input())
# x2 = float(input())
# y2 = float(input())
# xn = float(input())
# yn = float(input())
# if(x1>x2):
#     xmax = x1
#     xmin = x2
# else: 
#     xmax = x2 
# if(y1>y2):
#     ymax=y1
#     ymin=y2
# else:
#     ymax=y2
#     ymin=y1 
# if ((xn<xmax and xn>xmin)and(yn<ymax and yn>ymin)):
#     print("dentro")
# else:
#     print("fuera")






# Enunciado del problema

# El teorema fundamental de la aritmética o teorema de la factorización única, nos dice que todo número mayor a 1 se puede expresar como un único producto de números primos.


# Ahora tu tarea es ver si un número entero cualquiera mayor a uno, tiene a otros tres números enteros entre su factorización.



# Entrada
# Cuatro números enteros, donde el primero es cualquier número mayor a 1, y los otros tres son números primos.


# Salida
# Una cadena diciendo “Es uno de mis compuestos” o “Nunca he visto a este numero”. Dependiendo del caso


# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# m = b * c * d
# if a % m == 0:
#     print("Es uno de mis compuestos")
# else:
#     print("Nunca he visto a este numero")







# Enunciado del problema
# Como tarea tienes que simular el funcionamiento de una calculadora. Primero recibirá una cadena que representa la operación que necesitas realizar ‘+’, ‘-’, ‘*’, ‘/’, ‘sqrt’, ‘pow’. Las cuales representan la suma, resta, multiplicación, división, raíz cuadrada y exponenciación.


# Después de recibir la cadena recibira dos números enteros, excepto en el caso de raiz cuadrada, en el cual solo recibira uno. Con estos números debe realizar la operación correspondiente.



# Entrada

# Una cadena, seguido de dos números enteros separados por una línea de salto.


# Salida

# Un número entero que representa el resultado de la operación

# cadena=input()
# if(cadena!="sqrt"):
#     a=int(input())
#     b=int(input())
#     if(cadena=="+"):
#         print(a+b)
#     else:
#         if(cadena=="-"):
#             print(a-b)
#         else:
#             if(cadena=="*"):
#                 print(a*b)
#             else:
#                 if(cadena=="/"):
#                     print(int(a/b))
#                 else:
#                     if(cadena=="pow"):
#                         print(int(a**b))
# else:                    
#     a=int(input())
#     print(int(a**(0.5)))





