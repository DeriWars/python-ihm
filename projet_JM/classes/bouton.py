from projet_JM.all_imports import *


def ombre(widget, color=None, radius=10):
    shadow = QGraphicsDropShadowEffect()

    # réglage du flou
    shadow.setBlurRadius(radius)
    if color is not None:
        shadow.setColor(QColor(color))

    # ajout de l'ombre au widget
    widget.setGraphicsEffect(shadow)


def bouton_clique(bouton):
    bouton.setEnabled(False)


class Bouton(QPushButton):
    def __init__(self, label):
        super().__init__(label)
        self.clicked.connect(lambda: bouton_clique(self))
        ombre(self)

    """
    def add_widget(self, widget, pos_x, pos_y):
        widget.addWidget(self.bouton, pos_x, pos_y)
    """

