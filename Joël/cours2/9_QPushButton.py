import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


#### Fonctions ####

def bouton_clique(bouton):
    print(bouton.text(), "est cliqué")


def presse_relache(bouton):
    if bouton.isChecked():
        print("le bouton a été préssé")
    else:
        print("le bouton a été relaché")
####################################

app = QApplication(sys.argv)

dialog = QDialog()
boite = QVBoxLayout(dialog)

bouton1 = QPushButton("premier")
bouton2 = QPushButton("deuxième")
bouton3 = QPushButton("trosième")

bouton1.clicked.connect(lambda: bouton_clique(bouton1))
bouton2.clicked.connect(lambda: bouton_clique(bouton2))
bouton3.clicked.connect(lambda: bouton_clique(bouton3))

boite.addWidget(bouton1)
boite.addWidget(bouton2)
boite.addWidget(bouton3)

# Pour changer le bouton par défaut

bouton3.setDefault(True)

# Désactiver un bouton

bouton2.setEnabled(False)

# Voir le statut du bouton

bouton1.clicked.connect(lambda: presse_relache(bouton1))


dialog.show()

sys.exit(app.exec())
