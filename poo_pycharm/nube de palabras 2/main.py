from OpinionsReader import *
from WordProcessor import wordProcessor


opiniones = opinionsReader("opinions.txt", "stopWords.txt")

opiniones.readStopWords()
opiniones.readOpinions()

wproc = wordProcessor(opiniones.getOpinions())

wproc.calculateStatics()
wproc.writeStatistics()

