# class Opinions_reader():
#   def __init__(self, opinions_file, stop_words_file):
#     self.opinions_file = opinions_file
#     self.stop_words    = stop_words_file
#     self.opinions      = []
#     self.stop_words    = set()


#   def read_opinios(self):
#     with open("opinions_file.txt", "r") as file:
#        for i in file:
#          self.opinions.append(i)


#   def read_stop_words(self):
#     with open("stop_words", "r") as file:
#       words_file = file.read().split(",")
#       for i in words_file:
#         self.stop_words.add(i.strip())



# class Opinions_readers():
#   def __init__(self, opinions_file):
#     self.opinions_file = opinions_file
#     # self.stop_words    = stop_words_file
#     self.opinions      = []
#     self.stop_words    = set()


#   # def read_opinios(self):
#   #   with open("opinions_file.txt", "r") as file:
#   #      for i in file:
#   #        self.opinions.append(i)

#   def read_opinions(self):
#     with open("opinions_file.txt") as archive_object:
#       self.opinions = archive_object.readlines()
#         # print(self.opinions)


file_txt =("taller_nube_palabras/opinions_file.txt")



with open(file_txt,) as archive_object:
  read = archive_object.readlines()
  print(read)
  print("")
  print("")
  for i in read[:]:
    if i == "\n":
      read.remove(i)
    
  


  print(read)
 