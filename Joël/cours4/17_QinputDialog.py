import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

def entrer_nom():
    nom, ok = QInputDialog.getText(window,"Input Dialog","Entrez votre nom")
    if ok:
        ligne1.setReadOnly(False)
        ligne1.setText(nom)
        ligne1.setReadOnly(True)

def entrer_age():
    age, ok = QInputDialog.getInt(window,"Input Dialog","Entrez votre age",min=5)
    if ok:
        ligne2.setReadOnly(False)
        ligne2.setText(str(age))
        ligne2.setReadOnly(True)

def entrer_categorie():
    categories = ['Étudiant','Salarié','Retraité']
    categorie, ok = QInputDialog.getItem(window,"Input Dialog","Catégorie",categories,1,False)
    if ok:
        ligne3.setReadOnly(False)
        ligne3.setText(str(categorie))
        ligne3.setReadOnly(True)

app = QApplication(sys.argv)
window =  QWidget()
questionnaire = QFormLayout()

ligne1 = QLineEdit()
ligne1.setReadOnly(True)
bouton1 = QPushButton("Entrez votre nom")

bouton1.clicked.connect(entrer_nom)

ligne2 = QLineEdit()
ligne2.setReadOnly(True)
bouton2 = QPushButton("Entrez votre age")

bouton2.clicked.connect(entrer_age)

ligne3 = QLineEdit()
ligne3.setReadOnly(True)
bouton3 = QPushButton("Entrez une catégorie")

bouton3.clicked.connect(entrer_categorie)

questionnaire.addRow(bouton1,ligne1)
questionnaire.addRow(bouton2,ligne2)
questionnaire.addRow(bouton3,ligne3)

window.setLayout(questionnaire)
window.show()


sys.exit(app.exec())