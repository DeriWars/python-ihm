import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Pendu:
    def __init__(self):
        pass

    def bouton_clique(self, bouton):
        bouton.setEnabled(False)
        print(bouton.text(), "est cliqué")


    def layout(self):
        app = QApplication(sys.argv)
        window = QWidget()
        window.resize(1200, 700)
        window.setWindowTitle("Le jeu du pendu")

        pendu_layout = QFormLayout()
        top_grid_layout = QGridLayout()
        bottom_grid_layout = QGridLayout()

        bouton_a = QPushButton("a")
        bouton_b = QPushButton("b")
        bouton_c = QPushButton("c")
        bouton_d = QPushButton("d")
        bouton_e = QPushButton("e")
        bouton_f = QPushButton("f")
        bouton_g = QPushButton("g")
        bouton_h = QPushButton("h")
        bouton_i = QPushButton("i")
        bouton_j = QPushButton("j")
        bouton_k = QPushButton("k")
        bouton_l = QPushButton("l")
        bouton_m = QPushButton("m")
        bouton_n = QPushButton("n")
        bouton_o = QPushButton("o")
        bouton_p = QPushButton("p")
        bouton_q = QPushButton("q")
        bouton_r = QPushButton("r")
        bouton_s = QPushButton("s")
        bouton_t = QPushButton("t")
        bouton_u = QPushButton("u")
        bouton_v = QPushButton("v")
        bouton_w = QPushButton("w")
        bouton_x = QPushButton("x")
        bouton_y = QPushButton("y")
        bouton_z = QPushButton("z")

        bouton_a.clicked.connect(lambda: self.bouton_clique(bouton_a))
        bouton_b.clicked.connect(lambda: self.bouton_clique(bouton_b))
        bouton_c.clicked.connect(lambda: self.bouton_clique(bouton_c))
        bouton_d.clicked.connect(lambda: self.bouton_clique(bouton_d))
        bouton_e.clicked.connect(lambda: self.bouton_clique(bouton_e))
        bouton_f.clicked.connect(lambda: self.bouton_clique(bouton_f))
        bouton_g.clicked.connect(lambda: self.bouton_clique(bouton_g))
        bouton_h.clicked.connect(lambda: self.bouton_clique(bouton_h))
        bouton_i.clicked.connect(lambda: self.bouton_clique(bouton_i))
        bouton_j.clicked.connect(lambda: self.bouton_clique(bouton_j))
        bouton_k.clicked.connect(lambda: self.bouton_clique(bouton_k))
        bouton_l.clicked.connect(lambda: self.bouton_clique(bouton_l))
        bouton_m.clicked.connect(lambda: self.bouton_clique(bouton_m))
        bouton_n.clicked.connect(lambda: self.bouton_clique(bouton_n))
        bouton_o.clicked.connect(lambda: self.bouton_clique(bouton_o))
        bouton_p.clicked.connect(lambda: self.bouton_clique(bouton_p))
        bouton_q.clicked.connect(lambda: self.bouton_clique(bouton_q))
        bouton_r.clicked.connect(lambda: self.bouton_clique(bouton_r))
        bouton_s.clicked.connect(lambda: self.bouton_clique(bouton_s))
        bouton_t.clicked.connect(lambda: self.bouton_clique(bouton_t))
        bouton_u.clicked.connect(lambda: self.bouton_clique(bouton_u))
        bouton_v.clicked.connect(lambda: self.bouton_clique(bouton_v))
        bouton_w.clicked.connect(lambda: self.bouton_clique(bouton_w))
        bouton_x.clicked.connect(lambda: self.bouton_clique(bouton_x))
        bouton_y.clicked.connect(lambda: self.bouton_clique(bouton_y))
        bouton_z.clicked.connect(lambda: self.bouton_clique(bouton_z))


        bottom_grid_layout.addWidget(bouton_a, 1, 1)
        bottom_grid_layout.addWidget(bouton_z, 1, 2)
        bottom_grid_layout.addWidget(bouton_e, 1, 3)
        bottom_grid_layout.addWidget(bouton_r, 1, 4)
        bottom_grid_layout.addWidget(bouton_t, 1, 5)
        bottom_grid_layout.addWidget(bouton_y, 1, 6)
        bottom_grid_layout.addWidget(bouton_u, 1, 7)
        bottom_grid_layout.addWidget(bouton_i, 1, 8)
        bottom_grid_layout.addWidget(bouton_o, 1, 9)
        bottom_grid_layout.addWidget(bouton_p, 1, 10)

        bottom_grid_layout.addWidget(bouton_q, 2, 1)
        bottom_grid_layout.addWidget(bouton_s, 2, 2)
        bottom_grid_layout.addWidget(bouton_d, 2, 3)
        bottom_grid_layout.addWidget(bouton_f, 2, 4)
        bottom_grid_layout.addWidget(bouton_g, 2, 5)
        bottom_grid_layout.addWidget(bouton_h, 2, 6)
        bottom_grid_layout.addWidget(bouton_j, 2, 7)
        bottom_grid_layout.addWidget(bouton_k, 2, 8)
        bottom_grid_layout.addWidget(bouton_l, 2, 9)
        bottom_grid_layout.addWidget(bouton_m, 2, 10)

        bottom_grid_layout.addWidget(bouton_w, 3, 3)
        bottom_grid_layout.addWidget(bouton_x, 3, 4)
        bottom_grid_layout.addWidget(bouton_c, 3, 5)
        bottom_grid_layout.addWidget(bouton_v, 3, 6)
        bottom_grid_layout.addWidget(bouton_b, 3, 7)
        bottom_grid_layout.addWidget(bouton_n, 3, 8)

        pixmap = QPixmap("img.png")
        labelImage = QLabel()
        labelImage.setPixmap(pixmap)
        top_grid_layout.addWidget(labelImage, 1, 1)

        pendu_layout.addRow(top_grid_layout)
        pendu_layout.addRow(bottom_grid_layout)
        window.setLayout(pendu_layout)

        window.show()
        sys.exit(app.exec())


def main():
    pendu = Pendu()
    pendu.layout()


main()
