import os
dirpath = os.getcwd()
print("Current Directory: "+dirpath)


def print_hello(fromWho,to):
    print("Hello from "+fromWho + " to "+to)


#print_hello("Jylie", "Elly")

def sum(numberOne=1, numberTwo=0):
    print(numberOne+numberTwo)

#sum(5,6)
#sum(100,200)

'''
myVar = "Some text"
myVar2 = 731
print(type(myVar))
print(type(str(myVar2)))
'''
#sum(9)

def doubled(x):
    x *=2
    return x

finalResult = doubled(10)
#print(finalResult)

myString = "Hello World" #--------------global variable, can't be changed

def changeString():
    name = "Alice"       #--------------local variable
    #print(myString)

    #myString = myString + " from Tatevik"
    #global myString
    #myString+=" from Tatevik"

changeString()
#print(name)
#print(myString)   


