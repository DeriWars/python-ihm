import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

app = QApplication(sys.argv)

window = QDialog()
window.setGeometry(0, 0, 200, 200)

label1 = QLabel(window)
label1.setText("Label 1")

label2 = QLabel("Label 2", window)

label2.move(0,20)

label3 = QLabel()
label3.setText("label 3")

label4 = QLabel("label 4")

boite = QVBoxLayout()

boite.addWidget(label3)
boite.addStretch()
boite.addWidget(label4)

label3.setAlignment(Qt.AlignCenter)
label4.setAlignment(Qt.AlignRight)


window.show()
sys.exit(app.exec())