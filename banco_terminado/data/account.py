from data.cancelTransaction import CancelTransaction

class Account():
    def __init__(self, id, balance, password):
        self._id = id
        self._balance = self._validateAmount(balance)
        self._password = password

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, newId):
        pass

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, newBalance):
        if newBalance > 0:
            self._balance = newBalance

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, newPassword):
        self._password = newPassword

    def _validateAmount(self, amount):
        try:
            amount = int(amount)
        except ValueError:
            raise CancelTransaction('La cantidad debe ser un entero')
        if amount < 0:
            raise CancelTransaction('La cantidad debe ser positiva')
        return amount

    def passwordMatch(self, password):
        return password == self._password

    def deposit(self, amountToDeposit):
        amountToDeposit = self._validateAmount(amountToDeposit)
        self._balance = self._balance + amountToDeposit
        return self._balance

    def getBalance(self):
        return self._balance

    def withdraw(self, amountToWithdraw):
        amountToWithdraw = self._validateAmount(amountToWithdraw)
        if amountToWithdraw > self._balance:
            raise CancelTransaction('Fondos insuficientes para este retiro')
        self._balance = self._balance - amountToWithdraw
        return self._balance

    def __str__(self):
        return '\nNúmero: ' + self._id + '\n' + 'Saldo: ' + str(
            self._balance) + '\n' + 'Contraseña: ' + self._password + '\n'