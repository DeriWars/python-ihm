import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from login import *

username_list = []


def get_username():
    read_json_file()
    print(data)
    for username, score in data:
        username_list.append(username)

    print(username_list)

class Score:
    def __init__(self):
        pass

    def score(self):
        app = QApplication(sys.argv)
        self.window = QWidget()
        self.window.resize(600, 600)
        self.window.setWindowTitle("Tableau des scores")
        self.window.setStyleSheet("background-color : #D2E1E1")

        form_layout = QFormLayout()
        label_global_scores = QLabel("Scores globaux")
        label_global_scores.setAlignment(Qt.AlignCenter)
        label_global_scores.setFont(QFont('Times', 50))
        form_layout.addRow(label_global_scores)
        label_space = QLabel("\n")

        grid_layout = QGridLayout()
        label_username = QLabel("Pseudo")
        label_username.setFont(QFont("Times", 25))
        label_username.setAlignment(Qt.AlignCenter)
        label_score = QLabel("Score")
        label_score.setFont(QFont("Times", 25))
        label_score.setAlignment(Qt.AlignCenter)

        # TODO : vertical bar to separate username and score

        label_pseudos = QLabel()

        form_layout.addRow(label_space)
        form_layout.addRow(grid_layout)
        grid_layout.addWidget(label_username, 1, 1)
        grid_layout.addWidget(label_score, 1, 2)


        self.window.setLayout(form_layout)



        self.window.show()
        sys.exit(app.exec())

score = Score()
get_username()
score.score()