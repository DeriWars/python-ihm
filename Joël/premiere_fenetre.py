import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

app = QApplication(sys.argv)

window = QWidget()
window.setGeometry(0, 0, 200, 200)  # permet de postionner la fenetre et forcer la taille et le placement

label = QLabel(window)  # on fait un label
label.setText("Ma première appli")  # on lui mets du texte

window.show()
sys.exit(app.exec())
