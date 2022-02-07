'''
i = 0
while i<10:
    i = i+1 
    if i == 5:
        continue
    print("Hello! " + str(i))
'''

while True:
    print("1. Settingd")
    print("2. Home")
    print("3. Profiel")
    print("4. Exit")
    print("Enter Menu ID")
    command = input()

    if int(command) == 1:
        print("Go Settings")
    elif int(command) == 2:
        print("Go Home") 
    elif int(command) == 3:
        print("Go Profile")
    elif int(command) == 4:
        print("Exit")
        break
    else: 
        print("Wrong Menu ID")

    print("==========")
