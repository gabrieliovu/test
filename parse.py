import csv
import json
from datetime import datetime

f = open("data.json")
data = json.load(f)

result = []
for i in data:
    value = dict()
    value["pk"] = i.get("id")
    value["model"] = "users.person"
    value["fields"] = dict()
    value["fields"]["first_name"] = i.get("first_name")
    value["fields"]["last_name"] = i.get("last_name")
    value["fields"]["email"] = i.get("email")
    value["fields"]["gender"] = i.get("gender")
    value["fields"]["date_of_birth"] = datetime.strptime(i.get("date_of_birth"), '%d/%m/%Y').strftime('%Y-%m-%d')
    value["fields"]["industry"] = i.get("industry")
    value["fields"]["salary"] = i.get("salary")
    value["fields"]["years_of_experience"] = i.get("years_of_experience")
    result.append(value)

filename = "records.json"
g = open(filename, "w")
json.dump(result, g)
f.close()
g.close()
