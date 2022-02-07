#Ex1
'''
number1 = 20
number2 = 30

product = number1*number2
gumar = number1+number2
if product > 1000:
    print(product)
else:
    print("The result is " + str(gumar))
    '''


#Ex2
for i in range(10):
    currentNumber = i
    previewsNumber = i -1
    
    if previewsNumber < 0:
        previewsNumber = 0

    print("Current Number: ", currentNumber)
    print("Prev Number: ", previewsNumber)  
    print("Sum: ", currentNumber + previewsNumber)


