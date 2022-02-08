import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


def tab1():
    questionnaire = QFormLayout()
    label1 = QLabel("Prénom")
    ligne1 = QLineEdit()
    questionnaire.addRow(label1, ligne1)
    label2 = QLabel("Nom")
    ligne2 = QLineEdit()
    questionnaire.addRow(label2, ligne2)

    t1.setLayout(questionnaire)


def tab2():
    boite = QHBoxLayout()
    label1 = QCheckBox("Catégorie 1")
    label2 = QCheckBox("Catégorie 2")
    label3 = QCheckBox("Catégorie 3")

    boite.addWidget(label1)
    boite.addWidget(label2)
    boite.addWidget(label3)

    t2.setLayout(boite)


app = QApplication(sys.argv)

window = QTabWidget()

t1 = QWidget()
t2 = QWidget()

tab1()
tab2()

window.addTab(t1, "Tab 1")
window.addTab(t2, "Tab 2")

window.show()

sys.exit(app.exec())
