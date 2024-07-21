import tkinter as tk
import functions




def open_about():
    nuevo = tk.Tk()
    nuevo.minsize(300, 200)
    nuevo.title("datos creadores")

    new_lb = tk.Label(master = nuevo,
    font = ("NORMAL", 10),
    text=   "AUTORES: Carlos Daniel García \n Jose Sebastian Alarcon. \n"
            "CORREOS: cagarciach@unal.edu.co \n joalarconb@unal.edu.co. \n"
            "VERSION: 1.0.",
    fg="DeepSkyBlue2",
    bg="black",
    width=10,
    height=10

    ).pack( side=tk.TOP, fill=tk.BOTH, expand=True)

class Buttons_frame(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.configure(background = "Gray")
        self.controller = controller
        self.init_widgets()

    def init_widgets(self):
        btn_open = tk.Button(self, text="Open", command=functions.open_file, bg="cyan")
        btn_save = tk.Button(self, text="Save As...", command=functions.save_file, bg="cyan")
        btn_about = tk.Button(self, text="About", command=open_about, bg="cyan")

        btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
        btn_save.grid(row=1, column=0, sticky="ew", padx=5)
        btn_about.grid(row=2, column=0, sticky="ew", padx=5)