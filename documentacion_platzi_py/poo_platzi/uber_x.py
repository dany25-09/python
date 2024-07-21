from car import Car

class uberx(Car):
    brand   = str
    model   = str

    def __init__(self, lincense, driver, brand, model):
        super.__init__(license, driver)
        self.brand  = brand
        self.model  = model
