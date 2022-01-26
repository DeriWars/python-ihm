import sys
from PyQt5.QtWidgets import *

app = QApplication(sys.argv)

window = QDialog()
window.setGeometry(0, 0, 200, 200)

bouton1 = QPushButton(window)
bouton1.setText("Nom")

bouton2 = QPushButton(window)
bouton2.setText("âge")
bouton2.move(0, 30)

bouton3 = QPushButton(window)
bouton3.move(0, 60)


def bouton1_clique():
    bouton3.setText("cliqué 1")
    print("tu as cliqué")


def bouton2_clique():
    bouton3.setText("cliqué 2")
    print("tu as cliqué 2")


bouton1.clicked.connect(bouton1_clique)
bouton2.clicked.connect(bouton2_clique)

window.show()
sys.exit(app.exec())
