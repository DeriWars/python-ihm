import json

file_json = "../data/database.json"
data = {}


def read_json_file():
    global data
    with open(file_json, "r", encoding="utf8") as file:
        data = json.load(file)


def load_file(username):
    with open(file_json, "w", encoding="utf8") as file:
        data[username] = 0
        json.dump(data, file, indent=4)
