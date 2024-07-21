import sys
sys.path.insert(0, "C:/Users/dany2/Documents/Programación/Python/estructuras")
from estructuras_datos_lineales.estructuras_lineales.nodo_bidireccion import Nodo_bidireccion

class Queue():
    def __init__(self):
        self.head =  None
        self.tail = None
        self.count = 0  #Conteo de nodos que hay en la queue


    def push(self, element):
        new_node = Nodo_bidireccion(element)

        if self.head is None:
            self.head = new_node
            self.tail = new_node

        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

        self.count += 1

    def pop(self):
        if self.head is None:
            self.tail = None # Si la cabeza queda vacía, también actualizamos la cola
            return None  # Si la cola está vacía, devolvemos None

        else:
            node = self.head  # Obtenemos el nodo que vamos a eliminar
            self.head = self.head.next  # Actualizamos la cabeza de la cola
            self.count -= 1

        return node.data
    
    
    def peek(self):
        if self.count == 0:
            return None
        else:
            return self.head.data
    

    def Imprimir(self):
        if self.count == 0:
             print("La lista se encuentra vacía")
        else:
             actual_nodo = self.head
             while actual_nodo is not None:
                 print(actual_nodo.data)
                 actual_nodo = actual_nodo.next

# cola = Queue()
# cola.push(1)
# cola.push(2)
# cola.push(3)
# cola.pop()
# cola.Imprimir()