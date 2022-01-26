import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

app = QApplication(sys.argv)

window = QWidget()

combo_box = QComboBox(window)

combo_box.addItem("Premier")

window.show()
sys.exit(app.exec())