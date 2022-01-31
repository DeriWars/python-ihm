import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Pictures:
    def __init__(self, liste, index):
        self.liste = liste
        self.index = index

    def affichage(self, widget):
        name = self.liste[self.index]
        pixmap = QPixmap(f"../images/{name}")
        label_image = QLabel()
        label_image.setAlignment(Qt.AlignCenter)
        label_image.setPixmap(pixmap)
        widget.addWidget(label_image, 1, 1)

    """def error_state(self, top_grid_layout):
        picture = Pictures(liste_images, errors)
        picture.affichage(top_grid_layout)"""
