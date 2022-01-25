import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from math import *

TEXT = ""
REP = "0"

app = QApplication(sys.argv)

# création de la fenêtre
window = QWidget()
window.setGeometry(250, 250, 300, 300)

# création de la zone d'écriture de la calculatrice
input1 = QLineEdit()
calc_layout = QFormLayout()
input1.setMinimumSize(300, 100)

calc_layout.addRow(input1)

# création des différents boutons de la calculatrice : utilisation d'un grid layout
bouton0 = QPushButton("0")
bouton1 = QPushButton("1")
bouton2 = QPushButton("2")
bouton3 = QPushButton("3")
bouton4 = QPushButton("4")
bouton5 = QPushButton("5")
bouton6 = QPushButton("6")
bouton7 = QPushButton("7")
bouton8 = QPushButton("8")
bouton9 = QPushButton("9")
bouton_point = QPushButton(".")
bouton_entrer = QPushButton("=")
bouton_plus = QPushButton("+")
bouton_moins = QPushButton("-")
bouton_fois = QPushButton("x")
bouton_diviser = QPushButton("/")
bouton_sin = QPushButton("sin")
bouton_cos = QPushButton("cos")
bouton_tan = QPushButton("tan")
bouton_del = QPushButton("suppr")
bouton_sqrt = QPushButton("sqrt")
bouton_ln = QPushButton("ln")
bouton_exp = QPushButton("exp")
bouton_p1 = QPushButton("(")
bouton_p2 = QPushButton(")")
bouton_pow = QPushButton("^")
bouton_rep = QPushButton("REP")

grille_calc = QGridLayout()

grille_calc.addWidget(bouton_ln, 1, 1)
grille_calc.addWidget(bouton_exp, 1, 2)
grille_calc.addWidget(bouton_sqrt, 1, 3)
grille_calc.addWidget(bouton_sin, 2, 1)
grille_calc.addWidget(bouton_cos, 2, 2)
grille_calc.addWidget(bouton_tan, 2, 3)
grille_calc.addWidget(bouton_pow, 2, 4)
grille_calc.addWidget(bouton_del, 3, 1)
grille_calc.addWidget(bouton_p1, 3, 2)
grille_calc.addWidget(bouton_p2, 3, 3)
grille_calc.addWidget(bouton_diviser, 3, 4)
grille_calc.addWidget(bouton7, 4, 1)
grille_calc.addWidget(bouton8, 4, 2)
grille_calc.addWidget(bouton9, 4, 3)
grille_calc.addWidget(bouton_fois, 4, 4)
grille_calc.addWidget(bouton4, 5, 1)
grille_calc.addWidget(bouton5, 5, 2)
grille_calc.addWidget(bouton6, 5, 3)
grille_calc.addWidget(bouton_moins, 5, 4)
grille_calc.addWidget(bouton1, 6, 1)
grille_calc.addWidget(bouton2, 6, 2)
grille_calc.addWidget(bouton3, 6, 3)
grille_calc.addWidget(bouton_plus, 6, 4)
grille_calc.addWidget(bouton_rep, 7, 1)
grille_calc.addWidget(bouton0, 7, 2)
grille_calc.addWidget(bouton_point, 7, 3)
grille_calc.addWidget(bouton_entrer, 7, 4)

calc_layout.addRow(grille_calc)


# affectation des boutons à leurs actions
def bouton0_clique():
    global TEXT
    TEXT += "0"
    input1.setText(TEXT)


def bouton1_clique():
    global TEXT
    TEXT += "1"
    input1.setText(TEXT)


def bouton2_clique():
    global TEXT
    TEXT += "2"
    input1.setText(TEXT)


def bouton3_clique():
    global TEXT
    TEXT += "3"
    input1.setText(TEXT)


def bouton4_clique():
    global TEXT
    TEXT += "4"
    input1.setText(TEXT)


