import string
import sys
from PyQt5 import QtCore
from PyQt5 import QtWidgets
from time import sleep

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QScrollArea, QVBoxLayout, QLabel, QApplication

"""
DURATION_INT = 15


class MyMainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.time_left_int = DURATION_INT
        self.widget_counter_int = 0

        central_widget = QtWidgets.QWidget()
        self.setCentralWidget(central_widget)
        vbox = QtWidgets.QVBoxLayout()
        central_widget.setLayout(vbox)

        self.pages_qsw = QtWidgets.QStackedWidget()
        vbox.addWidget(self.pages_qsw)
        self.time_passed_qll = QtWidgets.QLabel()
        vbox.addWidget(self.time_passed_qll)

        self.widget_one = QtWidgets.QLabel("This is widget one")
        self.pages_qsw.addWidget(self.widget_one)
        self.widget_two = QtWidgets.QLabel("This is widget two")
        self.pages_qsw.addWidget(self.widget_two)
        self.widget_three = QtWidgets.QLabel("This is widget three")
        self.pages_qsw.addWidget(self.widget_three)
        self.widget_four = QtWidgets.QLabel("This is widget four")
        self.pages_qsw.addWidget(self.widget_four)

        self.timer_start()
        self.update_gui()

    def timer_start(self):
        self.time_left_int = DURATION_INT

        self.my_qtimer = QtCore.QTimer(self)
        self.my_qtimer.timeout.connect(self.timer_timeout)
        self.my_qtimer.start(1000)

        self.update_gui()

    def timer_timeout(self):
        self.time_left_int -= 1

        if self.time_left_int == 0:
            self.widget_counter_int = (self.widget_counter_int + 1) % 4
            self.pages_qsw.setCurrentIndex(self.widget_counter_int)
            self.time_left_int = DURATION_INT

        self.update_gui()

    def update_gui(self):
        self.time_passed_qll.setText(str(self.time_left_int))


app = QtWidgets.QApplication(sys.argv)
main_window = MyMainWindow()
main_window.show()
sys.exit(app.exec_())"""
"""
def calculo():
    global time
    time = time.addSecs(1)
    print(time.toString("hh:mm:ss"))
    if time.toString("hh:mm:ss") == "00:00:04":
        print("eeee conar")


app = QtCore.QCoreApplication(sys.argv)

timer0 = QtCore.QTimer()
time = QtCore.QTime(0, 0, 0)
timer0.setInterval(1000)
timer0.timeout.connect(calculo)
timer0.start()


sys.exit(app.exec_())

"""
"""
import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QListWidget, QGridLayout, QLabel
from PyQt5.QtCore import QTimer, QDateTime


class WinForm(QWidget):
    def __init__(self, parent=None):
        super(WinForm, self).__init__(parent)
        self.setWindowTitle('QTimer example')

        self.listFile = QListWidget()
        self.label = QLabel('Label')
        self.startBtn = QPushButton('Start')
        self.endBtn = QPushButton('Stop')

        layout = QGridLayout()

        self.timer = QTimer()
        self.timer.timeout.connect(self.showTime)

        layout.addWidget(self.label, 0, 0, 1, 2)
        layout.addWidget(self.startBtn, 1, 0)
        layout.addWidget(self.endBtn, 1, 1)

        self.startBtn.clicked.connect(self.startTimer)
        self.endBtn.clicked.connect(self.endTimer)

        self.setLayout(layout)

    def showTime(self):
        time = QDateTime.currentDateTime()
        timeDisplay = time.toString('yyyy-MM-dd hh:mm:ss dddd')
        self.label.setText(timeDisplay)

    def startTimer(self):
        self.timer.start(1000)
        self.startBtn.setEnabled(False)
        self.endBtn.setEnabled(True)

    def endTimer(self):
        self.timer.stop()
        self.startBtn.setEnabled(True)
        self.endBtn.setEnabled(False)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = WinForm()
    form.show()
    sys.exit(app.exec_())
"""

"""d = dict()
d["a"] = 5
d["b"] = 2
d["c"] = 10
print(d)
e = sorted(d.items(), key=lambda x: x[1], reverse=True)
print(e)
print(type(e))
print(dict(e))"""

