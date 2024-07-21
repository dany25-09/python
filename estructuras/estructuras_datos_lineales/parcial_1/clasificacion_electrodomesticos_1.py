# class Nodo():
#     def __init__(self, data, next=None):
#         self.data = data
#         self.next = next


# class Nodo_bidireccion(Nodo):
#     def __init__(self, data, next=None, prev=None):
#         super().__init__(data, next)
#         self.prev = prev


# class Queue():
#     def __init__(self):
#         self.head = None
#         self.tail = None
#         self.size = 0
#         self.sublistas = []

#     def push(self, element):
#         new_node = Nodo_bidireccion(element)

#         if self.head is None:
#             self.head = new_node
#             self.tail = new_node

#         else:
#             new_node.prev = self.tail
#             self.tail.next = new_node
#             self.tail = new_node

#         self.size += 1

#     def crear_cola(self):
#         n_elementos = int(input("Número de electrodomesticos: "))
#         electrodomesticos = input("Electrodomesticos: ").split()

#         for electrodomestico in electrodomesticos:
#             self.push(electrodomestico)

#         if self.size != n_elementos:
#             print("Error")
#             exit()
#         else:
#             pass

#     def reparto(self):
#         n_tiendas = int(input("Tiendas a repartir: "))
#         rep_productos = input("Productos por tienda: ").split()
#         tam_rep_productos = 0

#         for i in rep_productos:
#             tam_rep_productos += 1

#         if n_tiendas != tam_rep_productos:
#             print("El numero de tiendas y la repartición no coinciden")
#         else:

#             list_elec = []
#             node1 = self.head

#             while node1 is not None:
#                 list_elec = list_elec + [node1.data]
#                 node1 = node1.next

#             pro_tienda = []
#             for elemento in rep_productos:
#                 pro_tienda = pro_tienda + [(int(elemento))]

#             self.sublistas = [[] for i in pro_tienda]

#             for i, elementos in enumerate(pro_tienda):
#                 self.sublistas[i] = list_elec[:elementos]
#                 list_elec = list_elec[elementos:]

#             global electrodomesticos
#             for sublista in self.sublistas:
#                 electrodomesticos = electrodomesticos + [sublista]


# numero_veces = int(input("Número de veces que se ejecuta el programa: "))
# electrodomesticos = []

# for i in range(numero_veces):
#     cola = Queue()
#     cola.crear_cola()
#     cola.reparto()

# for i, electrodomestico in enumerate(electrodomesticos):
#     if i == len(electrodomesticos) - 1:
#         print("[{}]".format(" ".join(electrodomestico)), end='')
#     else:
#         print("[{}]".format(" ".join(electrodomestico)))
print(2+2)