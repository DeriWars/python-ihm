import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


def ombre(widget, color=None, radius=10):
    shadow = QGraphicsDropShadowEffect()

    # réglage du flou
    shadow.setBlurRadius(radius)
    if color is not None:
        shadow.setColor(QColor(color))

    # ajout de l'ombre au widget
    widget.setGraphicsEffect(shadow)


def bouton_clique(bouton, plateau, word_to_guess, label_word):
    bouton.setEnabled(False)
    if bouton.text() in word_to_guess:
        for index, lettre in enumerate(word_to_guess):
            if lettre == bouton.text():
                plateau[index] = bouton.text()
            else:
                errors += 1
    label_word.setText(plateau)



class Bouton(QPushButton):
    def __init__(self, label):
        super().__init__(label)
        self.clicked.connect(lambda: bouton_clique(self))
        ombre(self)

    """
    def add_widget(self, widget, pos_x, pos_y):
        widget.addWidget(self.bouton, pos_x, pos_y)
    """

