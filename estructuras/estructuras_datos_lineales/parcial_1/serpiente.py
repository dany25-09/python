class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

def createBinaryTree(input_data):
    values = []
    for value in input_data:
        values = values + [int(value)]

    # Crear nodo raíz
    root = Node(values[0])

    # Utilizar una lista para realizar un seguimiento de los nodos pendientes de procesar
    queue = [root]
    i = 1

    while i < len(values):
        current_node = queue.pop(0)

        # Asignar el nodo izquierdo si hay un valor disponible
        if values[i] is not None:
            left_node = Node(values[i])
            current_node.left = left_node
            queue = queue + [left_node]
            # queue.append(left_node)
        i += 1

        # Asignar el nodo derecho si hay un valor disponible
        if i < len(values) and values[i] is not None:
            right_node = Node(values[i])
            current_node.right = right_node
            queue = queue + [right_node]
            # queue.append(right_node)
        i += 1


def zizagtraversal(root, calorias):
    if root is None:
        return

    current_level = []
    next_level = []
    lista_zigzag = []
    lista_calorias = []
    direction = True 

    current_level = current_level + [root]

    while len(current_level) > 0:
        delete = current_level.pop(-1)
        # print(delete.data, " ", end="")
        lista_zigzag = lista_zigzag + [delete.data]

        if direction:
            if delete.left:
                next_level = next_level + [delete.left]
            if delete.right:
                next_level = next_level + [delete.right]
        else:
            if delete.right:
                next_level = next_level + [delete.right]
            if delete.left:
                next_level = next_level + [delete.left]

        if len(current_level) == 0:
            direction = not direction
            current_level, next_level = next_level, current_level
    
    for numero in range(0, len(lista_zigzag), 2):
        lista_calorias = lista_calorias + [lista_zigzag[numero]]
    # print(lista_zigzag)
    # print(lista_calorias)
    suma_calorias = sum(lista_calorias)
    # print(suma_calorias)
    
    if suma_calorias >= calorias:
        print("Sobrevive", end="")
    else: 
        print("Muere", end="")

# Obtener la entrada del usuario
input_data = input("Ingrese los valores del árbol separados por espacios: ").split()
calorias = int(input("Calorias minimas: "))

# Crear el árbol binario a partir de la entrada del usuario
root = createBinaryTree(input_data)

zizagtraversal(root, calorias)
