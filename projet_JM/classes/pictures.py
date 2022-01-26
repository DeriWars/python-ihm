from projet_JM.all_imports import *

#["p1", "p2", "p3", "p4"]

class Pictures:

    def __init__(self, liste, index):
        self.liste = liste
        self.index = index

    def affichage(self, widget):
        name = self.liste[self.index]
        pixmap = QPixmap(f"../images/{name}")
        label_image = QLabel()
        label_image.setPixmap(pixmap)
        widget.addWidget(label_image, 1, 2)
