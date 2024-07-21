from data.silla import Silla


class Presidencial(Silla):
    def __init__(self, referencia, precio, nota, esImportada):
        super().__init__(referencia, precio, nota)
        self._esImportada = esImportada

    def removerDelCatalogo(self):
        if self._esImportada == 'si' and (self._nota < 3.5 or self._precio > 400000):
            return "Remover"
        return "Mantener"

    def __str__(self):
        return 'Presidencial' + '\t' + super().__str__() + '\t' + 'Importada?: ' + self._esImportada