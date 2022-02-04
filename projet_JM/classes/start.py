import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Start:
    def __init__(self):
        pass

    def start_layout(self):
        app = QApplication(sys.argv)
        self.window = QTabWidget()
        self.window.setWindowTitle("Démarrage")
        self.window.resize(450, 200)
        self.window.setStyleSheet("background : #D2E1E1")

        ############### TAB POUR JOUER TOUT SEUL ##################

        solo_tab = QWidget()
        solo_layout = QFormLayout()
        solo_label1 = QLabel("Choisir le niveau : ")
        solo_button_start = QPushButton("Jouer tout seul")
        space_label = QLabel("\n")

        level_box = QHBoxLayout()
        level_box.setAlignment(Qt.AlignCenter)
        level1_button = QRadioButton("Niveau 1")
        level1_button.setChecked(True)
        level2_button = QRadioButton("Niveau 2")
        level3_button = QRadioButton("Niveau 3")

        level_box.addWidget(level1_button)
        level_box.addWidget(level2_button)
        level_box.addWidget(level3_button)

        solo_layout.addRow(solo_label1)
        solo_layout.addRow(space_label)
        solo_layout.addRow(level_box)
        solo_layout.addRow(space_label)
        solo_layout.addRow(solo_button_start)

        solo_tab.setLayout(solo_layout)

        ######################### TAB POUR JOUER A DEUX ###################

        duo_tab = QWidget()
        duo_layout = QFormLayout()
        duo_input = QLineEdit()
        duo_input.setEchoMode(QLineEdit.Password)
        duo_label1 = QLabel("Mot à faire deviner : ")
        duo_button_start = QPushButton("Jouer à deux")
        space_label1 = QLabel("\n")

        duo_layout.addRow(space_label1)
        duo_layout.addRow(duo_label1, duo_input)
        duo_layout.addRow(space_label1)
        duo_layout.addRow(duo_button_start)
        duo_tab.setLayout(duo_layout)

        self.window.addTab(solo_tab, "Jouer seul")
        self.window.addTab(duo_tab, "Jouer à deux")
        self.window.show()
        sys.exit(app.exec())


start = Start()
start.start_layout()
