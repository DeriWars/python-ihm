import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


##############  Fonctions  ##############

def solution_un(combo):
    print(combo.currentText())


def solution_deux():
    print(combo_box.currentIndex(), " est l'index courant")
    print("La sélection est : ", combo_box.currentText())

####################################


app = QApplication(sys.argv)

window = QWidget()

combo_box = QComboBox(window)

combo_box.addItem("Premier")
combo_box.addItems(["Deuxieme", "Troisieme"])

###### récupérer l'information #########@####

### première façon #####
combo_box.currentIndexChanged.connect(lambda: solution_un(combo_box))

### Deuxième façon #####
combo_box.currentIndexChanged.connect(solution_deux)

window.show()
sys.exit(app.exec())
