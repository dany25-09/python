from data.silla import Silla

class Masajeadora(Silla):
    def __init__(self, referencia, precio, calificacion):
        super().__init__(referencia, precio, calificacion)

    def removerDelCatalogo(self):
        pass

    def __str__(self):
        return 'Masejeadora' + '\t' + super().__str__()