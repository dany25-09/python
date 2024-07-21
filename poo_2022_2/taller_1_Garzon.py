
import array

#ejercicio 1
def decimalToBin(n):
    if n<0:
        return "n<0"
    
    binario = 0
    i = 0

    while n>0:
        digito  = n%2
        n = int(n//2)
        binario = binario+digito*(10**i)
        i = i+1 
    return str(binario)

#ejercicio 2 
def tiketsCost(ages):
    total=0
    for i in ages:
        if i>=62:
            total+=18000
        elif 13<=i<62:
            total+=25000
        elif 2<i<13:
            total+=14000
        elif 0<=i<=2:
            total+=0
        else:
            return "age<0"
    return total

#ejercicio 3
def yearToAnimal(year):
        modulo =(year%12)
        print(modulo)
        if year<0:return "año<0"
        elif modulo==0:return "Mono"
        elif modulo==1:return "Gallo"
        elif modulo==2:return "Perro"
        elif modulo==3:return "Cerdo"
        elif modulo==4:return "Rata"
        elif modulo==5:return "Buey"
        elif modulo==6:return "Tigre"
        elif modulo==7:return "Liebre"
        elif modulo==8:return "Dragón"
        elif modulo==9:return "Serpiente"
        elif modulo==10:return "Caballo"
        elif modulo==11:return "Oveja"
        
#ejercicio 4
def Fibonacci(i):
    if i == 0:
        return 0
    elif i == 1 or i == 2:
        return 1
    else:
        return Fibonacci(i-1) + Fibonacci(i-2)
def isFibonacci(n):
    i=0
    for i in range(0,30):#limite de 30 primeros numeros
        if n==Fibonacci(i):
            return True
        i+1
    return False

# #ejercicio 5
def shapeType(n):
    if n==3: return "triángulo"
    elif n==4: return "cuadrilátero"
    elif n==5: return"pentágono"
    elif n==6: return"hexágono"
    elif n==7: return"heptágono"
    elif n==8: return"octágono"
    elif n==9: return"eneágono"
    elif n==10: return"decágono"
    else: return "None"

#ejercicio 6
def isStrongPassword(password):
    simbolos =['$', '@', '#', '%'] 
    validacion = True
          
    if len(password) < 8 or (" " not in password): 
        validacion = False
    cont=4
    if not any(char.isdigit() for char in password):cont=cont-1  
    if not any(char.isupper() for char in password):cont=cont-1
    if not any(char.islower() for char in password):cont=cont-1
    if not any(char in simbolos for char in password): cont=cont-1
    if cont>=3:validacion=True
    else:validacion=False


    if validacion: return validacion
    else:return False

#ejercicio 7
def median(a,b,c):
    array=[a,b,c]
    organizado=sorted(array)
    return organizado[1]

#ejercicio 8
def aproximatePI(n):
    multiplicador=0
    if n>=1:
        for i in range(2,n+1):
            multiplicador+=(pow(-1,i)*4)/((i*2)*(i*2-1)*(i*2-2))
        return 3+multiplicador
    else: return "n<1"


# #ejercicio 9
# def randomPassword(size)

# #ejercicio 10
# def daysInMonth(m,y)



def main():
    while True:
        continuar=input("¿desea probar otro ejercicio? ingrese Y o N:")
        if continuar=="N" or continuar=="n" :
            break
        else:
            menu="""\nmenu de ejercicios:
                1.decimal a binario
                2.costos de tiketes
                3.zodiaco chino
                4.n pertenece a fibonacci
                5.lados de la figura
                6.Validador de contraseña
                7.mediana de 3 numeros
                8.aproximacion de pi
                0.salir(cualquier tecla)\n"""
            opc=int(input(menu))
            if opc==1:
                n=int(input("Ejercicio 1(decimal a binario):\nn= "))
                print(f"bin= {decimalToBin(n)}")
            elif opc==2:
                ages=[]
                numero_personas=int(input("Ejercicio 2(costos de tiketes):\nNumero de personas="))
                print("ingrese sus edades:")
                for i in range(numero_personas):
                    ages.append(int(input(f"persona {i+1}=")))
                print(f"valor Total= {tiketsCost(ages)}")
            elif opc==3:
                print(yearToAnimal(int(input("Ejercicio 3(zodiaco chino):\nAño de nacimiento:"))))
            elif opc==4:
                print(isFibonacci(int(input("Ejercicio 4(n pertenece a fibonacci):\nIngrese numero para saber si cooresponde fibonacci: "))))
            elif opc==5:
                print(shapeType(int(input("Ejercicio 5(lados de la figura):\nIngrese numero de lados de la figura:"))))
            elif opc==6:
                print(isStrongPassword(input("Ejercicio 6(validar contraseña):\nIngrese contraseña: ")))
            elif opc==7:
                a=int(input("Ejercicio 7(mediana de 3 numeros):\nn1= "))
                b=int(input("n2= "))
                c=int(input("n3= "))
                print(median(a,b,c))
            elif opc==8:
                print(aproximatePI(int(input("Ejercicio 8(aproximacion de pi):\nn= "))))
            else:break

    pass

if __name__ == "__main__":
    main()