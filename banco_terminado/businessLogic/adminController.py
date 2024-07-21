from data.cancelTransaction import CancelTransaction
from userInterface.ui import UI

class AdminController():
    def __init__(self, ui, bank):
        self._ui = ui
        self._bank = bank

    def controller(self):
        while True:
            self._ui.showMenuAdmin()
            action = self._ui.askOption()
            if action == 'a':
                self._ui.showMessage('*** Abrir Cuenta ***')
                clientId = self._ui.askUserId()
                clientName = self._ui.askUserName()
                startingBalance = self._ui.askAccountBalance()
                accountPassword = self._ui.askAccountPassword()
                try:
                    newAccountId = self._bank.openAccount(clientId, clientName, startingBalance, accountPassword)
                except CancelTransaction as error:
                    self._ui.showMessage(error)
                    continue
                self._ui.showMessage('La nueva cuenta es: ' + newAccountId)
                continue
            if action == 'm':
                self._ui.showMessage('*** Mostrar Cuentas ***')
                self._bank.showAccounts()
                continue
            if action == 't':
                break
            self._ui.showMessage('Opción no valida. Intente de nuevo.')