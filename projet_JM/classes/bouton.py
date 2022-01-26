import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Bouton:
    def __init__(self, bouton_name):
        self.bouton = QPushButton(bouton_name)

    def bouton_clique(self, bouton):
        bouton.setEnabled(False)
        print(bouton.text(), "est cliqué")

    def connect_bouton(self):
        self.bouton.clicked.connect(lambda: self.bouton_clique(self.bouton))

    def add_widget(self, widget, pos_x, pos_y):
        widget.addWidget(self.bouton, pos_x, pos_y)
