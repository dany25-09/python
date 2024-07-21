import tkinter as tk
from esthetic import colors

class Home(tk.Frame):

  def __init__(self, parent, controller, _):
    super().__init__(parent)
    self.configure(background=colors.BACKGROUND)
    self.controller = controller
    self.widgets()


  def move_register(self):
        self.controller.show_frame(self.controller.Register)

  def move_show_client(self):
        self.controller.show_frame(self.controller.Show_client)

  def widgets(self):

    tk.Label(master=self,
             text="Bienvenido al programa de Gestión Hotelera",
             justify=tk.CENTER,
             **colors.STYLE).pack(side=tk.TOP,
                                  fill=tk.BOTH,
                                  expand=True,
                                  padx=22,
                                  pady=11)

    options_frame = tk.Frame(master=self, background=colors.COMPONENT)
    options_frame.pack(side=tk.TOP,
                       fill=tk.BOTH,
                       expand=True,
                       padx=22,
                       pady=11)

    tk.Label(master=options_frame,
             text="Elige que opción deseas realizar",
             justify=tk.CENTER,
             **colors.STYLE).pack(side=tk.TOP, fill=tk.X, padx=22, pady=11)

    register = tk.Button(master=options_frame,
                         **colors.STYLE,
                         text="Registrar",
                        command = self.move_register)
    register.pack(side=tk.LEFT, fill=tk.X, padx=150, pady=13, expand=True)

    ver_clientes = tk.Button(master=options_frame,
                             **colors.STYLE,
                             text="Ver Clientes",
                             command =
                             self.move_show_client)
    ver_clientes.pack(side=tk.LEFT, fill=tk.X, padx=250, pady=13, expand=True)