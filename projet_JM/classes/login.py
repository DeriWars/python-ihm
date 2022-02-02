import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from UserInterface import *
from io import StringIO
import json

file_json = "../data/database.json"


def read_json_file():
    with open(file_json, "r", encoding="utf8") as file:
        text = file.read()
        print(text)
        data = json.load()
        print(data)
        return dict(data)


def load_file(filename, username):
    with open(filename, "w", encoding="utf8") as file:
        data = dict(read_json_file())
        print(data)
        data[username] = 0
        json.dump(data, file, indent=4)


def connect_button_click(ihm: UserInterface, window, username):
    ihm.layout()
    window.hide()
    load_file(file_json, username)


class ConnectButton(QPushButton):
    def __init__(self, label, ihm: UserInterface, window, input_user):
        super().__init__(label)
        self.clicked.connect(lambda: connect_button_click(ihm, window, input_user.text()))




    """
    revoir self
    def readfile(filename, username):
        with open(filename, mode='r', encoding='utf8') as file:
            pass
    def loadfile(filename, username):
        with open(filename, mode='w', encoding='utf8') as file:
            data = json.load(file)
            data[self.username] = 0
            json.dump(data, file, indent=4)
    def bouton_connect_clicked():
        login_name = input_user.text()
        loadfile(FILENAME, login_name)
    connect_button.clicked.connect(bouton_connect_clicked)
    """


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
        level_box = QHBoxLayout()
        level_box.setAlignment(Qt.AlignCenter)
        level1_button = QRadioButton("Niveau 1")
        level1_button.setChecked(True)
        level2_button = QRadioButton("Niveau 2")
        level3_button = QRadioButton("Niveau 3")

        level_box.addWidget(level1_button)
        level_box.addWidget(level2_button)
        level_box.addWidget(level3_button)

        """connect_button = QPushButton(window)
        connect_button.setText("Se connecter")
        connect_button.move(175, 150)"""
        connect_button = ConnectButton("Se connecter", self.ihm, self.window, input_user)

        # connect_button.setGeometry(120, 120, 115, 40)
        login_layout.addRow(label_text)
        login_layout.addRow(label_space)
        login_layout.addRow(label_user, input_user)
        login_layout.addRow(level_box)
        login_layout.addWidget(connect_button)

        self.window.setLayout(login_layout)
        self.window.show()

