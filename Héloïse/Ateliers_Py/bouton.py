import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

app = QApplication(sys.argv)

window = QDialog()

window.setGeometry(0,0,800,500)
bouton1 = QPushButton(window)
bouton1.setText("nom")

#bouton1.setGeometry(0,0,200,100)

bouton2 = QPushButton(window)
bouton2.setText("âge")
bouton2.move(0,30) #pour pas que les noutns soient dessus l'un de l'autre pour
#bouton2.setGeometry(0,40,200,100)


# connectons nos boutons
bouton3 = QPushButton(window)
bouton3.setText("Pénom")
bouton3.move(0,60)

#bouton3.setGeometry(40,60,200,100)


def bouton1_clique():
    bouton1.setText(bouton1_clique)
    print("tu as cliqué sur bouton 1")

def bouton2_clique():
    bouton2.setText("cliqué 2")
    print("tu as cliqué sur bouton 2")

def bouton3_clique():
    bouton3.setText("Tu as cliqué sur le \n bouton3")
    print("tu as cliqué sur bouton 3")

bouton1.clicked.connect(bouton1_clique)
bouton2.clicked.connect(bouton2_clique)
bouton3.clicked.connect(bouton3_clique)




window.show()

sys.exit( app.exec())
