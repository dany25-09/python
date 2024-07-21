class metodo_lista():
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.lista = []
        self.contador = 0


    def push_back(self,elemento):
        if self.capacidad == self.contador:
            return "Error"
        else:
            print(self.contador)
            self.lista = self.lista + [elemento]
            self.contador = self.contador + 1
            return self.lista


    def pop_back(self):
        if self.contador == 0:
            return "Vacío"
        else:
            self.lista  = self.lista[:-1]
            self.contador = self.contador - 1
            return self.lista


# lista = metodo_lista(4)
# print(lista.push_back(1))
# print(lista.push_back(2))
# print(lista.push_back(3))
# print(lista.push_back(4))
# print(lista.push_back(5))
# print(lista.pop_back())