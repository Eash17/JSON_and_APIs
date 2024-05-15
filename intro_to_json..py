import json

car_data = {
    "name": "Tesla",
    "engine" : "electric"
}

print(type(car_data))

# json.dumps() --> turns python dict into str

car_data_json_string = json.dumps(car_data)
print(type(car_data_json_string))

# json.dump() --> converts dict into a str and puts it in a new file

with open("new_json_file.json", "w") as jsonfile:
    json.dump(car_data, jsonfile)



