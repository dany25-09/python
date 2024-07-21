class Client():
    def __init__(self, name, cedula):
        self._name = name
        self._cedula = cedula
        self._accounts = []

        # ENCAPSULAMIENTO NAME

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        pass

    # ENCAPSULAMIENTO CEDULA
    @property
    def cedula(self):
        return self._cedula

    @cedula.setter
    def id(self, new_cedula):
        pass

