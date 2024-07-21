# import math
# import os
# import random
# import re
# import sys
#
#
# if __name__ == '__main__':
#     N = int(input().strip())
#     if (N % 2 != 0):
#         print("Weird")
#     if (N % 2 == 0) and (2 <= N <= 5):
#         print("Not Weird")
#     if (N % 2 == 0) and (6 <= N <= 20):
#         print("Weird")
#     if (N % 2 == 0) and (20 < N):
#         print("Not Weird")

# class Person:
#     def __init__(self,initialAge, age):
#         self.age = age
#         self.initialAge = initialAge
#
#         if self.initialAge > 0:
#             self.age = self.initialAge
#         else:
#              print("Age is not valid, setting age to 0.")
#         # Add some more code to run some checks on initialAge
#
#     def amIOld(self):
#         if (self.age < 13):
#             print("You are young.")
#         if (self.age >= 13) and (age < 18):
#             print("You are a teenager.")
#         else:
#             print("You are old.")
#
#         # Do some computations in here and print out the correct statement to the console
#     def yearPasses(self, age = 1):
#         self.age = self.age + age
#         # Increment the age of the person in here
#
# t = int(input("x"))
# for i in range(0, t):
#     age = int(input("y"))
#     p = Person(age)
#     p.amIOld()
#     for j in range(0, 3):
#         p.yearPasses()
#     p.amIOld()
#     print("")







# class Person:
#     def __init__(self, initialAge):
#         self.age = None
#         self.initialAge = initialAge
#
#         if self.initialAge >= 0:
#             self.age = self.initialAge
#         if self.initialAge < 0:
#             print("Age is not valid, setting age to 0.")
#             self.age = self.initialAge
#
#         # Add some more code to run some checks on initialAge
#
#     def amIOld(self):
#
#         if (self.age < 13):
#             print("You are young.")
#         elif (self.age >= 13) and (self.age < 18):
#             print("You are a teenager.")
#         else:
#             print("You are old.")
#
#         # Do some computations in here and print out the correct statement to the console
#     def yearPasses(self):
#         self.age = self.age + 1
#         # Increment the age of the person in here

# joel = Person(-1)
# print(vars(joel))
# joel.amIOld()
#
# for i in range(0, 3):
#     joel.yearPasses()
# print(vars(joel))
# joel.amIOld()

# t = int(input("x: "))
# for i in range(0, t):
#     age = int(input("y: "))
#     p = Person(age)
#     p.amIOld()
#     for j in range(0, 3):
#         p.yearPasses()
#     p.amIOld()
#     print("")



#
# n = int(input().strip())
#
# for i in range(1, 11):
#     print(f"{n} x {i} = {n * i}")



# if __name__ == '__main__':
# n = int(input("x: ").strip())
#
# arr = list(map(int, input("y: ").rstrip().split()))
#
# while len(arr) != n:
#     # n = int(input("x: ").strip())
#     arr = list(map(int, input("y: ").rstrip().split()))
#
#
# arr_2 = arr[::-1]
# # print(arr_2)
# arr_3 = " ".join(arr_2)
# print(arr_3)
# cadena_3 = cadena_2[::-1]
# print(cadena_3)

# arr_2 = "".join(map(str, arr))
# cadena_2 = " ".join(cadena)
# cadena_3 = cadena_2[::-1]
# print(cadena_3)





# n = int(input().strip())
#
# arr = list(map(int, input().rstrip().split()))
#
# while len(arr) < n:
#     arr = list(map(int, input().rstrip().split()))
#
# arr = arr[::-1]
# arr_2 = str(arr)
#
# for i in arr_2:
#
#     if (i == "[") or (i == "]"):
#         arr_2 = arr_2.replace(i, "")
#     if (i == ","):
#         arr_2 = arr_2.replace(i, "")
#
# print(arr_2)


# diccionario = {}
#
# n = int(input())
#
# for i in range(0, n):
#     names, numbers = input().split()
#     numbers = int(numbers)
#     diccionario[names] = numbers
#
# print(diccionario)
#
# while True:
#     try:
#         name = input()
#         if diccionario.get(name):
#             num = diccionario[name]
#             print(f"{name}={num}")
#         else:
#             print("Not found")
#     except:
#         break



# def factorial_recursivo(n):
#
#     if n == 1:
#         return n
#     return n * factorial(n - 1)





# n = int(input())

# resultado = 0
# max = 0

# while n > 0:
#     if n % 2 == 1:
#         resultado += 1
#         if resultado > max:
#             max = resultado

