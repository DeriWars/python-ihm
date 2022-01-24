import sys
from PyQt5.QtWidgets import *

app = QApplication(sys.argv)

window = QDialog()
window.setGeometry(0, 0, 200, 200)


"""
bouton = QPushButton(window)
bouton.setText("Bouton")
bouton.move(100,100)


bouton1 = QPushButton("Premier")
bouton2 = QPushButton("Deuxieme")

verticalBoxLayout = QVBoxLayout()

verticalBoxLayout.addWidget(bouton1)
verticalBoxLayout.addWidget(bouton2)

window.setLayout(verticalBoxLayout)
"""
bouton3 = QPushButton("troisieme")
bouton4 = QPushButton("quatrieme")

horizontalBoxLayout = QHBoxLayout()
horizontalBoxLayout.addWidget(bouton3)
horizontalBoxLayout.addStretch()
horizontalBoxLayout.addWidget(bouton4)

window.setLayout(horizontalBoxLayout)



window.show()
sys.exit(app.exec())

