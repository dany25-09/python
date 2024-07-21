from data.silla import Silla


class Gerencial (Silla):
    def __init__(self, referencia, precio, nota):
        super().__init__(referencia, precio, nota)

    def removerDelCatalogo(self):
        if self._nota < 4 or self._precio > 300000:
            return "Remover"
        return "Mantener"

    def __str__(self):
        return 'Gerencial' + '\t' + super().__str__()