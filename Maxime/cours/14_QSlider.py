import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

app = QApplication(sys.argv)

window = QWidget()
window.setGeometry(0,0, 200, 200)
slider = QSlider(window)

# Mettre la valeur par défaut à 6
slider.setValue(6)

# changer les valeurs de début et de fin

slider.setMinimum(5)
slider.setMaximum(15)

# pour rajouter une graduation
slider.setTickPosition(QSlider.TicksBothSides)


window.show()
sys.exit(app.exec())