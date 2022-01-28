import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Bouton(QPushButton):
    def __init__(self, label):
        super().__init__(label)
        self.clicked.connect(lambda: self.bouton_clique(self))

    def bouton_clique(self, bouton):
        bouton.setEnabled(False)

    """
    def add_widget(self, widget, pos_x, pos_y):
        widget.addWidget(self.bouton, pos_x, pos_y)
    """

