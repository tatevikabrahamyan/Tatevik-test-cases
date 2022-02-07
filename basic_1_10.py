#1.
#print("Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are ")

#2.
'''
import sys
print("Python version:")
print(sys.version)
'''

#3
'''
from datetime import date
today = date.today()
print("Today:", today)
'''

#4
'''
from math import pi
print("Enter r")
r = float(input())
S = pi * r**2
print("Circle area is:", S)
'''

#5
'''
name=input("Enter name: ")
surname = input("Enter surname: ")
name = name.capitalize()
surname = surname.capitalize()
print("Name is", name, "\nSurname is", surname)
'''

#6
'''
sequence = input("Enter sequence of comma-separated numbers")
#print(sequence)
numbers = sequence.split(",")
tuple = tuple(numbers)
print("List: ", numbers)
print("Tuple:", tuple)
'''

#7
'''
enter = input("Enter your file name")
fileName = enter.split(".")
print(fileName[1]) 
'''

#8
#colors = ["bleu", "red", "green", "yellow"]
#print(colors[0].capitalize(), ",", colors[-1].capitalize())

#9
#exam_date = (11,12,2014)
#print("The examination will start at %i/ %i/ %i"%exam_date)

#10
'''
k= int(input("Input number to get sum: "))
k1 = int("%s" % k)
#print(k1)
k2 = int("%s%s" % (k,k))
k3 = int("%s%s%s" %(k,k,k))
k=k1+k2+k3
print(k)
'''

