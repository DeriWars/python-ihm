import string
import sys
from typing import Callable

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
app = QApplication(sys.argv)

window = QWidget()
window.setGeometry(0, 0, 420, 350)
window.setWindowTitle("Calculatrice")

input1 = QLineEdit()
input1.setMinimumSize(380, 50)
input1.setValidator(QDoubleValidator())
input1.setValidator(QRegExpValidator())
fenetre_commandes = QFormLayout()

fenetre_commandes.addRow(input1)
window.setLayout(fenetre_commandes)

boutoncoma = QPushButton(window)
boutoncoma.setText(".")
boutoncoma.move(100, 310)

boutonsupp = QPushButton(window)
boutonsupp.setText("del")
boutonsupp.move(190, 310)

bouton0 = QPushButton(window)
bouton0.setText("0")
bouton0.move(10, 310)

bouton1 = QPushButton(window)
bouton1.setText("1")
bouton1.move(10, 270)

bouton2 = QPushButton(window)
bouton2.setText("2")
bouton2.move(100, 270)

bouton3 = QPushButton(window)
bouton3.setText("3")
bouton3.move(190, 270)

bouton4 = QPushButton(window)
bouton4.setText("4")
bouton4.move(10, 230)

bouton5 = QPushButton(window)
bouton5.setText("5")
bouton5.move(100, 230)

bouton6 = QPushButton(window)
bouton6.setText("6")
bouton6.move(190, 230)

bouton7 = QPushButton(window)
bouton7.setText("7")
bouton7.move(10, 190)

bouton8 = QPushButton(window)
bouton8.setText("8")
bouton8.move(100, 190)

bouton9 = QPushButton(window)
bouton9.setText("9")
bouton9.move(190, 190)

boutonmul = QPushButton(window)
boutonmul.setText("x")
boutonmul.move(300, 190)

boutondiv = QPushButton(window)
boutondiv.setText("/")
boutondiv.move(300, 150)

boutonadd = QPushButton(window)
boutonadd.setText("+")
boutonadd.move(300, 270)

boutonsub = QPushButton(window)
boutonsub.setText("-")
boutonsub.move(300, 230)

boutonequal = QPushButton(window)
boutonequal.setText("=")
boutonequal.move(300, 310)

boutonln = QPushButton(window)
boutonln.setText("ln")
boutonln.move(10, 70)

boutonexp = QPushButton(window)
boutonexp.setText("e")
boutonexp.move(100, 70)

boutonlog = QPushButton(window)
boutonlog.setText("log")
boutonlog.move(190, 70)

boutoncos = QPushButton(window)
boutoncos.setText("cos")
boutoncos.move(10, 110)

boutonsin = QPushButton(window)
boutonsin.setText("sin")
boutonsin.move(100, 110)

boutontan = QPushButton(window)
boutontan.setText("tan")
boutontan.move(190, 110)

boutonparg = QPushButton(window)
boutonparg.setText("(")
boutonparg.move(10, 150)

boutonpard = QPushButton(window)
boutonpard.setText(")")
boutonpard.move(100, 150)

boutonsqrt = QPushButton(window)
boutonsqrt.setText("√")
boutonsqrt.move(190, 150)

boutonpow = QPushButton(window)
boutonpow.setText("^")
boutonpow.move(300, 110)


bouton0_clique = lambda: input1.insert("0")
bouton1_clique = lambda: input1.insert("1")
bouton2_clique = lambda: input1.insert("2")
bouton3_clique = lambda: input1.insert("3")
bouton4_clique = lambda: input1.insert("4")
bouton5_clique = lambda: input1.insert("5")
bouton6_clique = lambda: input1.insert("6")
bouton7_clique = lambda: input1.insert("7")
bouton8_clique = lambda: input1.insert("8")
bouton9_clique = lambda: input1.insert("9")
boutoncoma_clique = lambda: input1.insert(".")
boutonadd_clique = lambda: input1.insert("+")
boutonsub_clique = lambda: input1.insert("-")
boutonmul_clique = lambda: input1.insert("*")
boutondiv_clique = lambda: input1.insert("/")
boutonsupp_clique = lambda : input1.clear()
boutonparg_clique = lambda : input1.insert("(")
boutonpard_clique = lambda : input1.insert(")")
boutonln_clique = lambda : input1.insert("log(")
boutone_clique = lambda : input1.insert("exp(")
boutonlog_clique = lambda : input1.insert("log10(")
boutoncos_clique = lambda : input1.insert("cos(")
boutonsin_clique = lambda : input1.insert("sin(")
boutontan_clique = lambda : input1.insert("tan(")
boutonsqrt_clique = lambda : input1.insert("sqrt(")
boutonpow_clique = lambda : input1.insert("**")

def boutonequal_clique():
    try:
        from math import log, log10, sqrt, exp, cos, sin, tan
        a = str(eval(input1.text()))
        input1.clear()
        input1.insert(str(float(a)))
    except:
        input1.clear()
        return input1.insert("Erreur")



bouton0.clicked.connect(bouton0_clique)
bouton1.clicked.connect(bouton1_clique)
bouton2.clicked.connect(bouton2_clique)
bouton3.clicked.connect(bouton3_clique)
bouton4.clicked.connect(bouton4_clique)
bouton5.clicked.connect(bouton5_clique)
bouton6.clicked.connect(bouton6_clique)
bouton7.clicked.connect(bouton7_clique)
bouton8.clicked.connect(bouton8_clique)
bouton9.clicked.connect(bouton9_clique)
boutonadd.clicked.connect(boutonadd_clique)
boutonsub.clicked.connect(boutonsub_clique)
boutonmul.clicked.connect(boutonmul_clique)
boutondiv.clicked.connect(boutondiv_clique)
boutoncoma.clicked.connect(boutoncoma_clique)
boutonequal.clicked.connect(boutonequal_clique)
boutonsupp.clicked.connect(boutonsupp_clique)
boutonparg.clicked.connect(boutonparg_clique)
boutonpard.clicked.connect(boutonpard_clique)
boutonexp.clicked.connect(boutone_clique)
boutonln.clicked.connect(boutonln_clique)
boutonlog.clicked.connect(boutonlog_clique)
boutoncos.clicked.connect(boutoncos_clique)
boutonsin.clicked.connect(boutonsin_clique)
boutontan.clicked.connect(boutontan_clique)
boutonsqrt.clicked.connect(boutonsqrt_clique)
boutonpow.clicked.connect(boutonpow_clique)

print(string.ascii_lowercase)

window.show()
sys.exit(app.exec())
