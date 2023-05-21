import json
with open('example.json','r') as file:
    data = json.load(file)
    print(data.keys())
    print(data['orders'])

def validateJson(json_file_example):
    try:
         json.loads(json_file_example)
    except ValueError as err:
      return False
    return True
JsonString = """{"name":"noam","pro":"QA","email":"lederma@gmail.com"}"""

isValid = validateJson(JsonString)
print("json string passed is valid ?", isValid)


