from io import open

class wordProcessor:

    def __init__(self, opinions):
        self.opinions = opinions
        self.wordDic = {}

    def calculateFrequency(self, word):
        mayus = word.upper()
        count = 0
        total_words = 0
        for opinions in self.opinions:
            word_list = opinions.split(" ")
            for w in word_list:
                if w == "":
                    continue
                total_words += 1
                if w == mayus:
                    count += 1
        return round((count/total_words)*100, 2)
    
    def calculateRelevance(self, word):
        mayus = word.upper()
        count = 0
        for opinions in self.opinions:
            word_list = opinions.split(" ")
            if mayus in word_list:
                count += 1
        return count

    def addWord(self, word):
        self.wordDic[word] = (self.calculateFrequency(word), self.calculateRelevance(word))
    
    def calculateStatics(self):
        for opinion in self.opinions:
            words = opinion.split(" ")
            for word in words:
                if word == "":
                    continue
                self.addWord(word)

    def writeStatistics(self):
        abc = 'abcdefghijklmnñopqrstvwxyz'
        output = open('output.txt', 'w', encoding='utf-8')
        sorted_k = sorted(list(self.wordDic.keys()))
        for key in sorted_k:
            output.write(f"{key}, {self.wordDic[key][0]}, {self.wordDic[key][1]}\n")
        output.close()
        