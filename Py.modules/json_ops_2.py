import json
from xml.dom import NO_MODIFICATION_ALLOWED_ERR

dataDict = {
    "sampleString": "Great Automation framework",
    "smapleList":["Good","Better","Best"],
     "sampleTuple":("Python","Pytest","Automation"),
    "sampleObject":{"platform":"Udemy","Valuable":True},
     "sampleInterger":555,
  "booleanValue": True,
    "nonvalue": NO_MODIFICATION_ALLOWED_ERR

}

print("Convert dict to json")
resultJSON = json.dumps(dataDict,sort_keys=True, indent=4)
print(resultJSON)
print(type(resultJSON)== str)

with open("example.json", "r") as file:
    data = json.load(file)
    print(type(data))
    print(data.keys())
    print(type(data["address"]))




