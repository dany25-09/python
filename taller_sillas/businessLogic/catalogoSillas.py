from data.gerencial import Gerencial
from data.presidencial import Presidencial
from data.secretarial import Secretarial
from data.tandem import Tandem
from data.masajeadora import Masajeadora
from data.ruedas import Ruedas

class CatalogoSillas:
    def __init__(self, archivo):
        self._archivo = archivo
        self._sillas = []

    def getSillas(self):
        return self._sillas

    def crearSillas(self):
        with open(self._archivo, 'r') as info:
            for line in info:
                self._sillas.append(self.crearSilla(line.split(",")))

    def crearSilla(self, record):
        record = list(map(lambda x: x.strip(), record))
        if record[1] == 'Presidencial':
            return Presidencial(record[0], float(record[2]), float(record[3]), record[4])
        if record[1] == 'Gerencial':
            return Gerencial(record[0], float(record[2]), float(record[3]))
        if record[1] == 'Secretarial':
            return Secretarial(record[0], float(record[2]), float(record[3]))
        if record[1] == 'Tandem':
            return Tandem(record[0], float(record[2]), float(record[3]))
        if record[1] == 'Ruedas':
            return Ruedas(record[0], float(record[2]), float(record[3]))
        if record[1] == 'Masajeadora':
            return Masajeadora(record[0], float(record[2]), float(record[3]))
        return None

    def status(self):
            for silla in self.getSillas():
                if silla.removerDelCatalogo() == "Mantener" or silla.removerDelCatalogo() == "Remover":
                    print(silla.getReferencia() + '\t' + silla.removerDelCatalogo())

    def mostrarCategoria(self, cat):
        if cat == 'p':
            return [s for s in self._sillas if type(s).__name__ == 'Presidencial']
        if cat == 'g':
            return [s for s in self._sillas if type(s).__name__ == 'Gerencial']
        if cat == 's':
            return [s for s in self._sillas if type(s).__name__ == 'Secretarial']
        if cat == 'a':
            return [s for s in self._sillas if type(s).__name__ == 'Tandem']
        if cat == 'r':
            return [s for s in self._sillas if type(s).__name__ == 'Ruedas']
        if cat == 'm':
            return [s for s in self._sillas if type(s).__name__ == 'Masajeadora']