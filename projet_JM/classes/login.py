import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import json

FILENAME = "../data/database.json"
data = None


class Login:
    def __init__(self, username, score=0):
        self.username = username
        self.score = score

    def layout(self):
        app = QApplication(sys.argv)
        window = QWidget()
        window.setWindowTitle("Login || By Personne73 // maxgiant_")
        window.resize(450, 200)

        label_text = QLabel(window)
        label_text.setText("Essai d'affichage du texte")
        label_text.setAlignment(Qt.AlignCenter)

        label_user = QLabel("Pseudo")
        input_user = QLineEdit()
        # input_user.setMaximumSize(250, 50)

        label_space = QLabel()

        login_layout = QFormLayout()
        login_layout.addRow(label_text)
        login_layout.addRow(label_space)
        login_layout.addRow(label_user, input_user)

        bouton_connect = QPushButton(window)
        bouton_connect.setText("Se connecter")
        bouton_connect.move(150, 100)

        # bouton_connect.setGeometry(120, 120, 115, 40)

        window.setLayout(login_layout)

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
        bouton_connect.clicked.connect(bouton_connect_clicked)
        """
        window.show()
        sys.exit(app.exec())


def main():
    user = Login("tresor", 0)
    user.layout()


if __name__ == "__main__":
    main()
