import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

app = QApplication(sys.argv)

window = QWidget()

window.setGeometry(0,0, 200, 200)

label = QLabel(window)
label.setText("Ma première appli")

window.show()

sys.exit(app.exec())