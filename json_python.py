import json

json_data = """
{
  "name": "Иван",
  "age": 30,
  "is_student": false,
  "courses": [
    "Python",
    "QA Automation",
    "Api Testing"
  ],
  "address": {
    "city": "Moscow",
    "zip": "10100"
  }
}
"""
parsed_data = json.loads(json_data)

# print((parsed_data['address']['city']))

#
# with open("json_example.json", "r", encoding="utf-8") as file:
#     read_data = json.load(file)
#     print(read_data, type(read_data))

with open("json_user.json", "w", encoding="utf-8") as file:
    json.dump(json_data, file, indent=2, ensure_ascii=False)
