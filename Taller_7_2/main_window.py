import tkinter as tk

class Main_window(tk.Text):

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller


