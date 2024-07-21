import sys
sys.path.insert(0, "C:/Users/dany2/Documents/Programación/Python/estructuras")
from estructuras_datos_lineales.estructuras_lineales.nodo import Nodo

class Nodo():
    def __init__(self, data, next = None):
        self.data = data                #El valor que almacena el nodo
        self.next = next                

class Nodo_bidireccion(Nodo):
    def __init__(self, data, next=None, prev=None):
        super().__init__(data, next)
        self.prev = prev  # Apuntador al nodo anterior

