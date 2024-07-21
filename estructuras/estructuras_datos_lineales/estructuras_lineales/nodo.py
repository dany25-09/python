class Nodo():
    def __init__(self, data, next = None):
        self.data = data                #El valor que almacena el nodo
        self.next = next                #La referencia hacia donde nos lleva el nodo

# nodo1 = Nodo("miercoles", None)
# nodo2 = Nodo("martes", nodo1)
# nodo3 = Nodo("Lunes", nodo2)

#
# head = nodo3  #nodo 3 es la cabeza porque es el primer elemento
# #
# #
# # imprimir los valores de los nodos
# while head != None:
#     print(head.data)
#     head = head.next


# apr = None
# for i in range(1,5):
#     apr = Nodo(i, apr)
#
#
# # head = None
# while apr != None:
#     print(apr.data)
#     apr = apr.next