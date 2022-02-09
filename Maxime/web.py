import sys
# importing Widgtes
from PyQt5.QtWidgets import *
# importing Engine Widgets
from PyQt5.QtWebEngineWidgets import *
# importing QtCore to use Qurl
from PyQt5.QtCore import *



# main window class (to create a window)-sub class of QMainWindow class
class Window(QMainWindow):
    # defining constructor function
    def __init__(self):
        # creating connnection with parent class constructor
        super(Window, self).__init__()
        # ---------------------adding browser-------------------
        self.browser = QWebEngineView()
        # setting url for browser, you can use any other url also
        self.browser.setUrl(QUrl('https://www.larousse.fr/dictionnaires/'))
        # to display google search engine on our browser
        self.setCentralWidget(self.browser)
        # -------------------full screen mode------------------
        # to display browser in full screen mode, you may comment below line if you don't want to open your browser in full screen mode
        self.showMaximized()
        # ----------------------navbar-------------------------
        # creating a navigation bar for the browser
        self.get_definition(self.word)
        self.show()

    def get_definition(self, word):
        self.browser.setUrl(QUrl(f"https://www.larousse.fr/dictionnaires/francais/{word}"))

    # method to navigate back to home page


