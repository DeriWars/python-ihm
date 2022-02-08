import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

operateurs = {type(0):{'+':int.__add__,'-':int.__sub__,'x':int.__mul__},
                   type(0.0):{'+':float.__add__,'-':float.__sub__,'x':float.__mul__,'/':float.__truediv__}}


def reset():
    resultat.setText('')
    resultat.precedent_op = ''
    resultat.pile = 0

def valeur(b):
    print(b.text())

def affiche(b):
    if resultat.precedent_op == '=':
        reset()
    valeur = b.text()
    cur_res = resultat.text()
    resultat.setText(cur_res + valeur)

def stock_op(b):
    nouveau_operateur = b.text()
    operateur = resultat.precedent_op
    if resultat.text() == '':
        return None
    nouveau_nombre = eval(resultat.text())
    valeur_prec = resultat.pile
    if operateur != '' and operateur != '=':
        if type(nouveau_nombre) == float or type(resultat.pile) == float or operateur == '/':
            resultat.pile = operateurs[type(0.0)][operateur](float(valeur_prec),float(nouveau_nombre))
        else:
            resultat.pile = operateurs[type(0)][operateur](valeur_prec, nouveau_nombre)
    else:
        resultat.pile = nouveau_nombre
        resultat.precedent_op = nouveau_operateur
    resultat.setText('')


def egal():
    nouveau_nombre = eval(resultat.text())
    valeur_prec = resultat.pile
    operateur = resultat.precedent_op
    if operateur != '':
        if type(nouveau_nombre) == float or type(resultat.pile) == float or operateur == '/':
            resultat.pile = operateurs[type(0.0)][operateur](float(valeur_prec),float(nouveau_nombre))
        else:
            resultat.pile = operateurs[type(0)][operateur](valeur_prec, nouveau_nombre)
    resultat.setText(str(resultat.pile))
    resultat.precedent_op = '='



app = QApplication(sys.argv)
window =  QWidget()

vbox_totale = QVBoxLayout()

grid = QGridLayout()




"""
for i in range (1,10):
    boutons.append(QPushButton(str(i)))

for i in range(9):
    grid.addWidget(boutons[i],i//3, i%3)
    boutons[i].clicked.connect(lambda:valeur(boutons[i]))
"""

class Resultat(QLineEdit):
    def __init__(self):
        super().__init__()
        self.pile = 0
        self.precedent_op = ''

class Mon_bouton(QPushButton):
    def __init__(self,label):
        super().__init__(label)
        self.clicked.connect(lambda:valeur(self))
        self.clicked.connect(lambda:affiche(self))

class Mon_bouton_op(QPushButton):
    def __init__(self,label):
        super().__init__(label)
        self.clicked.connect(lambda:valeur(self))
        self.clicked.connect(lambda:stock_op(self))

boutons = []

for i in range (1,10):
    boutons.append(Mon_bouton(str(i)))

for i in range(9):
    grid.addWidget(boutons[i],i//3, i%3)

boutons_op = []

for operateur in operateurs[type(0.0)].keys():
    boutons_op.append(Mon_bouton_op(operateur))

vbox_op = QVBoxLayout()

for bouton_op in boutons_op:
    vbox_op.addWidget(bouton_op)

bouton_egal = QPushButton("=")
bouton_egal.clicked.connect(egal)

bouton_point = Mon_bouton(".")
vbox_op.addWidget(bouton_point)

bouton_reset = QPushButton("CE")
bouton_reset.clicked.connect(reset)



resultat = Resultat()

vbox_totale.addWidget(resultat)
vbox_totale.addWidget(bouton_reset)
vbox_totale.addLayout(grid)
vbox_totale.addLayout(vbox_op)
vbox_totale.addWidget(bouton_egal)

window.setLayout(vbox_totale)
window.show()


sys.exit(app.exec())
