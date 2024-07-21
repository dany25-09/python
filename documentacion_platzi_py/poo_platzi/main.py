from car import Car
from account import Account

if __name__ == "__main__":
    print("Hola Mundo")

    car = Car("AMS234", Account("Andres Herrera", "ANDA876"), 3)
    print(vars(car))
    print(vars(car.driver))
    car3 = Car
    car2 = Car("QWE567", Account("Martha García", "456789"), 4)
    print(vars(car2))
    print(vars(car2.driver))

    # car = Car()
    # car.license = "AMS234"
    # car.driver = "Andres Herrera"
    # print(vars(car))
    #
    # car2 = Car()
    # car2.license = "QWE567"
    # car2.driver = "Martha García"
    # print(vars(car2))