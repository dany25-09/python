from nodo import Nodo

class Stack():
    def __init__(self):
        self.top = None     #Me indica que hay en el tope de la pila
        self.size = 0   #Tamaño de la pila


    def push(self, elemento):
        node = Nodo(elemento)

        if self.size == 0:
            self.top = node

        else:
            node.next = self.top
            self.top = node
        self.size = self.size + 1


    def pop(self):
        if self.size == 0:
            return None

        else:
            elemento = self.top.data
            self.top = self.top.next
            self.size = self.size - 1
            return (elemento)

    def peek(self):
        if self.size == 0:
            return None
        else:
            return self.top.data


    def Imprimir(self):
        elemento = self.top
        while elemento is not None:
            print(elemento.data)
            elemento = elemento.next



# pila = Stack()
# pila.push(1)
# pila.push(2)
# # pila.pop()
# pila.Imprimir()