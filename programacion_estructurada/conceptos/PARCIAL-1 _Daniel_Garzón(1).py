# !/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Escribir un programa en python usando funciones por cada accion 
diferente que evalue e imprima si una frase dada es palindroma 
o no indicando al final cuantas vocales contiene la frase dada 
frase_1= "AnITa Lava lA TINA"
frase_2= "Ella te dará detalle"
'''

x='''
--------------------------------------------
| Daniel Felipe Garzón Mora C.C:1000494735 |
--------------------------------------------
'''

def mayusculas(frase):
    return frase.upper()

def quitar_espacios(frase):
    return frase.strip().replace(" ","")

def quitar_tildes(frase):
    frase_1=frase
    frase_1=frase_1.replace("Á","A")
    frase_1=frase_1.replace("É","E")
    frase_1=frase_1.replace("Í","I")
    frase_1=frase_1.replace("Ó","O")
    frase_1=frase_1.replace("Ú","U")
    return frase_1

def verificador_palindromo(frase):
    cadena_reves=frase[::-1]
    if cadena_reves==frase: return "es palindroma"
    else: return "no es palindroma"

def contador_de_vocales(frase):
    frase_1 = frase
    contador = 0
    for i in range(len(frase_1)):
        if (
        frase[i] == "A" or 
        frase[i] == "E" or 
        frase[i] == "I" or 
        frase[i] == "O" or 
        frase[i] == "U"):
            contador=contador+1
    return contador

def main():

    frase_1="Ella te dará detalle" # AQUI ESTA LA FRASE 

    print("La frase ingresada es: ",frase_1)
    frase_1=quitar_espacios(frase_1)
    frase_1=mayusculas(frase_1)
    frase_1=quitar_tildes(frase_1)
    print(f"La frase ingresada {verificador_palindromo(frase_1)}")
    print(f"El numero de vocales de la frase es: {contador_de_vocales(frase_1)}")
    print(x)
    pass

if __name__ == "__main__":
    main()