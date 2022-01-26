import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

def valeur_actuelle():
    print(spin.value())

app = QApplication(sys.argv)

window = QWidget()

boite = QVBoxLayout()

label = QLabel("Valeur")
label.setAlignment(Qt.AlignCenter)
spin = QSpinBox()

boite.addWidget(label)
boite.addWidget(spin)

spin.valueChanged.connect(valeur_actuelle)

window.setLayout(boite)
window.show()

sys.exit(app.exec())