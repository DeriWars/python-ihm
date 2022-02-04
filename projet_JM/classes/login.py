import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from UserInterface import *
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


def connect_button_click(ihm: UserInterface, window, username):
    ihm.layout()
    window.hide()
    read_json_file()
    load_file(username)


class ConnectButton(QPushButton):
    def __init__(self, label, ihm: UserInterface, window, input_user):
        super().__init__(label)
        self.clicked.connect(lambda: connect_button_click(ihm, window, input_user.text()))


class Login:
    def __init__(self, ihm: UserInterface):
        self.ihm = ihm

    def layout(self):
        # app = QApplication(sys.argv)
        self.window = QWidget()
        self.window.setWindowTitle("Login || By Personne73 // maxgiant_")
        self.window.resize(450, 200)
        self.window.setStyleSheet("background : #D2E1E1")

        label_text = QLabel(self.window)
        label_text.setText("Entrez un pseudo, \npuis choisissez la difficulté du pendu avant de vous connecter")
        label_text.setAlignment(Qt.AlignCenter)
        label_text.setFont(QFont("Times", 10))

        label_user = QLabel("Pseudo")
        label_user.setFont(QFont("Times", 9))
        input_user = QLineEdit()
        input_user.setFont(QFont("Times", 10))
        label_space = QLabel()

        login_layout = QFormLayout()

        connect_button = ConnectButton("Se connecter", self.ihm, self.window, input_user)

        login_layout.addRow(label_text)
        login_layout.addRow(label_space)
        login_layout.addRow(label_user, input_user)
        login_layout.addWidget(connect_button)

        self.window.setLayout(login_layout)
        self.window.show()
