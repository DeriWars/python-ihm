import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


def bouton_clique(bouton):
    print(bouton.text(), "est cliqué")

app = QApplication(sys.argv)

window = QWidget()

boite = QHBoxLayout()

bouton1 = QRadioButton("Premier")
bouton2 = QRadioButton("Deuxième")

bouton1.clicked.connect(lambda: bouton_clique(bouton1))
bouton2.clicked.connect(lambda: bouton_clique(bouton2))

boite.addWidget(bouton1)
boite.addWidget(bouton2)

#bouton2.setChecked(True)

window.setLayout(boite)

window.show()

sys.exit(app.exec())
