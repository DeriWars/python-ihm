import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from random import *
from bouton import disable_buttons

TRANSTABLE = str.maketrans('áàâãäçèéêëìíîïñòóôõöšùúûüýÿž', 'aaaaaceeeeiiiinooooosuuuuyyz')


def read_file(filename):
    words_list = []
    with open(filename, "r", encoding="utf8") as file:
        words = file.read().split()
    for word in words:
        words_list.append(word.lower().translate(TRANSTABLE).replace(' ', ''))
    return words_list


def random_word(data):
    word = data[randint(0, len(data) - 1)]
    if 4 > len(word) > 15:
        random_word(data)
    return word


def display(word):
    plate = "_ " * len(word)
    if "-" in word:
        s = list(word).index("-")
        plate = " ".join(["_" for i in range(s)]) + " - " + " ".join(["_" for i in range(s + 1, len(word))])
    return plate


def change_display(plate, word, user_letter):
    for index, letter in enumerate(word):
        if letter == user_letter:
            plate = plate[:index * 2] + letter + plate[index * 2 + 1:]
    return plate


def win_label(label_word, input, buttons_list, word, disable_input):
    label_word.setFont(QFont("Times", 40))
    label_word.setText("\n---- Victoire du joueur ----\n"
                       f"Le bon mot était : {word}")
    disable_buttons(buttons_list)
    disable_input(input)


def lose_label(label_word, input, buttons_list, word, disable_input):
    label_word.setFont(QFont("Times", 40))
    label_word.setText("\n---- GAME OVER ---- \n"
                       f"Le bon mot était : {word}")
    disable_buttons(buttons_list)
    disable_input(input)
