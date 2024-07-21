import pickle


class Memory():
    def __init__(self, name):
        self.name = name

    def open(self):
        self.file = open(self.name, "rb+")

    def getData(self):
        self.open()
        data = pickle.load(self.file)
        self.close()

        return data

    def saveData(self, data):
        self.open()
        pickle.dump(data, self.file)
        self.close()

    def close(self):
        self.file.close()