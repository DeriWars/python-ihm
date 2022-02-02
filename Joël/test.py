import json


file_json = "../test.json"


def read_json_file():
    with open(file_json, "r", encoding="utf8") as file:
        data = json.load(file)
        print(data)
        return dict(data)


def load_file(username):
    with open(file_json, "w", encoding="utf8") as file:
        data = dict(read_json_file())
        print(data)
        data[username] = 0
        json.dump(data, file, indent=4)



load_file("maxime")
