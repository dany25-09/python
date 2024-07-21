# '''Pesos colombianos a dolares'''

# pesoColombiano = float(input("Ingrese la cantidad de dinero que tiene: "))
# precioDolar = 4401
# conversionMoneda = round(pesoColombiano / precioDolar, 3)
# print(f"Usted tiene {conversionMoneda} dolares")

# '''Dolares a pesos colombianos'''
# dolar = float(input("Ingrese la cantidad de dolares que tiene: "))
# precioPeso = 0.23
# conversionMoneda2 = round(dolar / precioPeso, 3)
# print(f"Usted tiene {conversionMoneda2} pesos colombianos") 





# """ NUMERO PRIMO"""

def primo(numero):
    if numero <= 1:
        return False
    elif numero == 2:
        return True
    else:
        for i in range (2, numero):
            if numero % i == 0:
                return False
            else:
                return True

def run():
    numero = int(input("Ingresa un numero: "))
    if primo(numero):
        print("Es primo")
    else:
        print("No es primo")

if __name__ == "__main__":
    run()








# """Numero al azar juego"""
# import random


# def run():
#     numero_aleatorio = random.randint(1, 100)
#     numero_elegido = int(input('Elige un nÃºmero del 1 al 100: '))
#     while numero_elegido != numero_aleatorio:
#         if numero_elegido < numero_aleatorio:
#             print('Busca un numero mas grande')
#             numero_elegido = int(input('Elige otro numero: '))
#         else:
#             print('Busca un numero mas pequeño')
#             numero_elegido = int(input('Elige otro numero: '))
#     print('Ganaste!!')


# if __name__ == '__main__':
#     run() 






# """"GENERADOR DE CONTRASEÑAS"""

# import random
# import string

# def generar_contrasena():
#     caracter = string.ascii_lowercase + string.digits + string.punctuation + string.ascii_uppercase

#     contrasena = []

#     while (len(contrasena) < 16):
#         caracteres=random.choice(caracter)    
#         contrasena.append(caracteres)

#     contrasena = "".join(contrasena)
#     return contrasena

# def run():
#     contrasena = generar_contrasena()
#     print('Tu nueva contraseña es: '+ contrasena)

# if __name__ == "__main__":
#     run()







# """PALABRA PALINDROMA"""
# def palindromo(palabra):
#     palabra = palabra.replace(' ', '')
#     palabra = palabra.lower()
#     palabra_invertida = palabra[::-1]
#     if palabra == palabra_invertida:
#         return True
#     else:
#         return False


# def run():
#     palabra = input('Escribe una palabra: ')
#     es_palindromo = palindromo(palabra)
#     if es_palindromo == True:
#         print('Es palíndromo')
#     else:
#         print('No es palíndromo')


# if __name__ == '__main__':
#     run()




import random

numero_aleatorio = random.randint(1, 100)
numero_elegido = int(input('Elige un numero del 1 al 100: '))
intentos = 0

while numero_elegido != numero_aleatorio:
    if numero_elegido < numero_aleatorio:
        print('Busca un numero mas grande')
        intentos = intentos + 1
        numero_elegido = int(input('Elige otro numero: '))
        
        
    if numero_elegido > numero_aleatorio:
        print('Busca un numero mas pequeño')
        intentos = intentos + 1
        numero_elegido = int(input('Elige otro numero: '))
        
        
    if numero_elegido == numero_aleatorio:
        intentos = intentos + 1
        print(f"Congratulations. Total try: {intentos}")
 
   