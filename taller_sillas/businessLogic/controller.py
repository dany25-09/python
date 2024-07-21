import sys

class Controller():
    def __init__(self, ui, catalogo):
        self._ui = ui
        self._catalogo = catalogo

    def loop(self):
        self._ui.bienvenida()
        while True:
            self._ui.mostrarMenu()
            opc = self._ui.pedirOpcion()
            if opc == 'c':  # Show chairs by category
                self._ui.mostrarMenuSillas()
                cat = self._ui.pedirOpcion()
                lst = self._catalogo.mostrarCategoria(cat)
                while (cat != "p") and (cat !="g") and (cat !="s") and (cat !="a") and (cat !="r") and (cat !="m") and (cat !="t"):
                    self._ui.mostrarMensaje('Opción no valida. Intente de nuevo.')
                    self._ui.mostrarMenuSillas()
                    cat = self._ui.pedirOpcion()
                lst = self._catalogo.mostrarCategoria(cat)
                for s in lst:
                    self._ui.mostrarMensaje(s)
                continue
            if opc == 's':  # Show the status of each chair
                self._ui.mostrarMensaje('***** STATUS DE LAS SILLAS *****')
                self._catalogo.status()
                continue
            if opc == 't':
                self._ui.mostrarMensaje('Sesión finalizada.')
                break

            self._ui.mostrarMensaje('Opción no valida. Intente de nuevo.')