"""d = {'DeriWars': 10000000, 'Test': 200000000000, 'maxou': 0, 'Maxime': 0, 'Nat': 0, 'Mars': 0, 'Trey Thomas': 0, 'machine': 0, 'moi': 0, 'King': 0, 'jojo': 0, 'a': 0, 'testttt': 0, 'teste': 0}
e = sorted(d.items(), key=lambda x: x[1], reverse=True)
print(dict(e))
pseudos, scores = "", ""
for username, score in dict(e):
    pseudos += username + "\n"
    scores += str(score) + "\n"
print(pseudos, scores)
"""

"""import time
import datetime


# Create class that acts as a countdown
def countdown(h, m, s):
    # Calculate the total number of seconds
    total_seconds = h * 3600 + m * 60 + s

    # While loop that checks if total_seconds reaches zero
    # If not zero, decrement total time by one second
    while total_seconds > 0:
        # Timer represents time left on countdown
        timer = datetime.timedelta(seconds=total_seconds)

        # Prints the time left on the timer
        print(timer, end="\r")

        # Delays the program one second
        time.sleep(1)

        # Reduces total time by one second
        total_seconds -= 1

    print("Bzzzt! The countdown is at zero seconds!")


# Inputs for hours, minutes, seconds on timer
h = input("Enter the time in hours: ")
m = input("Enter the time in minutes: ")
s = input("Enter the time in seconds: ")
countdown(int(h), int(m), int(s))"""

"""from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWidgets import QApplication
import sys

#champion = input("What champion would you like to check? ")
champions = "Katarina"
#role = input("What role are you playing (Middle, Jungle, Top, ADC, Support)? ")
roles = "Middle"
URL = f"google.com"

app = QApplication(sys.argv)

web = QWebEngineView()
web.load(QUrl(URL))
web.show()

sys.exit(app.exec_())"""
"""import sys
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
        self.browser.setUrl(QUrl('http://google.com'))
        # to display google search engine on our browser
        self.setCentralWidget(self.browser)
        # -------------------full screen mode------------------
        # to display browser in full screen mode, you may comment below line if you don't want to open your browser in full screen mode
        self.showMaximized()
        # ----------------------navbar-------------------------
        # creating a navigation bar for the browser
        navbar = QToolBar()
        # adding created navbar
        self.addToolBar(navbar)
        # -----------------prev Button-----------------
        # creating prev button
        prevBtn = QAction('Prev', self)
        # when triggered set connection
        prevBtn.triggered.connect(self.browser.back)
        # adding prev button to the navbar
        navbar.addAction(prevBtn)
        # -----------------next Button---------------
        nextBtn = QAction('Next', self)
        nextBtn.triggered.connect(self.browser.forward)
        navbar.addAction(nextBtn)
        # -----------refresh Button--------------------
        refreshBtn = QAction('Refresh', self)
        refreshBtn.triggered.connect(self.browser.reload)
        navbar.addAction(refreshBtn)
        # -----------home button----------------------
        homeBtn = QAction('Home', self)
        # when triggered call home method
        homeBtn.triggered.connect(self.home)
        navbar.addAction(homeBtn)
        # ---------------------search bar---------------------------------
        # to maintain a single line
        self.searchBar = QLineEdit()
        # when someone presses return(enter) call loadUrl method
        self.searchBar.returnPressed.connect(self.loadUrl)
        # adding created seach bar to navbar
        navbar.addWidget(self.searchBar)
        # if url in the searchBar is changed then call updateUrl method
        self.browser.urlChanged.connect(self.updateUrl)

    # method to navigate back to home page
    def home(self):
        self.browser.setUrl(QUrl('http://google.com'))

    # method to load the required url
    def loadUrl(self):
        # fetching entered url from searchBar
        url = self.searchBar.text()
        # loading url
        self.browser.setUrl(QUrl(url))

    # method to update the url
    def updateUrl(self, url):
        # changing the content(text) of searchBar
        self.searchBar.setText(url.toString())


MyApp = QApplication(sys.argv)
# setting application name
QApplication.setApplicationName('TechVidvan Web Browser')
# creating window
window = Window()
# executing created app
MyApp.exec_()
"""
from time import *
time1 = time()
sleep(5)
time2 = time()
print(time2-time1)