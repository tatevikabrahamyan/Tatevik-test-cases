#11
'''
def sampleFunction(anun):
    return anun
anun = input("Enter name:")
print(sampleFunction(anun))
'''
'''
def text(tar):
    return tar.count("a")
sentence = "Annan im harevann e"    
print(text(sentence.lower()))
'''
'''
def isPolyndrom(text):
    return text == text[::-1]
sentence = isPolyndrom("mom")
if sentence:
    print("Yes")
else:
    print("NO")
'''
#15
'''
import math  
def sphere_volume(r):  #volume = 4/3*pi*r^3
    v=4/3*math.pi*r**3
    return v
print(sphere_volume(3))
'''
#16
'''
def difference(a=17, b=0):
    c= b-a
    c=abs(c)
    if c>0:
        return c
    else:
        return (2*c)
print(difference(17,2))
'''
#17
'''
def check_number(a):
    #tver = range(100,2000)
    #for a in tver:
    if a>=100 and a<=1000:
        print("Your number ", a, " is in 100-1000 range")
    else:
        a<=2000 and a>=1001
        print("Your number ", a, " is in 1000-2000 range")
check_number(500)
'''
#18
'''
numList = []
for i in range(3):
    numList.append(int(input()))
#print(numList)

def threeNumber(numList):
    sum1 = numList[0] + numList[1]    
    sum2 = numList[1] + numList[2]
    sum3 = numList[0] + numList[2]
    if sum1 == sum2:
        for j in range(3):
            print(sum1)
    elif sum2 == sum3:
        print(sum2*3)
    elif sum1 == sum3:
        print(sum3*3)
    else:
        print("No calculation sum is equal")
threeNumber(numList)
'''

#19
'''
sentence = input("Enter sentence. ")
word = "is"
if word in sentence and word == sentence.split()[0]:
    print(sentence)
else:
    sentence = sentence.split()
    sentence.remove("is")
    print("is", ' '.join(sentence))
'''
#20
'''
def copyFunction(n):
    nax = input("Enter your sentence")
    for bar in range(n):
        print(nax)   
copyFunction(3)
'''






