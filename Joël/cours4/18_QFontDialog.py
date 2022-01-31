import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

def choisir_police():
    police, ok = QFontDialog.getFont()
    if ok:
        label.setFont(police)

app = QApplication(sys.argv)

window =  QWidget()

boite = QVBoxLayout()

bouton = QPushButton("Sélectionner une police :")
bouton.clicked.connect(choisir_police)

label = QLabel("Voici la police choisie")

boite.addWidget(bouton)
boite.addWidget(label)

window.setLayout(boite)
window.show()


sys.exit(app.exec())