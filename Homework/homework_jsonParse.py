import json
import pandas as pd

info = {
    "firstName": "Tatevik",
    "lastName":   "Abrahamyan",
    "address":    "Volo_Komitas"
}

with open("aboutMe.json", 'w+') as file_object:
    file_object.write(json.dumps(info,indent=4))

with open("aboutMe.json", 'r') as file_object:
    result_json = json.load(file_object)
    print(info["firstName"], info["lastName"]+"y ashxatum e ", info["address"]+"um")



# df = pd.read_json(r'C:\Users\tatevik.abrahamyan\Desktop\Projects\Python\Homework.json')
# df.to_csv(r'C:\Users\tatevik.abrahamyan\Desktop\Projects\Python\Homework.txt', index = False)    


