import tkinter as tk
from business_logic.home import Home
from data.register import Register
from business_logic.show_client import Show_client


class UI(tk.Tk):

    def __init__(self, memory=0):
        super().__init__()
        self.title("Sistema Gestor De Hoteles")
        self.minsize(500, 500)
        icon = tk.PhotoImage(file="esthetic/hotel.png")
        self.iconphoto(True, icon)

        self.Home = Home
        self.Register = Register
        self.Show_client = Show_client

        if memory == 0:
            print("error")
        else:
            self.memory = memory

        # frame principal
        frame_pr = tk.Frame(master=self)
        frame_pr.pack(
            side=tk.TOP,
            fill=tk.BOTH,
            expand=True,
        )
        frame_pr.configure(background="black", width=200)

        frame_pr.grid_columnconfigure(0, weight=1)
        frame_pr.grid_rowconfigure(0, weight=1)

        # Creo un diccionario que me guarde las clases de frames
        self.frames = {}
        for F in (Home, Register, Show_client):
            frame = F(frame_pr, self, memory)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky=tk.NSEW)
        self.show_frame(Home)

    def show_frame(self, container):
        frame = self.frames[container]
        frame.tkraise()  # Manda el frame al frente de todo

