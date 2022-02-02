import string
import sys
from PyQt5 import QtCore
from PyQt5 import QtWidgets
from time import sleep

"""DURATION_INT = 3


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