#     else:
#         resultado = 0

#     n //= 2

# print(max)


# class Person:
#     def __init__(self, firstName, lastName, idNumber):
#         self.firstName = firstName
#         self.lastName = lastName
#         self.idNumber = idNumber
#
#     def printPerson(self):
#         print("Name:", self.lastName + ",", self.firstName)
#         print("ID:", self.idNumber)


# class Student(Person):
#
#
#     def __init__(self, firstName, lastName, idNumber, scores):
#         self.scores = scores
#         super().__init__(firstName, lastName, idNumber)
#
#
#     def printPerson(self):
#         print("Name:", self.lastName + ",", self.firstName)
#         print("ID:", self.idNumber)
#
#     def calculate(self):
#         nota = 0
#
#         for i in scores:
#             nota = nota + i
#
#         total = nota/len(self.scores)
#
#         if 90 <= total <= 100:
#             return 'O'
#         if 80 <= total < 90:
#             return 'E'
#         if 70 <= total < 80:
#             return 'A'
#         if 55 <= total < 70:
#             return 'P'
#         if 40 <= total < 55:
#             return 'D'
#         if total < 40:
#             return 'T'
#
#
# line = input("x: ").split()
# firstName = line[0]
# lastName = line[1]
# idNum = line[2]
# numScores = int(input("y: "))  # not needed for Python
# scores = list(map(int, input("z: ").split()))
# s = Student(firstName, lastName, idNum, scores)
# s.printPerson()
# print(vars(s))
# print("Grade:", s.calculate())



# import math
# import os
# import random
# import re
# import sys
#
# arr = []
#
# for _ in range(6):
#     arr.append(list(map(int, input().rstrip().split())))
#
# lista = []
#
# for i in range(len(arr[0:4])):
#     for j in range(len(arr[0:4])):
#         # print(arr[i][j])
#         sumatoria = arr[i][j] + arr[i][j + 1] + arr[i][j + 2] + arr[i + 1][j + 1] + arr[i + 2][j] + arr[i + 2][j + 1] + \
#                     arr[i + 2][j + 2]
#         lista.append(sumatoria)
# print(max(lista))




# from abc import ABCMeta, abstractmethod
# class Book(object, metaclass=ABCMeta):
#     def __init__(self,title,author):
#         self.title=title
#         self.author=author
#     @abstractmethod
#     def display(): pass
#
# #Write MyBook class
# class MyBook(Book):
#
#     def __init__(self, tittle, author, price):
#         self.price = price
#         super().__init__(title, author)
#
#     def display(self):
#         print(f"Title: {self.title}")
#         print(f"Author: {self.author}")
#         print(f"Price: {self.price}")
#
# title=input()
# author=input()
# price=int(input())
# new_novel=MyBook(title,author,price)
# # print(vars(new_novel))
# new_novel.display()



# class Difference:
#     def __init__(self, a):
#         self.__elements = a
#
#     def computeDifference(self):
#         lista_2 = []
#
#         for i in self.__elements:
#             for j in self.__elements:
#                 diferencia = abs(i - j)
#                 lista_2.append(diferencia)
#
#         lista_2 = set(lista_2)
#         self.maximumDifference = (max(lista_2))
#
# _ = input("x: ")
# a = [int(e) for e in input("y: ").split(' ')]
#
# d = Difference(a)
# # print(vars(d))
# d.computeDifference()
# print(d.maximumDifference)


# if __name__ == '__main__':
#     S = input()
# try:
#     S = int(S)
#     print(S)
# except:
#     print("Bad String")



#Write your code here
# class Calculator():
#
#     def power(self,x, y):
# #
#         try:
#           if (x < 0) or (y < 0):
#               raise ValueError()
#         except:
#             return ("n and p should be non-negative")
#         else:
#             return(x**y)
#
# myCalculator=Calculator()
# T=int(input())
# for i in range(T):
#     n,p = map(int, input().split())
#     try:
#         ans=myCalculator.power(n,p)
#         print(ans)
#     except Exception as e:
#         print(e)


# n = 20
# lista = []
#
# for numero in range(1,n + 1):
#     if n % numero == 0:
#         lista.append(numero)
#
# print(sum(lista))




# class AdvancedArithmetic(object):
#     def divisorSum(n):
#         raise NotImplementedError
#
# class Calculator(AdvancedArithmetic):
#     def divisorSum(self, n):
#         lista = []
#         for numero in range(1,(n + 1)):
#             if n % numero == 0:
#                 lista.append(numero)
#         return(sum(lista))
#
#
# n = int(input())
# my_calculator = Calculator()
# s = my_calculator.divisorSum(n)
# print("I implemented: " + type(my_calculator).__bases__[0].__name__)
# print(s)



# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None
# class Solution:
#     def display(self,head):
#         current = head
#         while current:
#             print(current.data,end=' ')
#             current = current.next
#
#     def insert(self,head,data):
#
#         new_node = Node(data)
#
#         if head == None:
#             head = new_node
#
#         else:
#             actual_nodo = head
#
#             while actual_nodo.next is not None:
#                 actual_nodo = actual_nodo.next
#
#             actual_nodo.next = new_node
#
#         return head
#
# mylist= Solution()
# T=int(input("x: "))
# head=None
# for i in range(T):
#     data=int(input("y: "))
#     head=mylist.insert(head,data)
# mylist.display(head);


# if __name__ == '__main__':
#     n = int(input("x: ").strip())
#
#     a = list(map(int, input("y: ").rstrip().split()))
#     contador = 0
#
#     largo = len(a)
#     for i in range(largo):
#         for j in range(0, (n - i - 1)) :
#             if a[j] > a[j + 1]:
#                 a[j], a[j + 1] = a[j + 1], a[j]
#                 contador = contador + 1
#     print(f"Array is sorted in {contador} swaps.")
#     print(f"First Element: {a[0]}")
#     print(f"Last Element: {a[-1]}")



# class Node:
#     def __init__(self,data):
#         self.right=self.left=None
#         self.data = data
# class Solution:
#     def insert(self,root,data):
#         if root==None:
#             return Node(data)
#         else:
#             if data<=root.data:
#                 cur=self.insert(root.left,data)
#                 root.left=cur
#             else:
#                 cur=self.insert(root.right,data)
#                 root.right=cur
#         return root
#
#     def getHeight(self,root):
#             if root is None:
#                 return -1
#             else:
#                 altura_izquierdo = self.getHeight(root.left)
#                 altura_derecho = self.getHeight(root.right)
#                 return 1 + max(altura_izquierdo, altura_derecho)
#
# T=int(input())
# myTree=Solution()
# root=None
# for i in range(T):
#     data=int(input())
#     root=myTree.insert(root,data)
# height=myTree.getHeight(root)
# print(height)


# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None
# class Solution:
#     def insert(self,head,data):
#             p = Node(data)
#             if head==None:
#                 head=p
#             elif head.next==None:
#                 head.next=p
#             else:
#                 start=head
#                 while(start.next!=None):
#                     start=start.next
#                 start.next=p
#             return head
#     def display(self,head):
#         current = head
#         while current:
#             print(current.data,end=' ')
#             current = current.next

    # def removeDuplicates(self,head):
    #     unique_values = {}  # diccionario para almacenar valores únicos
    #     current = head
    #     previous = None
    #     while current is not None:
    #         if current.data in unique_values:  # si el valor actual ya existe en el diccionario
    #             previous.next = current.next  # eliminar el nodo actual
    #         else:
    #             unique_values[current.data] = True  # agregar el valor actual al diccionario
    #             previous = current
    #         current = current.next
    #     return head


# mylist= Solution()
# T=int(input())
# head=None
# for i in range(T):
#     data=int(input())
#     head=mylist.insert(head,data)
# head=mylist.removeDuplicates(head)
# mylist.display(head);



# from math import sqrt
#
# def is_prime(n):
#     if n < 2:
#         return False
#     if n == 2:
#         return True
#     if n % 2 == 0:
#         return False
#     for i in range(3, int(sqrt(n))+1, 2):
#         if n % i == 0:
#             return False
#     return True
#
#
# entrada = int(input())
# for i in range(entrada):
#     entrada_2 = int(input())
#     if is_prime(entrada_2) is True:
#         print("Prime")
#     if is_prime(entrada_2)is False:
#         print("Not prime")


# dev = input()
# dev_day, dev_month, dev_year = map(int, dev.split())
#
# ven = input()
# ven_day, ven_month, ven_year = map(int, ven.split())
#
# pay = 0
#
# if (dev_year > ven_year):
#     pay = 10000
# elif dev_year == ven_year:
#     if dev_month > ven_month:
#         #tardado_2 = dev_month - ven_month
#         pay = 500 * (dev_month - ven_month)
#     elif dev_month == ven_month:
#         if dev_day > ven_day:
#             #tardado = dev_day - ven_day
#             pay = 15 * ( dev_day - ven_day)
#
# print(pay)