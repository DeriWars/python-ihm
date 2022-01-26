import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


########## Fonctions ############

def valeur():
    print(slider.value())


def presse():
    print("Le slider est sélectionné")


def bouge():
    print("le slider est en train de bouger")


def libere():
    print("le slider est libéré")


#################################

app = QApplication(sys.argv)

window = QWidget()
window.setGeometry(0, 0, 200, 200)

slider = QSlider(window)
slider2 = QSlider(Qt.Horizontal, window)
slider2.move(0, 100)

# Par défaut les valeurs sont entre 0 et 99
slider.setValue(50)

# changer les valeurs de début et de fin
slider.setMinimum(10)
slider.setMaximum(60)

# pour rajouter une graduation
slider.setTickPosition(QSlider.TicksBothSides)  # TicksBelow, etc...
slider2.setTickPosition(QSlider.TicksBelow)
slider.setTickInterval(20)


###### Récupération des valeurs ################
slider.valueChanged.connect(valeur)

##### curseur pressé ######################
slider.sliderPressed.connect(presse)

###### le slider bouge ############
slider.sliderMoved.connect(bouge)

###### le slider est relaché ########
slider.sliderReleased.connect(libere)


window.show()
sys.exit(app.exec())
