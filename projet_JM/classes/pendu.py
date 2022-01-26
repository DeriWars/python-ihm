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
        label_space = QLabel()
        top_grid_layout = QGridLayout()
        bottom_grid_layout = QGridLayout()

        bouton_a = Bouton('a')
        bouton_b = Bouton('b')
        bouton_c = Bouton('c')
        bouton_d = Bouton('d')
        bouton_e = Bouton('e')
        bouton_f = Bouton('f')
        bouton_g = Bouton('g')
        bouton_h = Bouton('h')
        bouton_i = Bouton('i')
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

        bouton_a.add_widget(bottom_grid_layout, 1, 1)
        bouton_z.add_widget(bottom_grid_layout, 1, 2)
        bouton_e.add_widget(bottom_grid_layout, 1, 3)
        bouton_r.add_widget(bottom_grid_layout, 1, 4)
        bouton_t.add_widget(bottom_grid_layout, 1, 5)
        bouton_y.add_widget(bottom_grid_layout, 1, 6)
        bouton_u.add_widget(bottom_grid_layout, 1, 7)
        bouton_i.add_widget(bottom_grid_layout, 1, 8)
        bouton_o.add_widget(bottom_grid_layout, 1, 9)
        bouton_p.add_widget(bottom_grid_layout, 1, 10)

        bouton_a.connect_bouton()
        bouton_z.connect_bouton()
        bouton_e.connect_bouton()
        bouton_r.connect_bouton()
        bouton_t.connect_bouton()
        bouton_y.connect_bouton()
        bouton_u.connect_bouton()
        bouton_i.connect_bouton()
        bouton_o.connect_bouton()
        bouton_p.connect_bouton()

        bouton_q.add_widget(bottom_grid_layout, 2, 1)
        bouton_s.add_widget(bottom_grid_layout, 2, 2)
        bouton_d.add_widget(bottom_grid_layout, 2, 3)
        bouton_f.add_widget(bottom_grid_layout, 2, 4)
        bouton_g.add_widget(bottom_grid_layout, 2, 5)
        bouton_h.add_widget(bottom_grid_layout, 2, 6)
        bouton_j.add_widget(bottom_grid_layout, 2, 7)
        bouton_k.add_widget(bottom_grid_layout, 2, 8)
        bouton_l.add_widget(bottom_grid_layout, 2, 9)
        bouton_m.add_widget(bottom_grid_layout, 2, 10)

        bouton_q.connect_bouton()
        bouton_s.connect_bouton()
        bouton_d.connect_bouton()
        bouton_f.connect_bouton()
        bouton_g.connect_bouton()
        bouton_h.connect_bouton()
        bouton_j.connect_bouton()
        bouton_k.connect_bouton()
        bouton_l.connect_bouton()
        bouton_m.connect_bouton()

        bouton_w.add_widget(bottom_grid_layout, 3, 3)
        bouton_x.add_widget(bottom_grid_layout, 3, 4)
        bouton_c.add_widget(bottom_grid_layout, 3, 5)
        bouton_v.add_widget(bottom_grid_layout, 3, 6)
        bouton_b.add_widget(bottom_grid_layout, 3, 7)
        bouton_n.add_widget(bottom_grid_layout, 3, 8)

        bouton_w.connect_bouton()
        bouton_x.connect_bouton()
        bouton_c.connect_bouton()
        bouton_v.connect_bouton()
        bouton_b.connect_bouton()
        bouton_n.connect_bouton()

        """
        pixmap = QPixmap("../images/img.png")
        labelImage = QLabel()
        labelImage.setPixmap(pixmap)
        top_grid_layout.addWidget(labelImage, 1, 1)
        """
        liste_images = ["pendu_0.png", "pendu_1.png", "pendu_2.png", "pendu_3.png",
                        "pendu_4.png", "pendu_5.png", "pendu_6.png", "pendu_7.png", "pendu_8.png",
                        "pendu_9.png", "pendu_10.png", "pendu_11.png", ]

        picture = Pictures(liste_images, self.errors)
        picture.affichage(top_grid_layout)

        pendu_layout.addRow(top_grid_layout)
        pendu_layout.addRow(label_space)
        pendu_layout.addRow(bottom_grid_layout)
        window.setLayout(pendu_layout)

        window.show()
        sys.exit(app.exec())


def main():
    errors = 0
    pendu = Pendu(errors)
    pendu.layout()


if __name__ == main():
    main()
