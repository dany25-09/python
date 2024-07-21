from data.cancelTransaction import CancelTransaction


class ClientController():

    def __init__(self, ui, bank):
        self._ui = ui
        self._bank = bank

    def controller(self):
        clientId = self._ui.askUserId()
        while True:

            self._ui.showMenuClient()
            action = self._ui.askOption()

            if action == 't':
                break

            accountId = self._ui.askAccountId()
            accountPassword = self._ui.askAccountPassword()
            account = self._bank.validateAccount(accountId, accountPassword)

            if action == 's':
                try:
                    self._ui.showMessage('*** Obtener Saldo ***')
                    self._bank.getBalanceAccount(account)
                except CancelTransaction as error:
                    self._ui.showMessage(error)
                    continue
                continue

            if action == 'c':
                try:
                    self._ui.showMessage('*** Consignación ***')
                    depositAmount = self._ui.askDepositAmount()
                    self._bank.accountDeposit(depositAmount, account)
                except CancelTransaction as error:
                    self._ui.showMessage(error)
                    continue
                continue

            if action == 'r':
                try:
                    self._ui.showMessage('*** Retiro ***')
                    withdrawAmount = self._ui.askWithdrawAmount()
                    self._bank.accountWithdraw(withdrawAmount, account)
                except CancelTransaction as error:
                    self._ui.showMessage(error)
                    continue
                continue

            self._ui.showMessage('Opción no valida. Intente de nuevo.')