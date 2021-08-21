from pprint import pprint
import json

d = {"employees": [{"firstName": "John", "lastName": "Doe"},
                   {"firstName": "Anna", "lastName": "Smith"},
                   {"firstName": "Peter", "lastName": "Jones"}],
     "owners": [{"firstName": "Jack", "lastName": "Petter"},
                {"firstName": "Jessy", "lastName": "Petter"}]}


def printOutLastNameOfSecondEmployee():
    print(d["employees"][1]["lastName"])
    d["employees"][1]["lastName"] = "Smooth"
    print(d)


def addNewEmployee():
    d["employees"].append(dict(firstName="Geranimoo", lastName="ADC"))
    d["employees"].append(dict(firstName="ahahahah", lastName="bbbbbb"))
    pprint(d)


with open("company1.json", "w") as file:
    json.dump(d, file, indent=4)
