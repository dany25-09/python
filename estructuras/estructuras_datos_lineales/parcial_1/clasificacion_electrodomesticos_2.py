class Nodo():
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Nodo_bidireccion(Nodo):
    def __init__(self, data, next=None, prev=None):
        super().__init__(data, next)
        self.prev = prev


class Queue():
    # datos_globales = []
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0  # Conteo de nodos que hay en la queue
        self.sublistas = []
        self.sublista = []

    def push(self, element):
        new_node = Nodo_bidireccion(element)

        if self.head is None:
            self.head = new_node
            self.tail = new_node

        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

        self.size += 1

    def pop(self):
        if self.head is None:
            self.tail = None  # Si la cabeza queda vacía, también actualizamos la cola
            return None  # Si la cola está vacía, devolvemos None
        else:
            node = self.head  # Obtenemos el nodo que vamos a eliminar
            self.head = self.head.next  # Actualizamos la cabeza de la cola
            self.size -= 1
        return node.data

    def create_queue(self, n_elementos, electrodomesticos, n_tiendas, rep_productos):

        self.sublista = self.sublista + [n_elementos]

        for electrodomestico in electrodomesticos:
            self.push(electrodomestico)

        if self.size != n_elementos:
            # print(n_elementos)
            # print(self.size)
            print("Error")
            exit()
        else:
            # self.Imprimir()

            tam_rep_productos = 0
            self.sublista = self.sublista + [n_tiendas]
            self.sublista = self.sublista + [rep_productos]

            for i in rep_productos:
                tam_rep_productos += 1

            if n_tiendas != tam_rep_productos:
                print("El numero de tiendas y la repartición no coinciden")
            else:

                list_elec = []
                node1 = self.head

                while node1 is not None:
                    list_elec = list_elec + [node1.data]
                    node1 = node1.next

                # print(list_elec)
                self.sublista = self.sublista + [list_elec]  # Lista de todas las entradas

                pro_tienda = []
                for elemento in rep_productos:
                    pro_tienda = pro_tienda + [(int(elemento))]

                # print(pro_tienda)
                # Creamos las sublistas vacías
                self.sublistas = [[] for i in pro_tienda]
                # print(self.sublistas)

                # Agrega los elemtos a las sublistas
                for i, elementos in enumerate(pro_tienda):
                    self.sublistas[i] = list_elec[:elementos]
                    list_elec = list_elec[elementos:]
                # print(self.sublistas)

                # #SALTO DE LINEA TODAS LAS LINEAS
                # for i,elemento in enumerate(self.sublistas):
                #         print("[{}]".format(" ".join(elemento)))
                # else
                global datos_globales
                for elemento in self.sublistas:
                    datos_globales.append(elemento)

    def Imprimir(self):
        if self.size == 0:
            print("La lista se encuentra vacía")
        else:
            actual_nodo = self.head
            while actual_nodo is not None:
                print(actual_nodo.data)
                actual_nodo = actual_nodo.next


def operar(arreglo):
    # print(arreglo)
    for i in arreglo:
        n_elementos = (i[0])
        elementos = (i[1])
        tiendas = (i[2])
        pro_por_tienda = (i[3])
        cola = Queue()
        cola.create_queue(n_elementos, elementos, tiendas, pro_por_tienda)
    # cola.Immprimir_sublistas2()


num_veces = int(input("Número de veces que se ejecuta el programa: "))

# Ejecutar el procedimiento la cantidad de veces especificada
datos_globales = []
operar_datos = []

for i in range(num_veces):
    datos = []
    n_elementos = int(input("Número de electrodomesticos: "))
    electrodomesticos = input("Electrodomesticos: ").split()
    n_tiendas = int(input("Tiendas a repartir: "))
    rep_productos = input("Productos por tienda: ").split()

    datos = datos + [n_elementos]
    datos = datos + [electrodomesticos]
    datos = datos + [n_tiendas]
    datos = datos + [rep_productos]
    operar_datos = operar_datos + [datos]
# x = operar(operar_datos)

# # print(datos_globales)
# for i, dato in enumerate(datos_globales):
#     if i == len(datos_globales) - 1:
#         print("[{}]".format(" ".join(dato)), end='')
#     else:
#         print("[{}]".format(" ".join(dato)))
