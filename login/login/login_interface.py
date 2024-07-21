import tkinter as tk
from tkinter import ttk as ttk
from login.user import User


window = tk.Tk()
name_user = tk.StringVar()
pass_user = tk.StringVar()


def User_login():

    window.title("Login Usuario")

        #Frame principal
    main_frame = tk.Frame(window)
    main_frame.pack(
        side = tk.TOP,
        fill = tk.BOTH,
        expand = True,)
    main_frame.configure(widt = 480, height = 320, background = "white")

    #Textos y titulos
    log_tittle = tk.Label(main_frame, text = "Login De Usuario")
    log_tittle.grid(column = 0, row = 0, padx = 10, pady = 10, columnspan = 2)


    log_name = tk.Label(main_frame, text = "Nombre: ")
    log_name.grid(column = 0, row = 1)

    log_pass = tk.Label(main_frame, text = "Contraseña: ")
    log_pass.grid(column = 0, row = 2)


    #Entradas de texto
    # name_user = tk.StringVar()
    name_user.set("")
    name_entry = tk.Entry(main_frame, textvariable = name_user )
    name_entry.grid( column = 1, row = 1 )

    # pass_user =  tk.StringVar()
    pass_user.set("")
    pass_entry = tk.Entry(main_frame, textvariable = pass_user, show = "*" )
    pass_entry.grid(column = 1, row = 2)

    #Botones

    start_btn = ttk.Button(main_frame, text = "Iniciar Sesion", command = login)
    start_btn.grid(column = 1, row = 3, ipadx = 5, ipady = 5, padx = 10, pady = 10)


    register_btn = ttk.Button(main_frame, text = "Registrar", command = register_user)
    register_btn.grid(column = 0, row = 3, ipadx = 5, ipady = 5, padx = 10, pady = 10)

    window.mainloop()

def login():
    user1.connect(name_user.get())

def register_user():
    pass

if __name__ == '__main__':
    print("[APP]: Start Running ... ")
    user1 = User("Daniel", "1234")
    User_login()