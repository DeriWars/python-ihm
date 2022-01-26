import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


def select_ou_pas(bouton):
    if bouton.text() == "Premier":
        if bouton.isChecked():
            print("Premier est sélectionné")
        else:
            print("Premier est désélectionné")
    else:
        if bouton.isChecked():
            print("Deuxième est sélectionné")
        else:
            print("Deuxième est désélectionné")


app = QApplication(sys.argv)

window = QWidget()

boite = QHBoxLayout()
bouton1 = QCheckBox("Premier")
bouton2 = QCheckBox("Deuxième")

boite.addWidget(bouton1)
boite.addWidget(bouton2)

bouton1.stateChanged.connect(lambda: select_ou_pas(bouton1))
bouton2.stateChanged.connect(lambda: select_ou_pas(bouton2))


window.setLayout(boite)

window.show()
sys.exit(app.exec())
