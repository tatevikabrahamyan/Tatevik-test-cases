names = ["Julie", "Simon", "John", "Andrew", "Kim"]
'''
for name in names:
    if name == "John":
        break
    print(name)
'''

#total = 0
'''
for number in range(0,11):
    if number % 2 ==0 and number % 4 == 0:
        print(number)
'''

people = {
    "Julie":23,
    "Simon":28,
    "John":30,
    "Smith":55
}

for key,value in people.items():
    print(key)
    print(value)
    print("========")
