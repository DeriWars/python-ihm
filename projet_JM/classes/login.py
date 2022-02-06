import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from UserInterface import *
from json_data import *


def connect_button_click(ihm: UserInterface, window, username):
    """
    Function which control the click of the connect button
    :param ihm: a UserInterface object
    :param window: the window to hide
    :param username: the username of the player
    """

    ihm.layout()
    window.hide()
    read_json_file()
    load_file(username)


class ConnectButton(QPushButton):
    """
    Class for create the connect button and which connects it to the good function
    """

    def __init__(self, label, ihm: UserInterface, window, input_user):
        super().__init__(label)
        self.clicked.connect(lambda: connect_button_click(ihm, window, input_user.text()))


class Login:
    """
    Class that manages the login layout
    """

    def __init__(self, ihm: UserInterface):
        self.ihm = ihm

    def layout(self):
        self.window = QWidget()
        self.window.setWindowTitle("Login || By Personne73 // maxgiant_")
        self.window.resize(450, 200)
        self.window.setStyleSheet("background : #D2E1E1")

        label_text = QLabel(self.window)
        label_text.setText("Entrez un pseudo puis connectez vous")
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
