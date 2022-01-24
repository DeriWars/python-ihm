import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

app = QApplication(sys.argv)

window = QWidget()
window.setGeometry(0, 0, 200, 200)  # permet de postionner la fenetre et forcer la taille et le placement

# deux méthode pour faire un label :
# 1/
label1 = QLabel(window)
label1.setText("label1")

# 2/
label2 = QLabel("label 2", window)
label2.move(0, 20)

# Avec une vbox
label3 = QLabel()
label3.setText("label 3")

label4 = QLabel("label 4")

boite = QHBoxLayout()

boite.addWidget(label3)
boite.addStretch()  # ajoute un espace
boite.addWidget(label4)

label3.setAlignment(Qt.AlignCenter)
label4.setAlignment(Qt.AlignRight)
window.setLayout(boite)

window.show()
sys.exit(app.exec())
