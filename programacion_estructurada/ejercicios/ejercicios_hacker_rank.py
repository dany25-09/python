# """ELEVAR UN NUMERO ( 1 < n < 20) AL CUADRADO"""

# from math import pow

# def mayor_o_menor(numero):
#     while numero < 1 or numero > 20:
#         numero = int(input("ingrese un numero mayor a 1 y menor a 20: "))
       

# lista = []
# def potencia_cuadrado(numero):
#     for i in range(numero):
#         potencia = int(pow(i, 2))
#         lista.append(potencia) 
#     return(lista)

# (potencia_cuadrado(3))

# def run():
#     numero = int(input("Ingrese un numero: "))
#     if mayor_o_menor(numero):  
#         mayor_o_menor(numero)
#         print(potencia_cuadrado(numero))
#     else:
#         print(potencia_cuadrado(numero))


# if __name__ == "__main__":
#     run() 








# """NUMERO CONDICIONAL"""

# def run():
#     n = int(input("").strip())
#     if n % 2 != 0:
#         print("Weird")
#     elif n % 2 == 0 and 2 <= n <= 5:
#         print("Not Weird")
#     elif n % 2 == 0 and 6 <= n <= 20:
#         print("Weird")
#     elif n % 2 == 0 and 20 < n:
#         print("Not Weird")

# if __name__ == "__main__":
#     run()


"""AÑO BICIESTO"""


def is_leap(year):
    if (year % 4 == 0) and (year % 100 != 0):
        return True
    elif (year % 100 == 0) and (year % 400 == 0):
        return True
    else:
        return False


year = int(input())
print(is_leap(year))

