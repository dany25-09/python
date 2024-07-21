import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename


def open_file():
    """Open a file for editing."""
    filepath = askopenfilename(
        title = "Text Pro – Open a file",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    txt_edit.delete("1.0", tk.END)
    with open(filepath, mode="r", encoding="utf-8") as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END, text)
    window.title(f"TextPro-Open a file - {filepath}")


def save_file():
    """Save the current file as a new file."""
    filepath = asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )
    if not filepath:
        return
    with open(filepath, mode="w", encoding="utf-8") as output_file:
        text = txt_edit.get("1.0", tk.END)
        output_file.write(text)
    window.title(f"TextPro Editor - {filepath}")

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

window = tk.Tk()
window.title("TextPro Editor")
icon = tk.PhotoImage(file="hoja.png")
window.iconphoto(True, icon)



window.rowconfigure(0, minsize=500, weight=1)
window.columnconfigure(1, minsize=500, weight=1)


txt_edit = tk.Text(window)
frm_buttons = tk.Frame(window, relief=tk.RAISED, bd=2, bg="Gray")

btn_open = tk.Button(frm_buttons, text="Open", command=open_file, bg="cyan")
btn_save = tk.Button(frm_buttons, text="Save As...", command=save_file, bg="cyan")
btn_about = tk.Button(frm_buttons, text="About", command = open_about, bg="cyan")

btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=1, column=0, sticky="ew", padx=5)
btn_about.grid(row=2, column=0, sticky="ew", padx=5)


frm_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")




window.mainloop()


