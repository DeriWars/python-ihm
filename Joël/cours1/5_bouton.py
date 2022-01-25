import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

app = QApplication(sys.argv)

window = QDialog()
window.setGeometry(0, 0, 200, 200)  # permet de postionner la fenetre et forcer la taille et le placement

bouton1 = QPushButton(window)
bouton1.setText("Nom")

bouton2 = QPushButton(window)
bouton2.setText("Age")
bouton2.move(0, 30)

bouton3 = QPushButton(window)
bouton3.move(0, 60)

### si on veut connecter nos boutons ###


def bouton1_clique():
    bouton3.setText("Cliqué 1")
    print("Tu as cliqué sur 1!")


def bouton2_clique():
    bouton3.setText("Cliqué 2")
    print("Tu as cliqué sur 2!")


bouton1.clicked.connect(bouton1_clique)
bouton2.clicked.connect(bouton2_clique)

window.show()
sys.exit(app.exec())
