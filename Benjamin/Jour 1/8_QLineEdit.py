import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

app = QApplication(sys.argv)

window = QWidget()

input1 = QLineEdit()

questionnaire = QFormLayout()
questionnaire.addRow(input1)

# Plus de contrôle

input2 = QLineEdit()
input2.setValidator(QIntValidator())
input2.setMaxLength(2)

questionnaire.addRow(input2)

# encore plus de contrôle

input3 = QLineEdit()
input3.setValidator(QDoubleValidator(-5, 12, 5))
#ca fonctionne mal le QDoubleValidator
#piège1 : accepte la notation scientifique

input3.setValidator(QDoubleValidator(-5,12,5,notation=QDoubleValidator.StandardNotation))

questionnaire.addRow(input3)

#exercice : creer un meilleur filtre

#remplacer virgule par un point
input4 = QLineEdit()

validator = QDoubleValidator(0.1,10,2)

localite = QLocale(QLocale.English, QLocale.UnitedStates)

validator.setLocale(localite)
validator.setNotation(QDoubleValidator.StandardNotation)

input4.setValidator(validator)
questionnaire.addRow(input4)

input4.textChanged.connect(print)

input5 = QLineEdit()
input5.setEchoMode(QLineEdit.Password)

questionnaire.addRow(input5)

input6 = QLineEdit()
input6.setText("Tu peux pas m'effacer !")
input6.setReadOnly(True)
#pour print dans la console
print(input6.text())
questionnaire.addRow(input6)

#changer le font et la taille
input7 = QLineEdit()
input7.setText("Tu peux pas m'effacer ! ")
input7.setReadOnly(True)
input7.setFont(QFont("Times", 24, QFont.Bold, True)) #font, size, weight, italic mais seul font est obligatoire
input7.setMinimumSize(500, 50)

palette = input7.palette()
palette.setColor(QPalette.Base, QColor(255, 0, 0))
palette.setColor(QPalette.Text, QColor(0, 255, 0))
palette.setColor(QPalette.Highlight, QColor(0, 0, 255))
input7.setPalette(palette)

questionnaire.addRow(input7)
window.setLayout(questionnaire)

window.show()
sys.exit(app.exec())

