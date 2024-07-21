class Dose():

    def __init__(self, application_date, maker, lote, place_application, nurse_applied):
        self.application_date   = application_date
        self.maker              = maker
        self.lote               = lote
        self.place_application  = place_application
        self.nurse_applied      = nurse_applied

    def show_info(self):
        print(f"Fecha de aplicación: {self.application_date}")
        print(f"fabricante: {self.maker}")
        print(f"lote: {self.lote}")
        print(f"lugar de aplicación: {self.place_application}")
        print(f"Nombre enfermera: {self.nurse_applied}")


