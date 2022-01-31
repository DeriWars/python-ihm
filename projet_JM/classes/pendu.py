from pictures import *
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from random import *

TRANSTABLE = str.maketrans('áàâãäçèéêëìíîïñòóôõöšùúûüýÿž', 'aaaaaceeeeiiiinooooosuuuuyyz')


def read_file(filename):
    words_list = []
    with open(filename, "r", encoding="utf8") as file:
        words = file.read().split()

    for word in words:
        for i in word:
            if i != "-":
                words_list.append(word.lower().translate(TRANSTABLE).replace(' ', ''))
    return words_list


def affichage(taille: int, mot):
    # return [" _ " for i in range(taille)]
    # return "_ " * taille
    plateau = "_ " * len(mot)
    if "-" in mot:
        s = list(mot).index("-")
        plateau = " ".join(["_" for i in range(s)]) + " - " + " ".join(["_" for i in range(s+1, len(mot))])
    return plateau


def random_word(data):
    word = data[randint(0, len(data) - 1)]
    if 4 > len(word) > 15:
        random_word(data)
    return word


"""class Pendu:
    def __init__(self, word, errors=0):
        self.errors = errors
        self.word = word

    def game(self, plateau, boutons_liste):
        for bouton in boutons_liste:
            if bouton.isChecked() and bouton.text() in self.word:
                for index, lettre in enumerate(self.word):
                    if lettre == bouton.text():
                        plateau[index] = bouton.text()
            elif bouton.isChecked() and bouton.text() not in self.word:
                self.errors += 1
        return plateau, self.errors"""


#print(read_file("../data/mots.txt"))