import json

with open("./data/patients.json") as f:
    data = json.load(f)

for patient_id, patient_info in data.items():
    print(patient_info)
