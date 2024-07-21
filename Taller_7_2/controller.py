import tkinter as tk
from buttons_frame import Buttons_frame
from main_window import Main_window

class Controller(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("TextPro Editor")
        self.minsize(800, 500)
        icon = tk.PhotoImage(file="hoja.png")
        self.iconphoto(True, icon)

        self.rowconfigure(0, minsize=500, weight=1)
        self.columnconfigure(1, minsize=500, weight=1)

        container = tk.Frame( master = self, background = "Gray")
        container.pack(
            side = tk.TOP,
            fill = tk.BOTH,
            expand = True
        )
        container.grid_columnconfigure(0, weight = 1)
        container.grid_rowconfigure(0, weight = 1)


        frame = Buttons_frame(container, self)
        frame_2 = Main_window(container, self)
        frame.grid(row=0, column=0, sticky=tk.NSEW)
        frame_2.grid(row=0, column=1, sticky=tk.NS)











