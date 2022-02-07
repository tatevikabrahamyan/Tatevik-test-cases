names = ["John","Smith","Ann","Sam","Elly"]
#print(names)

ages = [49,56,78,96]
#print(ages)

mixedLists = [15,56, "Tatevik", False]
#print(mixedLists)

#print(names[2])
#print(names[-1])

names[1] = "Ani"
#print(names)

names.append("Sona")
#print(names)

lastElement = names.pop()
#print(lastElement)

mixedLists2 = [
    ["BMW", "Kia", "Opel"],
    [15,26,98,12,45,78]
]

#print(mixedLists2[1])
#print(mixedLists2[0][2])
totalLists = mixedLists2[0] + mixedLists2[1]
#print(totalLists)

doubledLists = mixedLists2[1]*2
#print(doubledLists)
#print(mixedLists2[1][1:])
print(mixedLists2[1][:-2])
