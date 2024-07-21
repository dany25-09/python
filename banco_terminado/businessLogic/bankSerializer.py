# this class saves a dictionary or loads it from a file
# https://machinelearningmastery.com/a-gentle-introduction-to-serialization-for-python/
import pickle

class BankSerializer():
    def pickling(self, dct, fileName):
        path = 'resources/' + fileName
        with open(path, "wb") as f:
            pickle.dump(dct, f)

    def unpickling(self, fileName):
        path = 'resources/' + fileName
        try:
            with open(path, "rb") as f:
                dct = pickle.load(f)
        except FileNotFoundError:
            dct = {}
        return dct