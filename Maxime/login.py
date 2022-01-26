import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Login:
    def __init__(self, username, score=0):
        self.username = username
        self.score = score

    def layout(self):
        app = QApplication(sys.argv)
        window = QWidget()
        window.setWindowTitle("Login || By Personne73 // maxgiant_")
        window.resize(350, 200)

        label_text = QLabel(window)
        label_text.setText("essai ozjeg z gpzg pg zpj zpgzrg z")

        label_user = QLabel("Pseudo")
        input_user = QLineEdit()

        login_layout = QFormLayout()
        login_layout.addRow(label_text)
        login_layout.addRow(label_user, input_user)
        #login_layout.addWidget(label_tex)
        #login_layout.addWidget(label_user).addWidget(input_user)

        bouton_connect = QPushButton(window)
        bouton_connect.setText("Se connecter")
        bouton_connect.move(150, 100)
        bouton_connect.setGeometry(120, 120, 115, 40)

        window.setLayout(login_layout)

        window.show()
        sys.exit(app.exec())


def main():
    user = Login("tresor", 0)
    user.layout()


main()
