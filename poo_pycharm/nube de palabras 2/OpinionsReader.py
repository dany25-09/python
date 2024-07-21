from io import open

class opinionsReader:

    def __init__(self, opinionsFile, stopWordsFile):
        self.opinionsFile = opinionsFile
        self.stopWordsFile = stopWordsFile
        self.opinions = []
        self.stopWords = set()

    def getOpinions(self):
        return self.opinions

    def getStopWords(self):
        return self.stopWords

    def readStopWords(self):
        stopWords_read = open(self.stopWordsFile, 'r', encoding='utf-8')
        words = stopWords_read.read().split(", ")
        for word in words:
            self.stopWords.add(word.upper())
        stopWords_read.close()

    def readOpinions(self):
        opinions_read = open(self.opinionsFile, 'r', encoding='utf-8')
        opinions = opinions_read.read().split("\n")
        u_opinions = []
        for i in opinions:
            if i == "":
                opinions.remove("")
        for i in opinions:
            u_opinions.append(i.upper().replace("¿", "").replace("?", "").replace(",", ""))
        for i in u_opinions:
            words = i.split(" ")
            n_string = ""
            for word in words:
                if word in self.stopWords:
                    continue
                n_string += word + " "
            self.opinions.append(n_string)
        opinions_read.close()
