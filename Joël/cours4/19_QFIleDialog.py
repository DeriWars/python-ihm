import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


def ouvrir_texte():
    fichiers = QFileDialog()
    fichiers.setFileMode(QFileDialog.AnyFile)
    fichiers.setNameFilter("Fichiers textes (*.txt)")

    liste_fichiers = QStringListModel()
    if fichiers.exec_():
        liste_fichiers = fichiers.selectedFiles()
        f = open(liste_fichiers[0],'r')
        label1.setText(f.read())

def ouvrir_image():
    nom_image = QFileDialog.getOpenFileName(window,
                                            "Ouvrez une image",
                                            "/Users/vrabiet/Downloads/",
                                            "Fichiers images (*.jpg *.png *.jpeg)"
                                            )
    label2.setPixmap(QPixmap(nom_image[0]))

app = QApplication(sys.argv)

window =  QWidget()

boite = QVBoxLayout()

bouton1 = QPushButton("Choisissez le texte")
bouton1.clicked.connect(ouvrir_texte)
label1 = QLabel("Mon label")
boite.addWidget(bouton1)
boite.addWidget(label1)


bouton2 = QPushButton("Choisissez votre image")
bouton2.clicked.connect(ouvrir_image)
label2 = QLabel("Mon label")


label3 = QLabel()
label3.setPixmap(QPixmap('/Users/vrabiet/Downloads/abacus-gd9668c8f1_1920.jpg'))


boite.addWidget(bouton2)
boite.addWidget(label2)
boite.addWidget(label3)
window.setLayout(boite)

window.show()


sys.exit(app.exec())