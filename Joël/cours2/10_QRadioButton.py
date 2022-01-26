import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


### fonction ####
def bouton_clique(bouton):
    print(bouton.text(), "est cliqué")


def radio_verif_2(bouton):
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


##################

app = QApplication(sys.argv)

window = QWidget()

boite = QHBoxLayout()

bouton1 = QRadioButton("Premier")
bouton2 = QRadioButton("Deuxième")

boite.addWidget(bouton1)
boite.addWidget(bouton2)

### pour pré-selectionner un bouton ####

bouton2.setChecked(True)

"""
bouton1.clicked.connect(lambda: bouton_clique(bouton1))
bouton2.clicked.connect(lambda: bouton_clique(bouton2))
"""

bouton1.toggled.connect(lambda: radio_verif_2(bouton1))
bouton2.toggled.connect(lambda: radio_verif_2(bouton2))

window.setLayout(boite)

window.show()
sys.exit(app.exec())
