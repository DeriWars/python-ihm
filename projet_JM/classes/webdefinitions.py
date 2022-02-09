import sys
# importing Widgtes
from PyQt5.QtWidgets import *
# importing Engine Widgets
from PyQt5.QtWebEngineWidgets import *
# importing QtCore to use Qurl
from PyQt5.QtCore import *


class WebDef:
    def __init__(self):
        pass

    def definition_word(self, word: str):
        self.window = QWidget()
        self.window.resize(1000, 1000)
        self.window.setWindowTitle(f"Définiton du mot {word}")
        browser = QWebEngineView()
        browser.setUrl(QUrl(f"https://www.larousse.fr/dictionnaires/francais/{word}"))
        layout = QGridLayout()
        layout.addWidget(browser)
        self.window.setLayout(layout)
        self.window.show()
