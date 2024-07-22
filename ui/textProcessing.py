import json 

"""
This module will contain all the functions to manipulate text and format it for use by the UI frontend.
"""

"""
This functions returns a dict formatted as such: {Patient1 : ["demography", "Age:62", etc], Patient2 : [...]}

Here each key is a patient and the value is a list containing headings, and data. The return value of this function is intended to be passed
to a a text formatter that will then pass a value to a text widget on the front end to display patient data.
"""
def readPatient_json(fileName):
    patients = {}
    with open(fileName, "r") as data:
        data = json.load(data)
        # add patient as keys to patients dict
        for patient in data:
            patients[patient] = []
            # add all the data to the list
            for category in data[patient]:
                patients[patient].append(category)
                # all all the data in each category
                for info in data[patient][category]:
                    patients[patient].append(info + ":" + str(data[patient][category][info]))
    return patients

def returnPatientDataAsList():
    patients = []
    data = readPatient_json("../patientData/multiplePatient.json")
    for patient in data:
        patients.append(data[patient])
    return patients

def processjson():
    with open("../patientData/multiplePatient.json", "r") as data:
        return json.load(data)

if __name__ == "__main__":
    print(returnPatientDataAsList())