import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

operateurs = {type(0):{'+':int.__add__,'-':int.__sub__,'x':int.__mul__},
                   type(0.0):{'+':float.__add__,'-':float.__sub__,'x':float.__mul__,'/':float.__truediv__}}


def reset(resultat):
    resultat.setText('')
    resultat.precedent_op = ''
    resultat.pile = 0

def valeur(b):
    print(b.text())

def affiche(b,resultat):
    if resultat.precedent_op == '=':
        reset(resultat)
    valeur = b.text()
    cur_res = resultat.text()
    resultat.setText(cur_res + valeur)

def stock_op(b,resultat):
    nouveau_operateur = b.text()
    operateur = resultat.precedent_op
    if resultat.text() == '':
        return None
    nouveau_nombre = eval(resultat.text())
    valeur_prec = resultat.pile
    if operateur != '' and operateur != '=':
        if type(nouveau_nombre) == float or type(resultat.pile) == float or operateur == '/':
            resultat.pile = operateurs[type(0.0)][operateur](float(valeur_prec),float(nouveau_nombre))
        else:
            resultat.pile = operateurs[type(0)][operateur](valeur_prec, nouveau_nombre)
    else:
        resultat.pile = nouveau_nombre
        resultat.precedent_op = nouveau_operateur
    resultat.setText('')


def egal(resultat):
    nouveau_nombre = eval(resultat.text())
    valeur_prec = resultat.pile
    operateur = resultat.precedent_op
    if operateur != '':
        if type(nouveau_nombre) == float or type(resultat.pile) == float or operateur == '/':
            resultat.pile = operateurs[type(0.0)][operateur](float(valeur_prec),float(nouveau_nombre))
        else:
            resultat.pile = operateurs[type(0)][operateur](valeur_prec, nouveau_nombre)
    resultat.setText(str(resultat.pile))
    resultat.precedent_op = '='


def ombre(widget, color=None, radius=10):
    shadow = QGraphicsDropShadowEffect()

    # réglage du flou
    shadow.setBlurRadius(radius)
    if color is not None:
        shadow.setColor(QColor(color))

    # ajout de l'ombre au widget
    widget.setGraphicsEffect(shadow)


app = QApplication(sys.argv)


class Resultat(QLineEdit):
    def __init__(self):
        super().__init__()
        self.pile = 0
        self.precedent_op = ''
        self.setReadOnly(True)
        self.setStyleSheet("""
            border-style: solid;
            border-width: 1px;
            border-radius:6px
        """)
        self.setFont(QFont("American Typewriter"))
        ombre(self)

class Mon_bouton(QPushButton):
    def __init__(self,label,resultat):
        super().__init__(label)
        self.clicked.connect(lambda:valeur(self))
        self.clicked.connect(lambda:affiche(self,resultat))
        ombre(self)

class Mon_bouton_op(QPushButton):
    def __init__(self,label,resultat):
        super().__init__(label)
        self.clicked.connect(lambda:valeur(self))
        self.clicked.connect(lambda:stock_op(self,resultat))
        ombre(self,radius=30)


class Window(QWidget):
    def __init__(self):
        super().__init__()
        pal = QPalette()
        pal.setColor(self.backgroundRole(),QColor(200,200,100))
        self.setPalette(pal)
        self.setAutoFillBackground(True)

        self.setWindowFlags(Qt.FramelessWindowHint)
        self.resultat = Resultat()

        vbox = QVBoxLayout()
        grid = QGridLayout()

        # bord arrondis avec un mask
        rayon = 100
        chemin = QPainterPath()
        self.resize(250,320)
        chemin.addRoundedRect(QRectF(self.rect()),rayon,rayon)
        masque = QRegion(chemin.toFillPolygon().toPolygon())
        self.setMask(masque)
        self.move(QCursor.pos())




        boutons = []

        for i in range (1,10):
            boutons.append(Mon_bouton(str(i),self.resultat))

        for i in range(9):
            grid.addWidget(boutons[i],2 - i//3, i%3)

        boutons_op = []

        for operateur in operateurs[type(0.0)].keys():
            boutons_op.append(Mon_bouton_op(operateur,self.resultat))


        for i, bouton_op in enumerate(boutons_op):
            grid.addWidget(bouton_op,i,3)

        bouton_egal = QPushButton("=")
        bouton_egal.clicked.connect(lambda:egal(self.resultat))

        bouton_point = Mon_bouton(".",self.resultat)


        grid.addWidget(Mon_bouton(str(0),self.resultat), 3, 0)
        grid.addWidget(bouton_egal, 3, 1)
        grid.addWidget(bouton_point, 3, 2)

        hbox_c  = QHBoxLayout()


        bouton_reset = QPushButton("CE")
        bouton_reset.clicked.connect(lambda:reset(self.resultat))

        hbox_c.addWidget(bouton_reset,2)



        vbox.addWidget(self.resultat)
        vbox.addLayout(hbox_c)
        vbox.addLayout(grid)

        self.setLayout(vbox)

    def mousePressEvent(self, event):
        self.m_lastPos = event.globalPos()
        print(self.m_lastPos)

    def mouseMoveEvent(self, event):
        self.move(self.x() + (event.globalX() - self.m_lastPos.x()),
                  self.y() + (event.globalY() - self.m_lastPos.y()))
        self.m_lastPos = event.globalPos()

    def mouseReleaseEven(self, event):
        self.m_lastPos = event.globalPos()

    def mouseDoubleClickEvent(self, event):
        app.quit()


window = Window()

window.show()


sys.exit(app.exec())
