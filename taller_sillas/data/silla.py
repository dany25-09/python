from abc import abstractmethod


class Silla:
    def __init__(self, referencia, precio=0, nota=0.0):
        self._referencia = referencia
        self._precio = int(precio)
        self._nota = float(nota)

    def getReferencia(self):
        return self._referencia

    @abstractmethod
    def removerDelCatalogo(self):
        pass

    def __str__(self):
        return 'Ref.: ' + self._referencia + '\t' + '$: ' + str(self._precio) + '\t' + 'Nota: ' + str(self._nota)



