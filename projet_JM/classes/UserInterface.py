import string
from pendu import *
from bouton import *
from pictures import *
from score import *
from webdefinitions import *
from PyQt5.QtCore import QTime, QTimer
from login import *
from timer import start_time

plate = ""
buttons_list = []
pictures_list = ["pendu_0.png", "pendu_1.png", "pendu_2.png", "pendu_3.png",
                 "pendu_4.png", "pendu_5.png", "pendu_6.png", "pendu_7.png", "pendu_8.png",
                 "pendu_9.png", "pendu_10.png", "pendu_11.png", "pendu_12.png"]


def game(button, label_word, top_grid_layout, input, word, score_button, def_word_button, replay_button, ihm):
    """
    Function that manages the hangman game
    :param score_button: score button
    :param button: the button clicked
    :param label_word: the word generated with underscores
    :param top_grid_layout: the layout where the label_word is generated
    :param input: the line where the word can be inserted
    :param word: the word generated thanks to the list of words. This one is known
    """
    global plate

    if button.text() in word:
        plate = change_display(plate, word, button.text())

    elif button.text() not in word:
        ihm.errors += 1
    label_word.setText(plate)
    error_state(top_grid_layout, pictures_list, ihm.errors)

    if ihm.errors == len(pictures_list) - 1:
        lose_label(label_word, input, buttons_list, word, disable_input, button_state, score_button, def_word_button, replay_button)

    if "_" not in plate:
        win_label(label_word, input, buttons_list, word, disable_input, button_state, score_button, def_word_button, replay_button)


def input_enter(label_word, word, answer: QLineEdit, top_grid_layout, input, score_button, def_word_button, replay_button, ihm):
    """
    Function that manages the input pressed
    :param score_button: score button
    :param label_word: the word generated with underscores
    :param word: the word not hidden
    :param answer: the input line
    :param top_grid_layout:
    :param input: the input line
    """
    if answer.text() == "":
        return
    if answer.text() == word:
        win_label(label_word, input, buttons_list, word, disable_input, button_state, score_button, def_word_button, replay_button)
    elif answer.text() != word:
        ihm.errors += 1
        answer.clear()
        label_word.setText(plate)
    error_state(top_grid_layout, pictures_list, ihm.errors)


def disable_input(input):
    """
    Function ta disable the input
    :param input: the input line
    """
    input.setReadOnly(True)


def button_state(button, state: bool):
    """
    Function to set enable or not a button
    :param state: the state of the button
    :param button: a button
    """
    button.setEnabled(state)


def score_button_click(score: Score):
    """
    Function which shows the scoreboard when the score button is pressed
    :param score: a Score object
    """
    score.score_layout()


def definition_button_click(web_def, word):
    web_def.definition_word(word)


