from nodo import Nodo

class Linked_list():
    def __init__(self):
        self.head = None #apuntador a la cola de la lista
        self.size = 0   #Tamaño de la lista


    def pushback(self, element):    #Agregar atrás
        new_node = Nodo(element)

        if self.head == None:    #Si la lista está vacía
            self.head = new_node

        else:
            actual_nodo = self.head #Me indica mi posicion actual en la lista

            while actual_nodo.next is not None:    #Mientras el ultimo nodo no apunte a none
                actual_nodo = actual_nodo.next    #Recorre la lista enlazada

            actual_nodo.next = new_node    #el puntero del ultímo nodo pasa a ser el penultimo y apunta al nodo creado

        self.size = self.size + 1   #Aumenta el tamaño de la lista


    def pushfront(self, element):
        new_node = Nodo(element)

        if self.size == 0:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

        self.size = self.size + 1



    def popback(self):
        if self.head is None:
            try:
                print("Error, la lista está vacía")
            except:
                pass

        elif self.size == 1:  # si hay un solo elemento en la lista
            pop = self.apr #Guardo el nodo que quiero eliminar
            self.head = None
            self.size = self.size - 1
            return pop.data

        else:
            actual_nodo = self.head

            while actual_nodo.next.next is not None: # mientras no haya nada después del penúltimo nodo
                actual_nodo = actual_nodo.next

            pop = actual_nodo.next  # se guarda el último nodo
            actual_nodo.next = None  # elimina el puntero que apunta al último nodo
            self.size = self.size - 1
            return pop.data


    def Imprimir(self):
        if self.size == 0:
            print("La lista se encuentra vacía")
        else:
            actual_nodo = self.head
            while actual_nodo is not None:
                print(actual_nodo.data)
                actual_nodo = actual_nodo.next


# lista_enlazada = Linked_list()
# lista_enlazada.pushback(1)
# lista_enlazada.pushback(2)
# lista_enlazada.pushfront(3)
# lista_enlazada.Imprimir()
# print()
# print()
# lista_enlazada.popback()
# print()
# lista_enlazada.Imprimir()