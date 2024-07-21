import tkinter as tk
from esthetic import colors

class Show_client(tk.Frame):
    def __init__(self, parent, controller, memory):
        super().__init__(parent)
        self.memory = memory
        self.controller = controller
        self.configure(background=colors.COMPONENT)
        self.canvas = tk.Canvas(self, bg=colors.COMPONENT)
        self.sc = tk.Scrollbar(
            self, orient='vertical', command=self.canvas.yview
        )
        self.sc.pack(side='right', fill=tk.Y)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.frame = tk.Frame(self.canvas, bg=colors.COMPONENT)

        self.frame.bind(
            '<Configure>',
            lambda _: self.canvas.configure(
                scrollregion=self.canvas.bbox('all')
            ),
        )
        self.canvas.create_window((0, 0), window=self.frame, anchor='nw')

        self.canvas.config(yscrollcommand=self.sc.set)
        self.canvas.configure(yscrollcommand=self.sc.set)

        self.widgets()

    def move_home(self):
        self.controller.show_frame(self.controller.Home)

    def widgets(self):
        try:
            data = self.memory.getData()
        except:
            tk.Label(
                master=self.frame,
                text='No Hay Usuarios Creados',
                justify=tk.CENTER,
                **colors.STYLE
            ).pack(fill=tk.Y, expand=0, padx=22, pady=11)
            data = None

        if data:
            for i in range(0, len(data)):
                user = data[i]
                title = tk.Label(
                    self.frame,
                    text='Usuario ' + str(i + 1),
                    justify=tk.CENTER,
                    **colors.STYLE
                )
                title.pack(fill=tk.Y, pady=13)
                name = tk.Label(
                    self.frame,
                    text='Nombre: ' + user['name'],
                    justify=tk.CENTER,
                    **colors.STYLE
                )
                name.pack(fill=tk.Y, pady=13)
                last_name = tk.Label(
                    self.frame,
                    text='Apellido: ' + user['last_name'],
                    justify=tk.CENTER,
                    **colors.STYLE
                )
                last_name.pack(fill=tk.Y, pady=13)
                id = tk.Label(
                    self.frame,
                    text='Número de documento: ' + user['id'],
                    justify=tk.CENTER,
                    **colors.STYLE
                )
                id.pack(fill=tk.Y, pady=13)
                phone = tk.Label(
                    self.frame,
                    text='Número de Telefono: ' + user['phone'],
                    justify=tk.CENTER,
                    **colors.STYLE
                )
                phone.pack(fill=tk.Y, pady=13)
                days = tk.Label(
                    self.frame,
                    text='Días De Hospedaje: ' + user['days'],
                    justify=tk.CENTER,
                    **colors.STYLE
                )
                days.pack(fill=tk.Y, pady=13)

        register = tk.Button(
            self.frame, **colors.STYLE, text='Regresar', command=self.move_home
        )
        register.pack(fill=tk.Y, padx=150, pady=13)
