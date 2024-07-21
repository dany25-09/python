class User():

    num_users = 0

    def __init__(self, name, password):
        self.name   = name
        self.password = password

        self.conectado = False
        self.intentos = 3

        User.num_users += 1


    def connect(self, clave = None):
        if clave == None:
            my_pass = input("Ingrese su contraseña: ")
        else:
            my_pass == clave
        if my_pass == self.password:
            print("Se ha conectado con éxito")
            self.conectado = True
        else:
            self.intentos -= 1
            if self.intentos > 0:
                print("Contraseña incorrecta, intentelo de vuelta")
                print(f"intentos restantes {self.intentos}")
                self.connect()
            else:
                print("Error, no se pudo iniciar sesión, Adios")


    def disconnect(self):
        if self.conectado:
            print("Se cerró sesión con éxito")
            self.conectado = False
        else:
            print("Error, no inició sesión")

    def __str__(self):
        if self.conectado:
            conn = "conectado"
        else:
            conn = "desconectado"

        return f"Mi nombre de usuario es {self.name} y estoy {conn}"