import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


def get_pos(event):
    x = event.pos().x()
    y = event.pos().y()
    print(x, y)


def get_press(event):
    if event.key() == Qt.Key_F5:
        print("toto")


def presse_bouton(event):
    if event.key() == Qt.Key_Space:
        print("Zozo")


def move_left():
    image.move(image.pos() + QPoint(-15, 0))


def move_right():
    image.move(image.pos() + QPoint(15, 0))


app = QApplication(sys.argv)

window = QWidget()

boite = QVBoxLayout()
image = QLabel()
boite.addWidget(image)

image.setPixmap(QPixmap("/Users/vrabiet/Downloads/9782746755734.jpg"))

image.mousePressEvent = get_pos

window.keyPressEvent = get_press

# Attention keyPressEvent ne fonctionne sur un QLabel

bouton = QPushButton()
bouton.setText("Hello")

bouton.keyPressEvent = presse_bouton
boite.addWidget(bouton)

# pour pouvoir utiliser des actions clavier sur des labels
# Qshorcut

QShortcut(QKeySequence(Qt.Key_Left), window, activated=move_left)
QShortcut(QKeySequence(Qt.Key_Right), window, activated=move_right)

window.setLayout(boite)
window.show()

sys.exit(app.exec())
