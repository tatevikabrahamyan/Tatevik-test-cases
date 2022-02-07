import json

from datetime import date

current_date = date.today()
current_year = current_date.year
current_month = current_date.month
print(current_year)

myInfo = {
    "firstName": "Tatevik",
    "lastname":  "Abrahamyan",
    "address":   "Volo Komitas",
    "year":      int(input("Input year of birth. ")),
    "month":     int(input("Input monyh. "))
}

with open("myInfo.json", 'w+') as f:
    f.write(json.dumps(myInfo, indent=4))

with open("myInfo.json", 'r') as f:
    myFile = json.load(f)

    year = myInfo["year"]
    month = myInfo["month"]
    
    if current_month < myInfo["month"]:
        age = current_year - year - 1
    else:
        age = current_year - year
    
    print("I am", age, "years old.")




 