from bouton import *
from pictures import *
from projet_JM.all_imports import *
from random import *

TRANSTABLE = str.maketrans('áàâãäçèéêëìíîïñòóôõöšùúûüýÿž', 'aaaaaceeeeiiiinooooosuuuuyyz')


def read_file(filename):
    words_list = []
    with open(filename, "r", encoding="utf8") as file:
        words = file.read().split()

    for word in words:
        words_list.append(word.lower().translate(TRANSTABLE).replace(' ', ''))
    return words_list


def affichage(taille: int):
    return [" _ " for i in range(taille)]
    # return " _ " * taille


def random_word(data):
    word = data[randint(0, len(data) - 1)]
    if 4 > len(word) > 15:
        random_word(data)
    return word


"""class Pendu:
    def __init__(self, word, errors=0):
        self.errors = errors
        self.word = word

    def game(self, plateau, word_to_guess, boutons_liste):
        for bouton in boutons_liste:
            if bouton.isChecked() and bouton.text() in word_to_guess:
                for index, lettre in enumerate(word_to_guess):
                    if lettre == bouton.text():
                        plateau[index] = bouton.text()
            elif bouton.isChecked() and bouton.text() not in word_to_guess:
                self.errors += 1
        return plateau
"""