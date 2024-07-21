from interface.user_interface import UI
from business_logic.memory import Memory


if __name__ == '__main__':
    print("[APP]: Start Running ... ")

    m = Memory("./clients.txt")

    app = UI(m)
    app.mainloop()