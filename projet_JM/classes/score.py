import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from json_data import read_json_file

database_dict = {}
current_player = ""

def get_score(difficulty_level:str, pseudo, word:str, errors: int):
    score = 0
    if difficulty_level == "Niveau 1":
        score = 100 + len(word)*10 - errors
    elif difficulty_level == "Niveau 2" :
        score = 200 + len(word)*10 - errors
    elif difficulty_level == "Niveau 3" :
        score = 300 + len(word)*10 - errors
    return score

def get_users():
    global database_dict, current_player
    read_json_file()
    from json_data import data
    database_dict = data
    from login import user_pseudo
    current_player = user_pseudo
    print(user_pseudo)


def score_calculator():
    pass


class Score(QScrollArea):
    """
    CLass that manages the scoreboard layout
    """

    def __init__(self):
        super(Score, self).__init__()
        self.window = None

    def score_layout(self):
        self.window = QWidget()
        self.resize(600, 600)
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
        get_users()
        label_pseudos_tab = QLabel()
        label_scores_tab = QLabel()
        pseudos, scores = "", ""
        liste_1 = []
        liste_2 = []
        liste_3 = []
        """for username, score in database_dict.items():
            pseudos += username + "\n"
            scores += str(score) + "\n" """
        e = sorted(database_dict.items(), key=lambda x: x[1], reverse=True)
        for username, score in dict(e).items():
            pseudos += username + "\n"
            scores += str(score) + "\n"
        label_pseudos_tab.setText(pseudos)
        label_pseudos_tab.setFont(QFont("Times", 12))
        label_pseudos_tab.setAlignment(Qt.AlignCenter)
        liste = label_pseudos_tab.text().split("\n")

        """for user in label_pseudos_tab.text():
            if user == current_player:
                """

        label_scores_tab.setText(scores)
        label_scores_tab.setFont(QFont("Times", 12))
        label_scores_tab.setAlignment(Qt.AlignCenter)

        grid_layout.addWidget(label_username, 1, 1)
        grid_layout.addWidget(label_pseudos_tab, 2, 1)
        grid_layout.addWidget(label_score, 1, 2)
        grid_layout.addWidget(label_scores_tab, 2, 2)

        form_layout.addRow(label_space)
        form_layout.addRow(grid_layout)

        self.window.setLayout(form_layout)

        self.setWidget(self.window)
        self.setWidgetResizable(True)
        self.show()
