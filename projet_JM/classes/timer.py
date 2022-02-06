import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QListWidget, QGridLayout, QLabel
from PyQt5.QtCore import QTimer, QDateTime


class Timer(QTimer):
    def __init__(self, label_time, label_word, input):
        super().__init__()
        self.label_time = label_time
        self.label_word = label_word
        self.input = input

    def timer(self, lose_label, buttons_list, disable_input):
        """
        Function used to print the timer in the layout
        :param label_time:
        :param label_word:
        :param input:
        """
        self.time = self.addSecs(1)
        self.label_time.setText(self.time.toString("hh:mm:ss"))
        if self.time.toString("hh:mm:ss") == "00:01:00":
            lose_label(self.label_word, input, buttons_list, self.word, disable_input)
            self.time = self.time.addSecs(-1)
            # self.time.stop()
            print(self.time.toString("hh:mm:ss"))
        elif self.label_word.text() == f"\n---- Victoire du joueur ----\nLe bon mot était : {self.word}" or self.label_word.text() == f"\n---- GAME OVER ---- \nLe bon mot était : {self.word}":
            # self.time.stop()
            self.time = self.time.addSecs(-1)
            print(self.time.toString("hh:mm:ss"))


