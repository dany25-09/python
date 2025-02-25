from nodo_bidireccion import Nodo_bidireccion

# class Nodo():
#     def __init__(self, data, next = None):
#         self.data = data                #El valor que almacena el nodo
#         self.next = next                

# class Nodo_bidireccion(Nodo):
#     def __init__(self, data, next=None, prev=None):
#         super().__init__(data, next)
#         self.prev = prev


class Double_linked_list():
    def __init__(self):
        self.head = None  #Apuntador hacia la cabeza
        self.tail = None   #Apuntador hacia la cola
        self.size = 0   #tamaño
        

    def pushback(self, element):
        new_node = Nodo_bidireccion(element)

        if self.size == 0:
            self.head = new_node
            self.tail = new_node

        else:
            new_node.prev = self.tail   #el apuntador prev del nuevo nodo apunta al último nodo de la lista(ahora es el penultimo)
            self.tail.next = new_node   #el apuntador next del pentultimo apunta al new_node que ahora es el ultimo
            self.tail = new_node    #El nuevo nodo pasa a ser el ultimo en la lista(oficialmente)

        self.size = self.size + 1


    def pushfront(self, element):
        new_node = Nodo_bidireccion(element)

        if self.size == 0:
            self.head = new_node
            self.tail = new_node

        else:
            new_node.next = self.head   #el apuntador next del nuevo nodo apunta a la cabeza (que ahora sería el segundo nodo)
            self.head.prev = new_node   #ahora el prev del que es el segundo nodo apunta al nuevo nodo que es el primero
            self.head = new_node    #El nuevo nodo pasa a ser el primero en la lista(oficialmente)

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
        print(element)



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
        print(element)



    def Imprimir(self):
        if self.size == 0:
             print("La lista se encuentra vacía")
        else:
             actual_nodo = self.head
             while actual_nodo is not None:
                 print(actual_nodo.data)
                 actual_nodo = actual_nodo.next



# lista1 = Double_linked_list()
# lista1.create_list()
# lista1.Imprimir()
