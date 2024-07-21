from data.account import Account
from data.client import Client
from userInterface.ui import UI


class Bank():
    def __init__(self, clients, accounts):
        self._clients = clients
        self._accounts = accounts

    def getClients(self):
        return self._clients

    def getAccounts(self):
        return self._accounts

    def openAccount(self, clientId, clientName, startingAmount, accountPassword):
        for client in self.getClients():
            # print(f"{client._id} == {clientId}: {client._id == clientId}")
            if client._id == clientId:
                newAccountId = str(len(client._accountIds) + 1)
                account = Account(newAccountId, startingAmount, accountPassword)
                client.addAccount(newAccountId)
                self._accounts.append(account)
                return newAccountId
        else:
            newClient = Client(clientId, clientName)
            account = Account('1', startingAmount, accountPassword)
            self._accounts.append(account)
            self._clients.append(newClient)
            newClient.addAccount('1')
            return '1'

    def showAccounts(self):
        for account in self.getAccounts():
            print(account, end='\n')

    def validateAccount(self, accountId, accountPassword):
        try:
            for account in self.getAccounts():
                if account._id == accountId and account._password == accountPassword:
                    return account
        except CancelTransaction as error:
            self._ui.showMessage(error)

    def getBalanceAccount(self, account):
        Balance = account.getBalance()
        print(f"El saldo es: {Balance}")

    def accountDeposit(self, amountToDeposit, account):
        account.deposit(amountToDeposit)
        print(f"Cantidad depositada: {amountToDeposit}")
        print(f"Su nuevo saldo: {account.getBalance()}")

    def accountWithdraw(self, amountToWithdraw, account):
        account.withdraw(amountToWithdraw)
        print(f"Cantidad retirada: {amountToWithdraw}")
        print(f"Su nuevo saldo: {account.getBalance()}")