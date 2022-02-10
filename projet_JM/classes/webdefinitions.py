import sys
# importing Widgets
from PyQt5.QtWidgets import QWidget, QGridLayout
# pip install PyQTWebEngine
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtCore import QUrl


class WebDef:
    """
    Class for create a window with the definition of the word chosen
    """
    def __init__(self):
        self.window = None

    def definition_word(self, word: str):
        """
        Function that allows the creation of the window
        :param word: the word that the player needs to guess
        """
        self.window = QWidget()
        self.window.resize(1000, 1000)
        self.window.setWindowTitle(f"Définiton du mot {word}")
        browser = QWebEngineView()
        browser.setUrl(QUrl(f"https://www.larousse.fr/dictionnaires/francais/{word}"))
        layout = QGridLayout()
        layout.addWidget(browser)
        self.window.setLayout(layout)
        self.window.show()