def bouton5_clique():
    global TEXT
    TEXT += "5"
    input1.setText(TEXT)


def bouton6_clique():
    global TEXT
    TEXT += "6"
    input1.setText(TEXT)


def bouton7_clique():
    global TEXT
    TEXT += "7"
    input1.setText(TEXT)


def bouton8_clique():
    global TEXT
    TEXT += "8"
    input1.setText(TEXT)


def bouton9_clique():
    global TEXT
    TEXT += "9"
    input1.setText(TEXT)


def bouton_point_clique():
    global TEXT
    TEXT += "."
    input1.setText(TEXT)


def bouton_entrer_clique():
    global TEXT, REP
    try:
        text = input1.text().replace("x", "*").replace("^", "**")
        res = eval(text)
        input1.setText(str(res))
        REP = str(res)
        TEXT = ""
    except:
        return


def bouton_plus_clique():
    global TEXT
    TEXT += "+"
    input1.setText(TEXT)


def bouton_moins_clique():
    global TEXT
    TEXT += "-"
    input1.setText(TEXT)


def bouton_fois_clique():
    global TEXT
    TEXT += "x"
    input1.setText(TEXT)


def bouton_diviser_clique():
    global TEXT
    TEXT += "/"
    input1.setText(TEXT)


def bouton_p1_clique():
    global TEXT
    TEXT += "("
    input1.setText(TEXT)


def bouton_p2_clique():
    global TEXT
    TEXT += ")"
    input1.setText(TEXT)


def bouton_del_clique():
    global TEXT
    TEXT = input1.text()[:-1]
    input1.setText(TEXT)


def bouton_sin_clique():
    global TEXT
    TEXT += "sin("
    input1.setText(TEXT)


def bouton_cos_clique():
    global TEXT
    TEXT += "cos("
    input1.setText(TEXT)


def bouton_tan_clique():
    global TEXT
    TEXT += "tan("
    input1.setText(TEXT)


def bouton_ln_clique():
    global TEXT
    TEXT += "log("
    input1.setText(TEXT)


def bouton_exp_clique():
    global TEXT
    TEXT += "exp("
    input1.setText(TEXT)


def bouton_sqrt_clique():
    global TEXT
    TEXT += "sqrt("
    input1.setText(TEXT)


def bouton_pow_clique():
    global TEXT
    TEXT += "^("
    input1.setText(TEXT)


def bouton_rep_clique():
    global TEXT, REP
    TEXT += REP
    input1.setText(TEXT)


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
bouton_point.clicked.connect(bouton_point_clique)
bouton_entrer.clicked.connect(bouton_entrer_clique)
bouton_plus.clicked.connect(bouton_plus_clique)
bouton_moins.clicked.connect(bouton_moins_clique)
bouton_fois.clicked.connect(bouton_fois_clique)
bouton_diviser.clicked.connect(bouton_diviser_clique)
bouton_p1.clicked.connect(bouton_p1_clique)
bouton_p2.clicked.connect(bouton_p2_clique)
bouton_del.clicked.connect(bouton_del_clique)
bouton_sin.clicked.connect(bouton_sin_clique)
bouton_cos.clicked.connect(bouton_cos_clique)
bouton_tan.clicked.connect(bouton_tan_clique)
bouton_ln.clicked.connect(bouton_ln_clique)
bouton_sqrt.clicked.connect(bouton_sqrt_clique)
bouton_exp.clicked.connect(bouton_exp_clique)
bouton_pow.clicked.connect(bouton_pow_clique)
bouton_rep.clicked.connect(bouton_rep_clique)

# couleur de la fenêtre
palette = window.palette()
palette.setColor(QPalette.Background, QColor("grey"))
window.setPalette(palette)
window.setFont(QFont("Normal", 12, QFont.Bold))

# ajout de du layout de la calculatrice dans la fenêtre
window.setLayout(calc_layout)

# ouverture de la fenêtre
window.show()
sys.exit(app.exec())
