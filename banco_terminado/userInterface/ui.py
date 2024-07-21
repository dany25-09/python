# This class implements the user interface

class UI():
    def welcome(self):
        print()
        print('------- BANCO NACIONAL -------')

    def askUserId(self):
        userId = input('¿Cuál es el número de identificación del cuentahabiente?: ')
        return userId

    def askUserName(self):
        userName = input('¿Cuál es el nombre del cuentahabiente?: ')
        return userName

    def askAccountId(self):
        accountPass = input('¿Cuál es el número de la cuenta?: ')
        return accountPass

    def askAccountPassword(self):
        accountPass = input('¿Cuál es la contraseña de la cuenta?: ')
        return accountPass

    def askDepositAmount(self):
        depositAmount = input('Ingrese el monto de la consignación: ')
        return depositAmount

    def askWithdrawAmount(self):
        withdrawAmount = input('Ingrese el monto del retiro: ')
        return withdrawAmount

    def askTransfererAccountId(self):
        transfererAccountId = input('Ingrese el ID de la cuenta a la que desea transferir: ')
        return transfererAccountId

    def askTransfererAmount(self):
        transfererAmount = input('Ingrese el monto a transferir: ')
        return transfererAmount

    def askAccountBalance(self):
        initialBalance = input('¿Cuál es el saldo inicial para esta cuenta? ')
        return initialBalance

    def askOption(self):
        action = input('¿Qué operación quiere hacer? ')
        return action

    def showMenuAdmin(self):
        print()
        print('Para abrir una nueva cuenta, digite a')
        print('Para mostrar todas las cuentas, digite m')
        print('Para terminar, digite t')

    def showMenuClient(self):
        print()
        print('Para obtener el saldo, digite s')
        print('Para consignar, digite c')
        print('Para retirar, digite r')
        print('Para terminar, digite t')

    def showMessage(self, msg):
        print()
        print(msg)