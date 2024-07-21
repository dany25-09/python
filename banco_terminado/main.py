from data.account import Account
from data.client import Client
from data.bank import Bank
from userInterface.ui import UI
from businessLogic.adminController import AdminController
from businessLogic.clientController import ClientController

from businessLogic.bankSerializer import BankSerializer

print('Probando un serializador')
bank = Bank("cliente 1", "cuenta 1")
# bank.openAccount()
ui = UI()
# admin = AdminController(ui, bank)
# admin.controller()
client=ClientController(ui,bank)
client.controller()