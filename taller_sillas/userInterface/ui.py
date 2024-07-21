class UI():
    def bienvenida(self):
        print()
        print('-------  FABRICA DE SILLAS -------')

    def mostrarMenu(self):
        print()
        print('Para ver sillas por categoría, digite c')
        print('Para ver qué sillas salen del catálogo, digite s')
        print('Para terminar, digite t')

    def pedirOpcion(self):
        return input('¿Qué opción desea? ')

    def mostrarMenuSillas(self):
        print()
        print('Para ver sillas presidenciales, digite p')
        print('Para ver sillas gerenciales, digite g')
        print('Para ver sillas secretariales, digite s')
        print('Para ver sillas Tandem, digite a')
        print('Para ver sillas de Ruedas, digite r')
        print('Para ver sillas Masajeadoras, digite m')
        print('Para terminar, digite t')

    def mostrarMensaje(self, msg):
        print()
        print(msg)