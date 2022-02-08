import sys
# importing Widgtes
from PyQt5.QtWidgets import *
# importing Engine Widgets
from PyQt5.QtWebEngineWidgets import *
# importing QtCore to use Qurl
from PyQt5.QtCore import *

def definitions_words(word:str):
    app = QApplication(sys.argv)

    window = QWidget()
    window.showMaximized()
    browser = QWebEngineView()
    browser.setUrl(QUrl(f"https://www.larousse.fr/dictionnaires/francais/{word}"))
    layout = QGridLayout()
    layout.addWidget(browser)
    window.setLayout(layout)





    window.show()
    sys.exit(app.exec())

definitions_words("sourient")