#21
'''
def numberType(i):
   
    if i%2 == 0:
        print("i is an even number.")
    else:
        print("i is an add number.")

i = int(input("Enter any number.")).__float__()
numberType(i)
'''

#22
# list =[2,44,23,4,6,7,89,143,40]
# number = list.count(4)
# print(number)

#25
# list1 = [1,5,8,3]

# def checkNumber(i):
#     if i in list1:
#         print(True)
#     else: 
#         print(False)
# checkNumber(3)

#27
# def make_elements_to_string(mylist):
#     emptylist = ""

#     for i in mylist:
#        emptylist += str(i);
          
#     return emptylist;       
# print(make_elements_to_string([1,3,35]))


#28
'''
numbers = [    
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 
    958,743, 527
    ]

def evennumbers(j):
    numbers[j] = a
    newNumbers = []
    for i in numbers:
        if a%2 == 0 and a<=237:
            print(newNumbers.append(a))
        else:
            break

evennumbers(5)
'''

#29
'''
color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])

print(color_list_1.difference(color_list_2)) #---------------- patrasti funkcia 


for color in color_list_1:
    newList = []
    if color not in color_list_2: 
        newList.append(color) 
        print(newList)
'''


#30
def triangle_area(b,h):
    s = 1/2 * b * h
    print(s)

triangle_area(12,24)