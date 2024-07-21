from data.silla import Silla


class Secretarial (Silla):
    def __init__(self, referencia, precio, calificacion):
        super().__init__(referencia, precio, calificacion)

    def removerDelCatalogo(self):
        if self._nota < 3 or self._precio > 200000:
            return "Remover"
        return "Mantener"

    def __str__(self):
        return 'Secretarial' + '\t' + super().__str__()