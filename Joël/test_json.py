import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Window(QScrollArea):
    def __init__(self):
        super(Window, self).__init__()
        self.widget = QWidget()
        self.resize(100, 100)
        layout = QVBoxLayout(self.widget)
        layout.setAlignment(Qt.AlignTop)
        layout.addWidget(QLineEdit())
        layout.addWidget(QLineEdit())
        layout.addWidget(QLineEdit())
        layout.addWidget(QLineEdit())
        layout.addWidget(QLineEdit())
        layout.addWidget(QLineEdit())
        layout.addWidget(QLineEdit())
        layout.addWidget(QLineEdit())
        layout.addWidget(QLineEdit())
        layout.addWidget(QLineEdit())

        self.setWidget(self.widget)
        self.setWidgetResizable(True)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    sys.exit(app.exec_())

