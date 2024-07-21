import sys
sys.path.insert(0, "C:/Users/dany2/Documents/Programación/Python/estructuras")
from estructuras_datos_lineales.estructuras_lineales.queue import Queue

from collections import deque

class node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

Q = deque()

# Helper function helps us in adding data
# to the tree in Level Order
def insertValue(data, root):
    newnode = node(data)
    if Q:
        temp = Q[0]
    if root == None:
        root = newnode
        
    # The left child of the current Node is
    # used if it is available.
    elif temp.left == None:
        temp.left = newnode
    
    # The right child of the current Node is used
    # if it is available. Since the left child of this
    # node has already been used, the Node is popped
    # from the queue after using its right child.
    elif temp.right == None:
        temp.right = newnode
        atemp = Q.popleft()
    
    # Whenever a new Node is added to the tree,
    # its address is pushed into the queue.
    # So that its children Nodes can be used later.
    Q.append(newnode)
    return root

# Function which calls add which is responsible
# for adding elements one by one
def createTree(a, root):
    for i in range(len(a)):
        root = insertValue(a[i], root)
    return root

# Function for printing level order traversal
# def levelOrder(root, order_list):
#     Q = deque()
#     Q.append(root)
#     while Q:
#         temp = Q.popleft()
#         order_list.append(temp.data)
#         if temp.left != None:
#             Q.append(temp.left)
#         if temp.right != None:
#             Q.append(temp.right)

# Function for printing Preorder traversal
def preorder(root, order_list):
    if root:
        order_list.append(root.data)
        preorder(root.left, order_list)
        preorder(root.right, order_list)

# Function for printing Inorder traversal
def inorder(root, order_list):
    if root:
        inorder(root.left, order_list)
        order_list.append(root.data)
        inorder(root.right, order_list)

# Function for printing Postorder traversal
def postorder(root, order_list):
    if root:
        postorder(root.left, order_list)
        postorder(root.right, order_list)
        order_list.append(root.data)


#Funcion para quitar -1 del arreglo
def arreglo_a_sumar(arr):
    return [num for num in arr if num != -1]    

#Funcion para cierta cantidad de elementos
def sum_elements(arr, num_elements):
    return sum(arr[:num_elements])

def maximo(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3



# Driver Code
# a = [4, 20, 10, -1, 16, 4, 0]
# numero_de_nodos = 4

a_str = input("Agregar: ").split()
a = [int (p) for p in a_str]

numero_de_nodos = int(input("#Nodos: "))

root = None
root = createTree(a, root)
preorderlist = []
inorderlist = []
postorderlist = []

# print("Level Order")
# levelOrder(root)

# print("\nPreorder")
preorder(root,preorderlist)

# arreglo = [4, 20, -1, 16, 10, 4, 0 ]
# print(preorderlist)
sumar1 = arreglo_a_sumar(preorderlist)
sumapreorder = sum_elements(sumar1,numero_de_nodos)
# print(arreglosinmenos1)

# print("\nInorder")
inorder(root,inorderlist)

sumar2 = arreglo_a_sumar(inorderlist)
sumainorder = sum_elements(sumar2,numero_de_nodos)

# print("\nPostorder")
postorder(root,postorderlist)

sumar3 = arreglo_a_sumar(postorderlist)
sumapostorder = sum_elements(sumar3,numero_de_nodos)

#COMPARAR LAS SUMAS

mejor_orden = maximo(sumapreorder, sumainorder, sumapostorder)

# Imprimimos el resultado según el mejor orden
if mejor_orden == sumapreorder:
    print("Preorder",sumapreorder,end="")
elif mejor_orden == sumainorder:
    print("Inorder",sumainorder,end="")
else:
    print("Postorder",sumapostorder,end="")

# print("Preorder",sumapreorder)          #Impresion Final
# print("Inorder",sumainorder)          #Impresion Final
# print("Postorder",sumapostorder)          #Impresion Final