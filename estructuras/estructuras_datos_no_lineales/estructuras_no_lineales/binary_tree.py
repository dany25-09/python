class Node():
    def __init__(self, data, right = None, left = None):
        self.data = data                #El valor que almacena el nodo
        self.right = right
        self.left = left


    def insert(self, data):
        if self.data is not None:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            if data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right = Node(data)
        else:
            self.data = data


    def print_tree(self):
      if self.left:
         self.left.print_tree()
      print(self.data),
      if self.right:
         self.right.print_tree()
         
                
root = Node(12)
root.insert(14)
root.insert(6)
root.insert(3)
root.insert(7)
root.print_tree()