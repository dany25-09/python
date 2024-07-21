class Nodo():
    def __init__(self, data, next=None):
        self.data = data  # El valor que almacena el nodo
        self.next = next


class Linked_list():
    def __init__(self):
        self.head = None  # apuntador a la cola de la lista
        self.size = 0  # Tamaño de la lista

    def pushback(self, element):  # Agregar atrás
        new_node = Nodo(element)

        if self.head == None:  # Si la lista está vacía
            self.head = new_node

        else:
            actual_nodo = self.head  # Me indica mi posicion actual en la lista

            while actual_nodo.next is not None:  # Mientras el ultimo nodo no apunte a none
                actual_nodo = actual_nodo.next  # Recorre la lista enlazada

            actual_nodo.next = new_node  # el puntero del ultímo nodo pasa a ser el penultimo y apunta al nodo creado

        self.size = self.size + 1

    def create_list(self):
        cantidad_com = int(input("Número de Competencias exigidas: "))
        new_list = input("Competencias: ").split()
        aptitudes = []

        for var in new_list:
            self.pushback(int(var))

        if self.size != cantidad_com:
            print("error")

        else:
            node1 = self.head
            while node1 is not None:
                aptitudes = aptitudes + [int(node1.data)]
                node1 = node1.next

            postulates = int(input("Número postulados: "))
            count_pos = 0
            elected = 0
            postulados_skills = []

            while postulates > count_pos:
                skills_pos = input("Habilidades postulados: ").split()
                enlazada = Linked_list()

                for var in skills_pos:
                    enlazada.pushback(int(var))

                node1 = enlazada.head
                skills = []
                while node1 is not None:
                    skills = skills + [int(node1.data)]
                    node1 = node1.next

                postulados_skills = postulados_skills + [skills]

                count_pos += 1

            for lista in postulados_skills:
                contiene_todos = True
                for elemento in aptitudes:
                    if elemento not in lista:
                        contiene_todos = False
                        break
                if contiene_todos:
                    elected += 1
            print(elected, end="")


# lista = Linked_list()
# lista.create_list()