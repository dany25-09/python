from car import Car


class uberpool(Car):
    brand = str
    model = str

    def __init__(self, lincense, driver, brand, model):
        super.__init__(license, driver)
        self.brand = brand
        self.model = model