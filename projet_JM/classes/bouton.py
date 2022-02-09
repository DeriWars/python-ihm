import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


def shadow(widget, color=None, radius=10):
    """
    Function to add some shadow to the buttons
    :param widget: the wiget where we will set the effets
    :param color: the color of the shadow
    :param radius: the number use for set the blur
    """
    shade = QGraphicsDropShadowEffect()

    # réglage du flou
    shade.setBlurRadius(radius)
    if color is not None:
        shade.setColor(QColor(color))

    # ajout de l'ombre au widget
    widget.setGraphicsEffect(shade)


def button_click(button, label_word, top_grid_layout, game, input, word, score_button, def_word_button):
    """
    Function to define what to do when a button is pressed
    :param button: a button
    :param label_word: the label where is the word to guess
    :param top_grid_layout: a layout
    :param game: a function which manages the hangman
    :param input: the area where the user can enter a word
    :param word: the word to guess
    :param score_button: the score button
    """
    button.setEnabled(False)
    game(button, label_word, top_grid_layout, input, word, score_button, def_word_button)
    if button.text() in word:
        button.setStyleSheet("background-color : #7CF96F")
    else:
        button.setStyleSheet("background-color : #FB5952")


def disable_buttons(buttons_list):
    """
    Function which disable all the buttons of the list
    :param buttons_list: list of buttons
    """
    for button in buttons_list:
        button.setEnabled(False)


class Button(QPushButton):
    """
    Class for create the alphabet buttons and which connects them to the right function
    """
    def __init__(self, label, label_word, top_grid_layout, game, input, word, score_button, def_word_button):
        super().__init__(label)
        self.clicked.connect(lambda: button_click(self, label_word, top_grid_layout, game, input, word, score_button, def_word_button))
        shadow(self)