class UserInterface:
    """
    Class that manages the main interface of the hangman game
    """
    def __init__(self, word, plate, errors):
        """
        :param word: the word generated
        :param plate: the plate generated
        """
        self.time = None
        self.window = None
        self.word = word
        self.plate = plate
        self.errors = errors

    def timer(self, label_time, label_word, input, score_button):
        """self.time = self.time.addSecs(1)
        label_time.setText(self.time.toString("hh:mm:ss"))
        if self.time.toString("hh:mm:ss") == "00:00:05":
            lose_label(label_word, input, buttons_list, self.word, disable_input, button_state, score_button)
            self.time = self.time.addSecs(-1)
            # self.time.stop()
            print(self.time.toString("hh:mm:ss"))
        elif label_word.text() == f"\n---- Victoire du joueur ----\nLe bon mot était : {self.word}" or label_word.text() == f"\n---- GAME OVER ---- \nLe bon mot était : {self.word}":
            # self.time.stop()
            self.time = self.time.addSecs(-1)
            print(self.time.toString("hh:mm:ss"))"""

    def layout(self):
        self.window = QWidget()
        self.window.resize(1200, 600)
        self.window.setWindowTitle("Le jeu du Pendu")
        self.window.setWindowIcon(QIcon("../images/10.gif"))
        self.window.setStyleSheet("background : #D2E1E1")
        global plate
        plate = self.plate

        hangman_layout = QFormLayout()
        label_space = QLabel()
        label_word = QLabel()
        label_time = QLabel()
        label_word.setText(plate)
        top_grid_layout = QGridLayout()
        top_layout_right = QVBoxLayout()
        bottom_grid_layout = QGridLayout()
        answer = QLineEdit()
        answer.setMaximumSize(600, 20)
        answer.setDisabled(False)
        definition_word_button = QPushButton("Definition")
        score_button = QPushButton("Score")
        replay_button = QPushButton("Rejouer")

        label_word.setFont(QFont("Times", 50))
        label_word.setAlignment(Qt.AlignCenter)

        for i in string.ascii_lowercase:
            buttons_list.append(Button(i, label_word, top_grid_layout, game, answer, self.word, score_button, definition_word_button, replay_button, self))

        bottom_grid_layout.addWidget(buttons_list[0], 1, 1)
        bottom_grid_layout.addWidget(buttons_list[25], 1, 2)
        bottom_grid_layout.addWidget(buttons_list[4], 1, 3)
        bottom_grid_layout.addWidget(buttons_list[17], 1, 4)
        bottom_grid_layout.addWidget(buttons_list[19], 1, 5)
        bottom_grid_layout.addWidget(buttons_list[24], 1, 6)
        bottom_grid_layout.addWidget(buttons_list[20], 1, 7)
        bottom_grid_layout.addWidget(buttons_list[8], 1, 8)
        bottom_grid_layout.addWidget(buttons_list[14], 1, 9)
        bottom_grid_layout.addWidget(buttons_list[15], 1, 10)

        bottom_grid_layout.addWidget(buttons_list[16], 2, 1)
        bottom_grid_layout.addWidget(buttons_list[18], 2, 2)
        bottom_grid_layout.addWidget(buttons_list[3], 2, 3)
        bottom_grid_layout.addWidget(buttons_list[5], 2, 4)
        bottom_grid_layout.addWidget(buttons_list[6], 2, 5)
        bottom_grid_layout.addWidget(buttons_list[7], 2, 6)
        bottom_grid_layout.addWidget(buttons_list[9], 2, 7)
        bottom_grid_layout.addWidget(buttons_list[10], 2, 8)
        bottom_grid_layout.addWidget(buttons_list[11], 2, 9)
        bottom_grid_layout.addWidget(buttons_list[12], 2, 10)

        bottom_grid_layout.addWidget(buttons_list[22], 3, 3)
        bottom_grid_layout.addWidget(buttons_list[23], 3, 4)
        bottom_grid_layout.addWidget(buttons_list[2], 3, 5)
        bottom_grid_layout.addWidget(buttons_list[21], 3, 6)
        bottom_grid_layout.addWidget(buttons_list[1], 3, 7)
        bottom_grid_layout.addWidget(buttons_list[13], 3, 8)

        bottom_grid_layout.addWidget(score_button, 4, 10)
        bottom_grid_layout.addWidget(definition_word_button, 4, 9)
        bottom_grid_layout.addWidget(replay_button, 4, 8)
        shadow(score_button)
        shadow(definition_word_button)
        shadow(replay_button)

        button_state(score_button, False)
        button_state(definition_word_button, False)
        button_state(replay_button, False)

        score = Score()
        score_button.clicked.connect(lambda: score_button_click(score))

        answer.returnPressed.connect(
            lambda: input_enter(label_word, self.word, answer, top_grid_layout, answer, score_button,
                                definition_word_button, replay_button, self))

        web_def = WebDef()
        definition_word_button.clicked.connect(lambda: definition_button_click(web_def, self.word))

        picture = Pictures(pictures_list, self.errors)
        picture.display(top_grid_layout)
        top_grid_layout.addItem(top_layout_right, 1, 2)
        top_layout_right.addWidget(label_word)
        top_layout_right.addWidget(answer)

        hangman_layout.addRow(top_grid_layout)
        hangman_layout.addRow(label_space)
        hangman_layout.addRow(label_space)
        hangman_layout.addRow(bottom_grid_layout)
        hangman_layout.addRow(label_time)

        self.window.setLayout(hangman_layout)
        self.window.show()
        self.time = start_time()
