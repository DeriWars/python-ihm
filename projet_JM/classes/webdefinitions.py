import sys
# importing Widgets
from PyQt5.QtWidgets import *
# importing Engine Widgets
# is it necessary to install QTWebEngine with
# pip install PyQTWebEngine
from PyQt5.QtWebEngineWidgets import *
# importing QtCore to use Qurl
from PyQt5.QtCore import *


class WebDef:
    def __init__(self):
        self.window = None

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
