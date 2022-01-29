import string
from projet_JM.all_imports import *
from pendu import *

WORDFILE = "../data/mots.txt"
errors = 0
boutons_liste = []
liste_images = ["pendu_0.png", "pendu_1.png", "pendu_2.png", "pendu_3.png",
                "pendu_4.png", "pendu_5.png", "pendu_6.png", "pendu_7.png", "pendu_8.png",
                "pendu_9.png", "pendu_10.png", "pendu_11.png", "pendu_12.png"]


"""class UserInterface:
    def __init__(self, label_word):
        self.label_word = label_word
        pass

    def layout(self):
        app = QApplication(sys.argv)
        window = QWidget()
        window.resize(1200, 700)
        window.setWindowTitle("Le jeu du Pendu")

        pendu_layout = QFormLayout()
        label_space = QLabel()
        # label_word = QLabel(" _ _ _ _ a _ _ _ _ a _ _ _ _ _ ")
        top_grid_layout = QGridLayout()
        bottom_grid_layout = QGridLayout()

        self.label_word.setFont(QFont("Times", 50, QFont.Bold))
        self.label_word.setAlignment(Qt.AlignCenter)

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

        for i in string.ascii_lowercase:
            boutons_liste.append(Bouton(i))

        for i in range(24):
            bottom_grid_layout.addWidget(boutons_liste[i], i // 3, i % 3)

        bouton_liste = [bouton_a, bouton_b, bouton_c, bouton_d, bouton_e, bouton_f, bouton_g, bouton_h,
                        bouton_i, bouton_j, bouton_k, bouton_l, bouton_m, bouton_n, bouton_o, bouton_p,
                        bouton_q, bouton_r, bouton_s, bouton_t, bouton_u, bouton_v, bouton_w, bouton_x,
                        bouton_y, bouton_z]
        
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
        

        picture = Pictures(liste_images, self.errors)
        picture.affichage(top_grid_layout)
        top_grid_layout.addWidget(self.label_word, 1, 2)

        pendu_layout.addRow(top_grid_layout)
        pendu_layout.addRow(label_space)
        pendu_layout.addRow(bottom_grid_layout)
        window.setLayout(pendu_layout)

        window.show()
        sys.exit(app.exec())"""


class UserInterface:
    def __init__(self, word, plateau):
        self.word = word
        self.plateau = plateau

    def layout(self):
        # words_list = read_file(WORDFILE)
        # word = random_word(words_list)
        # errors = 0
        # pendu = Pendu(word, errors)
        # plateau = "".join(affichage(len(word)))

        app = QApplication(sys.argv)
        window = QWidget()
        window.resize(1200, 600)
        window.setWindowTitle("Le jeu du Pendu")

        pendu_layout = QFormLayout()
        label_space = QLabel()
        label_word = QLabel()
        label_word.setText(self.plateau)
        top_grid_layout = QGridLayout()
        bottom_grid_layout = QGridLayout()

        label_word.setFont(QFont("Times", 50, QFont.Bold))
        label_word.setAlignment(Qt.AlignCenter)

        for i in string.ascii_lowercase:
            boutons_liste.append(Bouton(i))

        bottom_grid_layout.addWidget(boutons_liste[0], 1, 1)
        bottom_grid_layout.addWidget(boutons_liste[25], 1, 2)
        bottom_grid_layout.addWidget(boutons_liste[4], 1, 3)
        bottom_grid_layout.addWidget(boutons_liste[17], 1, 4)
        bottom_grid_layout.addWidget(boutons_liste[19], 1, 5)
        bottom_grid_layout.addWidget(boutons_liste[24], 1, 6)
        bottom_grid_layout.addWidget(boutons_liste[20], 1, 7)
        bottom_grid_layout.addWidget(boutons_liste[8], 1, 8)
        bottom_grid_layout.addWidget(boutons_liste[14], 1, 9)
        bottom_grid_layout.addWidget(boutons_liste[15], 1, 10)

        bottom_grid_layout.addWidget(boutons_liste[16], 2, 1)
        bottom_grid_layout.addWidget(boutons_liste[18], 2, 2)
        bottom_grid_layout.addWidget(boutons_liste[3], 2, 3)
        bottom_grid_layout.addWidget(boutons_liste[5], 2, 4)
        bottom_grid_layout.addWidget(boutons_liste[6], 2, 5)
        bottom_grid_layout.addWidget(boutons_liste[7], 2, 6)
        bottom_grid_layout.addWidget(boutons_liste[9], 2, 7)
        bottom_grid_layout.addWidget(boutons_liste[10], 2, 8)
        bottom_grid_layout.addWidget(boutons_liste[11], 2, 9)
        bottom_grid_layout.addWidget(boutons_liste[12], 2, 10)

        bottom_grid_layout.addWidget(boutons_liste[22], 3, 3)
        bottom_grid_layout.addWidget(boutons_liste[23], 3, 4)
        bottom_grid_layout.addWidget(boutons_liste[2], 3, 5)
        bottom_grid_layout.addWidget(boutons_liste[21], 3, 6)
        bottom_grid_layout.addWidget(boutons_liste[1], 3, 7)
        bottom_grid_layout.addWidget(boutons_liste[13], 3, 8)

        picture = Pictures(liste_images, errors)
        picture.affichage(top_grid_layout)
        top_grid_layout.addWidget(label_word, 1, 2)

        pendu_layout.addRow(top_grid_layout)
        pendu_layout.addRow(label_space)
        pendu_layout.addRow(bottom_grid_layout)
        window.setLayout(pendu_layout)

        # plateau = pendu.game(plateau, word, boutons_liste)
        # label_word.setText(plateau)
        if errors == len(liste_images):
            label_word.setFont(QFont("Times", 40))
            label_word.setText("\n---- GAME OVER ---- \n"
                               f"Le bon mot était : {self.word}")

        window.show()
        sys.exit(app.exec())


