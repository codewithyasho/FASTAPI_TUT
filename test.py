import json

with open("./data/patients.json") as f:
    data = json.load(f)

print(data["P001"])
