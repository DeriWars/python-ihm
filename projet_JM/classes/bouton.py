import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


def shadow(widget, color=None, radius=10):
    shade = QGraphicsDropShadowEffect()

    # réglage du flou
    shade.setBlurRadius(radius)
    if color is not None:
        shade.setColor(QColor(color))

    # ajout de l'ombre au widget
    widget.setGraphicsEffect(shade)


def button_click(button, label_word, top_grid_layout, game, input):
    button.setEnabled(False)
    game(button, label_word, top_grid_layout, input)


def disable_buttons(buttons_list):
    for button in buttons_list:
        button.setEnabled(False)


class Button(QPushButton):
    def __init__(self, label, label_word, top_grid_layout, game, input):
        super().__init__(label)
        self.clicked.connect(lambda: button_click(self, label_word, top_grid_layout, game, input))
        shadow(self)
