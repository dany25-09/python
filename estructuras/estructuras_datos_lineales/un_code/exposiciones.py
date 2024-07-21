#Exposiciones.

class Nodo():
    def __init__(self, data, next = None):
        self.data = data                #El valor que almacena el nodo
        self.next = next

class Nodo_bidireccion(Nodo):
    def __init__(self, data, next=None, prev=None):
        super().__init__(data, next)
        self.prev = prev


class Double_linked_list():
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def pushback(self, element):
        new_node = Nodo_bidireccion(element)

        if self.size == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

        self.size = self.size + 1


    def popback(self):
        if self.size == 0:
            return None

        element = self.tail.data

        if self.size == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None

        self.size = self.size - 1
        return element



    def popfront(self):
        if self.size == 0:
            return None

        element = self.head.data

        if self.size == 1:
            self.head = None
            self.tail = None

        else:
            self.head = self.head.next
            self.head.prev = None

        self.size = self.size - 1
        return element

    def create_list(self):
        apellidos = input("Ingrese los apellidos separados por espacios: ").split()
        for apellido in apellidos:
            lista.pushback(apellido)

    def final_list(self, lista):
        new_list = Double_linked_list()
        while lista.size > 1:
            primer_elemento = lista.popfront()
            ultimo_elemento = lista.popback()
            new_list.pushback(primer_elemento)
            new_list.pushback(ultimo_elemento)

        # Si queda un elemento en la lista original, se agrega al final de la nueva lista
        if lista.size == 1:
            new_list.pushback(lista.popfront())

        new_list.Imprimir()

    def Imprimir(self):
        if self.size == 0:
            print("La lista se encuentra vacía")
        else:
            actual_nodo = self.head
            while actual_nodo is not None:
                print(actual_nodo.data, end=" ")
                actual_nodo = actual_nodo.next
            print()



# lista = Double_linked_list()
# lista.create_list()
# # lista.popfront()
# print("Lista original:")
# lista.Imprimir()
# print("Nueva lista:")
# lista2 =Double_linked_list()
# lista2.final_list(lista)
