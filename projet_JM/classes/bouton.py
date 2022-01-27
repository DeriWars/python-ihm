import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

BOUTONNAME = ""


class Bouton:
    def __init__(self, bouton_name):
        self.bouton = QPushButton(bouton_name)

    def bouton_clique(self, bouton):
        global BOUTONNAME
        bouton.setEnabled(False)
        BOUTONNAME = bouton.text()

    def connect_bouton(self):
        self.bouton.clicked.connect(lambda: self.bouton_clique(self.bouton))

    def add_widget(self, widget, pos_x, pos_y):
        widget.addWidget(self.bouton, pos_x, pos_y)

    def is_checked(self):
        return self.bouton.isChecked()
