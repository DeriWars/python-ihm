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


def bouton_clique(bouton, label_word, top_grid_layout, game):
    bouton.setEnabled(False)
    game(bouton, label_word, top_grid_layout)


class Bouton(QPushButton):
    def __init__(self, label, label_word, top_grid_layout, game):
        super().__init__(label)
        self.clicked.connect(lambda: bouton_clique(self, label_word, top_grid_layout, game))
        ombre(self)


