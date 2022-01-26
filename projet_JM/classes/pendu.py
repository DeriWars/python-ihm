from projet_JM.classes.bouton import *
from projet_JM.classes.pictures import *


class Pendu:

    def __init__(self, errors=0):
        self.errors = errors


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

        """
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
        bouton_maj = Bouton("Maj")

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
        """
        #bouton_maj.add_widget(bottom_grid_layout, 3, 9)
        #bouton_maj.connect_bouton()

        bouton_a = Bouton('a')
        bouton_b = Bouton('b')
        bouton_c = Bouton('c')
        bouton_d = Bouton('d')
        bouton_e = Bouton('e')
        bouton_f = Bouton('f')
        bouton_g = Bouton('g')
        bouton_h = Bouton('h')
        bouton_j = Bouton('i')
        bouton_j = Bouton('j')
        bouton_k = Bouton('k')
        bouton_l = Bouton('l')
        bouton_m = Bouton('m')
        bouton_n = Bouton('n')
        bouton_o = Bouton('o')
        bouton_p = Bouton('p')
        bouton_q = Bouton('q')
        bouton_r = Bouton('r')
        bouton_s = Bouton('s')
        bouton_t = Bouton('t')
        bouton_u = Bouton('u')
        bouton_v = Bouton('v')
        bouton_w = Bouton('w')
        bouton_x = Bouton('x')
        bouton_y = Bouton('y')
        bouton_z = Bouton('z')

        """
        pixmap = QPixmap("../images/img.png")
        labelImage = QLabel()
        labelImage.setPixmap(pixmap)
        top_grid_layout.addWidget(labelImage, 1, 1)
        """
        liste_images = ["pendu_0.png", "pendu_1.png", "pendu_3.png",
                        "pendu_4.png", "pendu_5.png", "pendu_6.png", "pendu_7.png", "pendu_8.png",
                        "pendu_9.png", "pendu_10.png", "pendu_11.png", ]

        picture = Pictures(liste_images, self.errors)
        picture.affichage(top_grid_layout)

        pendu_layout.addRow(top_grid_layout)
        pendu_layout.addRow(bottom_grid_layout)
        window.setLayout(pendu_layout)

        window.show()
        sys.exit(app.exec())


def main():
    errors = 0
    pendu = Pendu(errors)
    pendu.layout()



main()
