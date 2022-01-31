import string
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from pendu import *
from bouton import *
from pictures import *
from PyQt5.QtCore import QTime


WORDFILE = "../data/mots.txt"
errors = 0
buttons_list = []
pictures_list = ["pendu_0.png", "pendu_1.png", "pendu_2.png", "pendu_3.png",
                "pendu_4.png", "pendu_5.png", "pendu_6.png", "pendu_7.png", "pendu_8.png",
                "pendu_9.png", "pendu_10.png", "pendu_11.png", "pendu_12.png"]


def game(button, label_word, top_grid_layout, input):
    global errors, plate

    if button.text() in word:
        plate = change_display(plate, word, button.text())

    elif button.text() not in word:
        errors += 1
    label_word.setText(plate)
    error_state(top_grid_layout, pictures_list, errors)

    if errors == len(pictures_list) - 1:
        lose_label(label_word, input, buttons_list, word, disable_input)

    if "_" not in plate:
        win_label(label_word, input, buttons_list, word, disable_input)


def input_enter(label_word, word, answer: QLineEdit, top_grid_layout, input):
    global errors
    if answer.text() == word:
        win_label(label_word, input, buttons_list, word, disable_input)
    elif answer.text() != word:
        errors += 1
        print("les erreurs :", errors)
        answer.clear()
        label_word.setText(plate)
    error_state(top_grid_layout, pictures_list, errors)


def disable_input(input):
    input.setReadOnly(True)


class UserInterface:
    def __init__(self, word, plate):
        self.word = word
        self.plate = plate
        self.time = None

    def timer(self, label_time, label_word, input):
        self.time = self.time.addSecs(1)
        label_time.setText(self.time.toString("hh:mm:ss"))
        if self.time.toString("hh:mm:ss") == "00:01:00":
            lose_label(label_word, input, buttons_list, word, disable_input)
            self.time = self.time.addSecs(-1)
            # self.time.stop()
            print(self.time.toString("hh:mm:ss"))
        elif label_word.text() == f"\n---- Victoire du joueur français ----\nLe bon mot était : {word}":
            # self.time.stop()
            self.time.addSecs(-1)
            print(self.time.toString("hh:mm:ss"))

    def getTimer(self):
        pass

    def layout(self):
        global errors
        app = QApplication(sys.argv)
        window = QWidget()
        window.resize(1200, 600)
        window.setWindowTitle("Le jeu du Pendu")
        window.setWindowIcon(QIcon("../images/10.gif"))

        hangman_layout = QFormLayout()
        label_space = QLabel()
        label_word = QLabel()
        label_word.setText(self.plate)
        top_grid_layout = QGridLayout()
        top_layout_right = QVBoxLayout()
        bottom_grid_layout = QGridLayout()
        answer = QLineEdit()
        answer.setMaximumSize(600, 20)
        label_time = QLabel()

        timer0 = QTimer()
        self.time = QTime(0, 0, 0)
        timer0.setInterval(1000)
        timer0.timeout.connect(lambda: self.timer(label_time, label_word, answer))
        timer0.start()

        label_word.setFont(QFont("Times", 50))
        label_word.setAlignment(Qt.AlignCenter)

        for i in string.ascii_lowercase:
            buttons_list.append(Button(i, label_word, top_grid_layout, game, answer))

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

        answer.returnPressed.connect(lambda: input_enter(label_word, self.word, answer, top_grid_layout, answer))

        picture = Pictures(pictures_list, errors)
        picture.display(top_grid_layout)
        top_grid_layout.addItem(top_layout_right, 1, 2)
        top_layout_right.addWidget(label_word)
        top_layout_right.addWidget(answer)

        hangman_layout.addRow(top_grid_layout)
        hangman_layout.addRow(label_space)
        hangman_layout.addRow(label_space)
        hangman_layout.addRow(bottom_grid_layout)
        window.setLayout(hangman_layout)

        hangman_layout.addRow(top_grid_layout)
        hangman_layout.addRow(label_space)
        hangman_layout.addRow(bottom_grid_layout)
        hangman_layout.addRow(label_time)
        window.setLayout(hangman_layout)

        window.show()
        sys.exit(app.exec())


words_list = read_file(WORDFILE)
word = random_word(words_list)
print(word)
plate = display(word)
ihm = UserInterface(word, plate)


def main():
    ihm.layout()


if __name__ == main():
    main()
