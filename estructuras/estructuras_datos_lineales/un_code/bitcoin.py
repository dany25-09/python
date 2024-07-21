class Nodo():
    def __init__(self, data, next=None):
        self.data = data  # El valor que almacena el nodo
        self.next = next


class Nodo_bidireccion(Nodo):
    def __init__(self, data, next=None, prev=None):
        super().__init__(data, next)
        self.prev = prev  # Apuntador al nodo anterior


class Queue():
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0  # Conteo de nodos que hay en la queue

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
            self.tail = None  # Si la cabeza queda vacía, también actualizamos la cola
            return None  # Si la cola está vacía, devolvemos None

        else:
            node = self.head  # Obtenemos el nodo que vamos a eliminar
            self.head = self.head.next  # Actualizamos la cabeza de la cola
            self.count -= 1

        return node.data

    def create_queue(self):
        precios_str = input("lista de precios: ").split()
        precios = [int(p) for p in precios_str]
        for precio in (precios):
            self.push(precio)

    def peek(self):
        if self.count == 0:
            return None
        else:
            print(self.head.data)

    def dias_espera(self):
        dias = Queue()
        cabeza = self.head
        dias_esperar = 0  # Inicializamos la variable que usaremos para contar los días a esperar
        dias_max = self.count - 1 #3 2

        while cabeza is not None:
            valor_act = cabeza.next
            while valor_act is not None:
                if cabeza.data < valor_act.data:
                    # print("holi")
                    dias_esperar = dias_esperar + 1
                    # print(dias_esperar)
                    # print()
                    dias.push(dias_esperar)
                    dias_max = self.count - 1
                    dias_esperar = 0
                    break

                elif cabeza.data > valor_act.data:
                    # print("entro")
                    dias_esperar = dias_esperar + 1
                    # print(dias_esperar)
                    if dias_max == dias_esperar and valor_act.next is None:
                        dias.push(0)
                        dias_esperar = 0
                        dias_max = dias_max - 1
                        break
                    else:
                        valor_act = valor_act.next


            cabeza = cabeza.next

        dias.push(0)

        dias.Imprimir()

    def Imprimir(self):
        if self.count == 0:
            print("La lista se encuentra vacía")
        else:
            actual_nodo = self.head
            while actual_nodo is not None:
                print(actual_nodo.data, end=" ")
                actual_nodo = actual_nodo.next


# cola = Queue()
# cola.create_queue()
# cola.Imprimir()
# print()
# cola.dias_espera()
