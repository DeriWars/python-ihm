import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from pendu import *


def yes_button_click(old_ihm, replay_layout):
    from start import choose_word
    from UserInterface import UserInterface
    choose_word()
    from start import word
    plate = display(word)
    errors = 0
    ihm = UserInterface(word, plate, errors)
    ihm.layout()
    """from start import Start
    starter = Start()
    starter.start_layout()"""
    old_ihm.hide()
    replay_layout.hide()


def no_button_click():
    from login import Login
    from start import choose_word
    from UserInterface import UserInterface
    choose_word()
    from start import word
    plate = display(word)
    errors = 0
    ihm = UserInterface(word, plate, errors)
    user = Login(ihm)
    user.layout()


class Replay:
    """
    Class that manages the replay layout
    """
    def __init__(self, old_ihm):
        self.window = None
        self.old_ihm = old_ihm

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

        yes_button.clicked.connect(lambda: yes_button_click(self.old_ihm, self.window))
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
