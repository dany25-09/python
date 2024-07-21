class Nodo():
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Linked_list():
    def __init__(self):
        self.head = None
        self.size = 0
        self.negative_values = None
        self.positive_values = None

    def pushback(self, element):
        new_node = Nodo(element)

        if self.head == None:
            self.head = new_node

        else:
            actual_nodo = self.head

            while actual_nodo.next is not None:
                actual_nodo = actual_nodo.next

            actual_nodo.next = new_node

        self.size = self.size + 1

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
                print("Error, la lista está vacía", end="")
            except:
                pass

        elif self.size == 1:
            pop = self.head
            self.head = None
            self.size = self.size - 1
            return pop.data

        else:
            actual_nodo = self.head

            while actual_nodo.next.next is not None:
                actual_nodo = actual_nodo.next

            pop = actual_nodo.next
            actual_nodo.next = None
            self.size = self.size - 1
            return pop.data

    def peek(self):
        if self.size == 0:
            return None
        else:
            return self.head.data

    def create_list(self):

        precios_str = input("ingrese los robots: ").split()
        precios = [int(p) for p in precios_str]

        self.negative_values = Linked_list()
        self.positive_values = Linked_list()
        for precio in precios:
            if precio < 0:
                valor_abs = abs(precio)
                self.negative_values.pushback(valor_abs)

            if precio > 0:
                self.positive_values.pushfront(precio)

    def comparacion(self):
        final_list = Linked_list()

        node1 = self.positive_values.head
        node2 = self.negative_values.head


        while node1 is not None and node2 is not None:
            try:
                if node1.data > node2.data:
                    node2 = node2.next

                if node1.data == node2.data:
                    # print("No quedaron robots!")
                    node1 = node1.next
                    node2 = node2.next

                elif node1.data < node2.data:
                    node1 = node1.next
            except:
                pass

        if node1 is not None:
            while node1 is not None:
                final_list.pushfront(node1.data)
                node1 = node1.next

        elif node2 is not None:
            while node2 is not None:
                # negativo = -1 * (node2.data)
                final_list.pushback(-node2.data)
                node2 = node2.next

        if final_list.size == 0:
            print("No quedaron robots!", end = "")

        else:
            final_list.Imprimir()

    def Imprimir(self):
        if self.size == 0:
            print("La lista se encuentra vacía")
        else:
            actual_nodo = self.head
            primer_elemento = True
            while actual_nodo is not None:
                impresion = actual_nodo.data
                if primer_elemento:
                    primer_elemento = False
                    print(impresion, end="")
                else:
                    print(" " + str(impresion), end="")
                actual_nodo = actual_nodo.next


# lista = Linked_list()
# lista.create_list()
# lista.comparacion()
