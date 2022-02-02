import json

file_json = "test.json"
data = {}


def read_json_file():
    global data
    with open(file_json, "r", encoding="utf8") as f:
        data = json.load(f)
    # return data


def load_json_file(username):
    with open(file_json, "w", encoding="utf8") as file:
        # data = dict(read_json_file())
        data[username] = 0
        json.dump(data, file, indent=4)


print(data)
read_json_file()
print(data)
load_json_file("maxgiant_")
print(data)