def main():
    words_list = read_file(WORDFILE)
    word = random_word(words_list)
    plateau = "".join(affichage(len(word)))
    ihm = UserInterface(word, plateau)
    ihm.layout()

"""    words_list = read_file(WORDFILE)
    word = random_word(words_list)
    # errors = 0
    # pendu = Pendu(word, errors)
    plateau = "".join(affichage(len(word)))

    app = QApplication(sys.argv)
    window = QWidget()
    window.resize(1200, 600)
    window.setWindowTitle("Le jeu du Pendu")

    pendu_layout = QFormLayout()
    label_space = QLabel()
    label_word = QLabel()
    label_word.setText(plateau)
    top_grid_layout = QGridLayout()
    bottom_grid_layout = QGridLayout()

    label_word.setFont(QFont("Times", 50, QFont.Bold))
    label_word.setAlignment(Qt.AlignCenter)

    for i in string.ascii_lowercase:
        boutons_liste.append(Bouton(i))

    bottom_grid_layout.addWidget(boutons_liste[0], 1, 1)
    bottom_grid_layout.addWidget(boutons_liste[25], 1, 2)
    bottom_grid_layout.addWidget(boutons_liste[4], 1, 3)
    bottom_grid_layout.addWidget(boutons_liste[17], 1, 4)
    bottom_grid_layout.addWidget(boutons_liste[19], 1, 5)
    bottom_grid_layout.addWidget(boutons_liste[24], 1, 6)
    bottom_grid_layout.addWidget(boutons_liste[20], 1, 7)
    bottom_grid_layout.addWidget(boutons_liste[8], 1, 8)
    bottom_grid_layout.addWidget(boutons_liste[14], 1, 9)
    bottom_grid_layout.addWidget(boutons_liste[15], 1, 10)

    bottom_grid_layout.addWidget(boutons_liste[16], 2, 1)
    bottom_grid_layout.addWidget(boutons_liste[18], 2, 2)
    bottom_grid_layout.addWidget(boutons_liste[3], 2, 3)
    bottom_grid_layout.addWidget(boutons_liste[5], 2, 4)
    bottom_grid_layout.addWidget(boutons_liste[6], 2, 5)
    bottom_grid_layout.addWidget(boutons_liste[7], 2, 6)
    bottom_grid_layout.addWidget(boutons_liste[9], 2, 7)
    bottom_grid_layout.addWidget(boutons_liste[10], 2, 8)
    bottom_grid_layout.addWidget(boutons_liste[11], 2, 9)
    bottom_grid_layout.addWidget(boutons_liste[12], 2, 10)

    bottom_grid_layout.addWidget(boutons_liste[22], 3, 3)
    bottom_grid_layout.addWidget(boutons_liste[23], 3, 4)
    bottom_grid_layout.addWidget(boutons_liste[2], 3, 5)
    bottom_grid_layout.addWidget(boutons_liste[21], 3, 6)
    bottom_grid_layout.addWidget(boutons_liste[1], 3, 7)
    bottom_grid_layout.addWidget(boutons_liste[13], 3, 8)

    picture = Pictures(liste_images, errors)
    picture.affichage(top_grid_layout)
    top_grid_layout.addWidget(label_word, 1, 2)

    pendu_layout.addRow(top_grid_layout)
    pendu_layout.addRow(label_space)
    pendu_layout.addRow(bottom_grid_layout)
    window.setLayout(pendu_layout)

    # plateau = pendu.game(plateau, word, boutons_liste)
    # label_word.setText(plateau)
    if errors == len(liste_images):
        label_word.setFont(QFont("Times", 40))
        label_word.setText("\n---- GAME OVER ---- \n"
                           f"Le bon mot était : {word}")

    window.show()
    sys.exit(app.exec())"""


if __name__ == main():
    main()
