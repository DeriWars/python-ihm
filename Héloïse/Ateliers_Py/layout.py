import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *



app = QApplication(sys.argv)

window = QWidget()

"""
bouton = QPushButton(window)
bouton.setText("Bouton")
bouton.move(100,100)
"""

label= QLabel(window)
"""
bouton.setText("Bouton")
bouton.move(100,100)


bouton1 = QPushButton("Premier")
bouton2= QPushButton("Deuxieme")
bouton3 = QPushButton("Troisieme")
bouton4= QPushButton("Quatrieme")



verticalBoxLayout = QVBoxLayout()
verticalBoxLayout.addWidget(bouton1)
verticalBoxLayout.addWidget(bouton2)

horizontalBoxLayout = QHBoxLayout()

horizontalBoxLayout.addWidget(bouton3)
horizontalBoxLayout.addStretch()
horizontalBoxLayout.addWidget(bouton4)

window.setLayout(verticalBoxLayout)


grille = QGridLayout()
grille.addWidget(bouton1,1,1)
grille.addWidget(bouton2,1,2)
grille.addWidget(bouton3,2,1)
grille.addWidget(bouton4,2,2)

window.setLayout(grille)

window.setGeometry(300,200,100,100)
"""

label1 = QLabel("Prénom")
input1 = QLineEdit()

label2 = QLabel("Nom")
input2 = QLineEdit()

questionnaire = QFormLayout()

questionnaire.addRow(label1,input1)
questionnaire.addRow(label2,input2)

label3 = QLabel("Adresse")
input3_1 = QLineEdit()
input3_2 = QLineEdit()

boite = QVBoxLayout()
boite.addWidget(input3_1)
boite.addWidget(input3_2)

questionnaire.addRow(label3,boite)
window.setLayout(questionnaire)
input2 = QLineEdit()




window.show()

sys.exit( app.exec())