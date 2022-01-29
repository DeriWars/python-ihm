import string
from projet_JM.all_imports import *
from pendu import *
# from bouton import *

WORDFILE = "../data/mots.txt"
errors = 0
boutons_liste = []
liste_images = ["pendu_0.png", "pendu_1.png", "pendu_2.png", "pendu_3.png",
                "pendu_4.png", "pendu_5.png", "pendu_6.png", "pendu_7.png", "pendu_8.png",
                "pendu_9.png", "pendu_10.png", "pendu_11.png", "pendu_12.png"]


def ombre(widget, color=None, radius=10):
    shadow = QGraphicsDropShadowEffect()

    # réglage du flou
    shadow.setBlurRadius(radius)
    if color is not None:
        shadow.setColor(QColor(color))

    # ajout de l'ombre au widget
    widget.setGraphicsEffect(shadow)


def bouton_clique(bouton, label_word, top_grid_layout):
    bouton.setEnabled(False)
    game(bouton, label_word, top_grid_layout)


def game(bouton, label_word, top_grid_layout):
    global errors, plateau
    """if bouton.text() in word:
        for index, lettre in enumerate(word):
            if lettre == bouton.text():
                plateau = plateau[:index * 2] + lettre + plateau[index * 2 + 1:]
    elif bouton.text() not in word:
        errors += 1
        print(errors)
    label_word.setText(plateau)"""
    # while "_" in plateau:

    if bouton.text() in word:
        for index, lettre in enumerate(word):
            if lettre == bouton.text():
                plateau = plateau[:index * 2] + lettre + plateau[index * 2 + 1:]
    elif bouton.text() not in word:
        errors += 1
        print("les erreurs :", errors)
    label_word.setText(plateau)
    error_state(top_grid_layout)
    # break
    if errors == len(liste_images) - 1:
        print("perdu")
        label_word.setFont(QFont("Times", 40))
        label_word.setText("\n---- GAME OVER ---- \n"
                           f"Le bon mot était : {word}")
        desactive_boutons()
        # break

    if "_" not in plateau:
        label_word.setFont(QFont("Times", 40))
        label_word.setText("\n---- Victoire du joueur français ----\n"
                           f"Le bon mot était : {word}")
        desactive_boutons()
        # break


def error_state(top_grid_layout):
    picture = Pictures(liste_images, errors)
    picture.affichage(top_grid_layout)


def desactive_boutons():
    for bouton in boutons_liste:
        bouton.setEnabled(False)


class Bouton(QPushButton):
    def __init__(self, label, label_word, top_grid_layout):
        super().__init__(label)
        self.label_word = label_word
        self.top_grid_layout = top_grid_layout
        self.clicked.connect(lambda: bouton_clique(self, self.label_word, self.top_grid_layout))
        ombre(self)


class UserInterface:
    def __init__(self, word, plateau):
        self.word = word
        self.plateau = plateau

    def layout(self):
        global errors, label_word
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
            boutons_liste.append(Bouton(i, label_word, top_grid_layout))

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

        # plateau = self.game(self.plateau, boutons_liste)
        # label_word.setText(plateau)

        pendu_layout.addRow(top_grid_layout)
        pendu_layout.addRow(label_space)
        pendu_layout.addRow(bottom_grid_layout)
        window.setLayout(pendu_layout)

        # plateau = self.game(self.plateau, boutons_liste)


        window.show()
        sys.exit(app.exec())


words_list = read_file(WORDFILE)
word = random_word(words_list)
print(word)
plateau = affichage(len(word))
ihm = UserInterface(word, plateau)


def main():
    ihm.layout()


if __name__ == main():
    main()
