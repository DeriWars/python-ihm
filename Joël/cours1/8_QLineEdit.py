import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

app = QApplication(sys.argv)

window = QWidget()

# 1/ La base
input1 = QLineEdit()

questionnaire = QFormLayout()
questionnaire.addRow(input1)

# 2/ plus de controle
input2 = QLineEdit()
input2.setValidator(QIntValidator())
input2.setMaxLength(2)

questionnaire.addRow(input2)

# encore plus de controle
input3 = QLineEdit()
input3.setValidator((QDoubleValidator(-5, 12, 5)))

# fonctionne très bizarement
# piège 1 : accepte la notation scientique

input3.setValidator((QDoubleValidator(-5, 12, 5, notation=QDoubleValidator.StandardNotation)))

questionnaire.addRow(input3)

# exercice : crée un meilleur filtre

# comment remplacer la virgule par un point
# la virgule marche toujours
input4 = QLineEdit()
validator = QDoubleValidator(0.1, 10, 2)

localite = QLocale(QLocale.English, QLocale.UnitedStates)

validator.setLocale(localite)
validator.setNotation(QDoubleValidator.StandardNotation)

input4.setValidator(validator)
questionnaire.addRow(input4)

input4.textChanged.connect(print)  # option permettant d'afficher dans la console le texte tapé

### PASSWORD ####

input5 = QLineEdit()
input5.setEchoMode(QLineEdit.Password)

questionnaire.addRow(input5)

### Readonly ####

input6 = QLineEdit()
input6.setText("Tu peux pas m'effacer !")
input6.setReadOnly(True)

## astuce : lire le texte dans la console
print(input6.text())
questionnaire.addRow(input6)

### Changer les fonts et la taille ####

input7 = QLineEdit()
input7.setText("Tu peux pas m'effacer !")
input7.setReadOnly(True)

input7.setFont(QFont("Times", 24, QFont.Bold, True))  # font, size, weight, italic
# seul font est obligatoire
input7.setMinimumSize(500, 50)
input7.setAlignment(Qt.AlignCenter)

questionnaire.addRow(input7)

# remarque, il est possible d'utiliser la syntaxe du CSS pour le style des widgets

input7.setStyleSheet("""QLineEdit { background-color:grey; color: white }""")

# exercice 2 : changer la couleur du texte et du fond sans utiliser le CSS

window.setLayout(questionnaire)

window.show()
sys.exit(app.exec())
