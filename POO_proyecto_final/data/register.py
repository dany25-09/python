import tkinter as tk
from esthetic import colors


class Register(tk.Frame):

  def __init__(self, parent, controller, memory):
    super().__init__(parent)
    self.memory = memory
    self.configure(background=colors.COMPONENT)
    self.controller = controller
    self.widgets()

  def move_home(self):
    self.controller.show_frame(self.controller.Home)

  def registrar(self):
    name = self.name.get()
    last_name = self.last_name.get()
    id = self.id_entry.get()
    phone = self.phone_entry.get()
    days = self.days_entry.get()

    user = {
      "name": name,
      "last_name": last_name,
      "id": id,
      "phone": phone,
      "days": days
    }

    try:
      data = self.memory.getData()
    except:
      self.memory.saveData([])
      data = []

    data.append(user)
    self.memory.saveData(data)

  def limpiar(self):
    self.name.set("")
    self.last_name.set("")
    self.id_entry.set("")
    self.phone_entry.set("")
    self.days_entry.set("")

  def widgets(self):

    # Titulo
    tittle_ = tk.Label(
      master=self,
      text=
      "Registrar cliente \n Precios: \n Habitación Sencilla: 80.000$",
      justify=tk.CENTER,
      **colors.STYLE)
    tittle_.grid(column=0, row=0, padx=10, pady=10, columnspan=2)
    # tittle_.pack()
    # tittle_.grid_columnconfigure(0, weight=20, minsize=75)
    # tittle_.grid_rowconfigure(0, weight=20, minsize=50)

    # datos
    # Nombre
    name = tk.Label(self, text="Nombre: ", **colors.STYLE)
    name.grid(column=0, row=1, sticky="w")
    name.grid_columnconfigure(0, weight=1, minsize=75)
    name.grid_rowconfigure(0, weight=1, minsize=50)

    name_user = tk.StringVar()
    name_entry = tk.Entry(self, textvariable=name_user, width=40)
    name_entry.grid(column=0, row=1, sticky="w", padx=300)
    name_entry.grid_columnconfigure(0, weight=1, minsize=75)
    name_entry.grid_rowconfigure(0, weight=1, minsize=50)

    self.name = name_user

    # Apellido
    last_name = tk.Label(self, text="Apellido: ", **colors.STYLE)
    last_name.grid(column=0, row=2, sticky="w")
    last_name.grid_columnconfigure(0, weight=1, minsize=75)
    last_name.grid_rowconfigure(0, weight=1, minsize=50)

    last_name_user = tk.StringVar()
    last_name_entry = tk.Entry(self, textvariable=last_name_user, width=40)
    last_name_entry.grid(column=0, row=2, sticky="w", padx=300)
    last_name_entry.grid_columnconfigure(0, weight=1, minsize=75)
    last_name_entry.grid_rowconfigure(0, weight=1, minsize=50)

    self.last_name = last_name_user

    # Documento
    id = tk.Label(self, text="Número de documento: ", **colors.STYLE)
    id.grid(column=0, row=3, sticky="w")
    id.grid_columnconfigure(0, weight=1, minsize=75)
    id.grid_rowconfigure(0, weight=1, minsize=50)

    id_user = tk.StringVar()
    id_entry = tk.Entry(self, textvariable=id_user, width=40)
    id_entry.grid(column=0, row=3, sticky="w", padx=300)
    id_entry.grid_columnconfigure(0, weight=1, minsize=75)
    id_entry.grid_rowconfigure(0, weight=1, minsize=50)

    self.id_entry = id_user

    # Número telefono
    phone = tk.Label(self, text="Número de Telefono: ", **colors.STYLE)
    phone.grid(column=0, row=4, sticky="w")
    phone.grid_columnconfigure(0, weight=1, minsize=75)
    phone.grid_rowconfigure(0, weight=1, minsize=50)

    phone_user = tk.StringVar()
    phone_entry = tk.Entry(self, textvariable=phone_user, width=40)
    phone_entry.grid(column=0, row=4, sticky="w", padx=300)
    phone_entry.grid_columnconfigure(0, weight=1, minsize=75)
    phone_entry.grid_rowconfigure(0, weight=1, minsize=50)

    self.phone_entry = phone_user

    # Días de hospedaje
    days = tk.Label(self, text="Días De Hospedaje: ", **colors.STYLE)
    days.grid(column=0, row=5, sticky="w")
    days.grid_columnconfigure(0, weight=1, minsize=75)
    days.grid_rowconfigure(0, weight=1, minsize=50)

    days_user = tk.StringVar()
    days_entry = tk.Entry(self, textvariable=days_user, width=40)
    days_entry.grid(column=0, row=5, sticky="w", padx=300)
    days_entry.grid_columnconfigure(0, weight=1, minsize=75)
    days_entry.grid_rowconfigure(0, weight=1, minsize=50)

    self.days_entry = days_user

    # Botones

    btn_register = tk.Button(master=self,
                             text="Registrar",
                             **colors.STYLE,
                             command=self.registrar)
    btn_register.grid(column=0, row=6, sticky="w")

    btn_clear = tk.Button(master=self,
                          text="Limpiar",
                          **colors.STYLE,
                          command=self.limpiar)
    btn_clear.grid(column=0, row=6, sticky="w", padx=150)

    btn_return = tk.Button(master=self,
                           text="Regresar",
                           **colors.STYLE,
                           command=self.move_home)
    btn_return.grid(column=0, row=6, sticky="w", padx=300)