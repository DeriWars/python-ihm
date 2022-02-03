"""import json

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
"""
def test():
    with open("Joël.txt", 'w', encoding='utf-8') as f:
        f.write("\n" + "Pseudo " + "Test ")
        return f


f = test()
print(f)

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

"""class Fenetre2():
    def __init__(self):
        self.window2 = None

    def open_window(self):
        self.window2 = QWidget()
        self.window2.setGeometry(200, 200, 500, 500)
        button2 = QPushButton("Fermer", self.window2)
        self.window2.show()


class Fenetre():
    def __init__(self):
        self.window = None

    def layout(self):
        self.window = QWidget()
        self.window.setGeometry(0, 0, 500, 500)
        f2 = Fenetre2()
        button = QPushButton("New Window", self.window)
        button.clicked.connect(lambda: f2.open_window())
        self.window.setWindowTitle("coucou")
        self.window.show()


app = QApplication(sys.argv)
f = Fenetre()
f.layout()
sys.exit(app.exec())"""


"""def close(window):
    window.close()


def open_window(window2):
    window2.setGeometry(200, 200, 500, 500)
    button2 = QPushButton("Fermer", window2)
    window2.show()
    button2.clicked.connect(lambda: close(window2))
    while QDate.currentDate() != "03/02/2002":
        window.show()
        button2.show()
        print(button2.isVisible(), window2.isVisible())


app = QApplication(sys.argv)

window = QWidget()
window.setGeometry(0, 0, 500, 500)
window2 = QWidget()
button = QPushButton("New Window", window)
button.clicked.connect(lambda: open_window(window2))
window.setWindowTitle("coucou")

window.show()
sys.exit(app.exec())"""


