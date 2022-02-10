import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from pendu import *


def yes_button_click():
    pass


def no_button_click():
    pass


class Replay:
    """
    Class that manages the replay layout
    """
    def __init__(self):
        self.window = None

    def replay_layout(self):
        self.window = QWidget()
        self.window.resize(400, 150)
        self.window.setWindowTitle("Rejouer")
        self.window.setStyleSheet("background : #D2E1E1")

        replay_layout = QFormLayout()

        text_label = QLabel("Voulez vous rejouer avec le même pseudo ?")
        text_label.setFont(QFont("Times", 10))
        text_label.setAlignment(Qt.AlignCenter)

        label_space = QLabel()

        answer_box = QHBoxLayout()
        answer_box.setAlignment(Qt.AlignCenter)

        yes_button = QCheckBox("Oui")
        no_button = QCheckBox("Non")

        yes_button.clicked.connect(lambda: yes_button_click(self.ihm))
        no_button.clicked.connect(lambda: no_button_click())

        answer_box.addWidget(yes_button)
        answer_box.addWidget(no_button)

        replay_layout.addRow(text_label)
        replay_layout.addRow(label_space)
        replay_layout.addRow(answer_box)

        self.window.setLayout(replay_layout)
        self.window.show()


"""app = QApplication(sys.argv)
restart = Replay()
restart.replay_layout()
sys.exit(app.exec())"""
