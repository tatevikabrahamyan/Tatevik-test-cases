data = {"John":2500,"July":1500, "Simon":3500}
#print(data)

#print(data["July"])

data2 = {
    "boys":["Bob", "Dave", "Rick", "Smith"],
    "girls":["July", "Laura", "Ann", "Kim"]
}

#print(data2["girls"])
#print(data.get("Elon"))
data["July"] = 4500
#print(data)

data2["girls"].append("Alice")
#print((data2))

data.update({"July":7800, "Simon":3300})
#print(data)

print(data2.keys())
print(data2.values())
