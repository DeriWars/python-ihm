import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


########## fonction ############

def valeur_actuelle():
    print(spin.value())


app = QApplication(sys.argv)

window = QWidget()

boite = QVBoxLayout()

label = QLabel("Valeur")
label.setAlignment(Qt.AlignCenter)

spin = QSpinBox()
# spin.setMinimum(5)
spin.setRange(5, 15)
spin.setPrefix('A')
spin.setSuffix('B')
spin.setSingleStep(3)
spin.setSpecialValueText('Par défaut')

boite.addWidget(label)
boite.addWidget(spin)

spin.valueChanged.connect(valeur_actuelle)

window.setLayout(boite)
window.show()


sys.exit(app.exec())
