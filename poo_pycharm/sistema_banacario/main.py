from client import Client
from account import Account

if __name__ == "__main__":

    lista = []
    lista_2 = []
    i = 0

    def mostrar():
        j = 0
        while j < len(lista):
            print(f"El nombre del usuario {j +1} es: {lista[j].name}")
            print(f"El número de documento del usuario {j +1} es: {lista[j].cedula}")

            j = j + 1

    def mostrar_2():
        k = 0
        while k < len(lista_2):
            print(f"El número de cuenta del usuario es: {lista_2[k].id}")
            print(f"La cantidad de dinero en la cuenta es: {lista_2[k].balance}")
            print(f"la clave de la cuenta es: {lista_2[k].password}")
            k = k + 1

    while i == 0:
        print("-----" * 20)
        print("  -------- BANCO NACIONAL -------  ")
        print("-----" * 20)
        print("¿Que operación quieres hacer?")
        print("Para abrir una nueva cuenta, digite 1" )
        print("Para mostrar todas las cuentas, digite 2")
        print("Para salir del programa, digite 3")
        print("")
        opcion = int(input("Ingresa algún número para acceder a su respectiva función: "))
        if opcion == 1:
            print("** Abrir Cuenta **")
            cliente_x = Client(input("Ingrese su nombre: "), input("Ingrese su cédula: "))
            lista.append(cliente_x)
            cliente_x_a = Account(input("Ingrese su número de cuenta: "), int(input("Cantidad de dinero en la cuenta: ")), input("ingrese su contraseña: "))
            # lista_2.append(cliente_x_a)
        if opcion == 2:
            print("** Mostrar Cuentas **")
            mostrar()
            print("-----" * 20)
            # mostrar_2()
        elif opcion == 3:
            print("** Usted Ha Salido Del Programa **")
            exit()



