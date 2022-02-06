import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from string import ascii_lowercase
from random import *
from bouton import disable_buttons

FRENCH = [8.173, 0.901, 3.345, 3.669, 16.734, 1.066, 0.866, 0.737, 7.579, 0.613, 0.049, 5.456, 2.968, 7.095, 5.819,
          2.521, 1.362, 6.693, 7.948, 7.244, 6.429, 1.838, 0.074, 0.427, 0.128, 0.326]

TRANSTABLE = str.maketrans('áàâãäçèéêëìíîïñòóôõöšùúûüýÿž', 'aaaaaceeeeiiiinooooosuuuuyyz')

WORDFILE = "../data/mots.txt"

STRING_ACCENTS = 'áàâãäçèéêëìíîïñòóôõöšùúûüýÿž'
LISTE_ACCENTS = list(STRING_ACCENTS)


def dico(liste):
    d = dict()
    for index, letter in enumerate(ascii_lowercase):
        d[letter] = liste[index]
    return d


def read_file(filename):
    words_to_ban = []
    with open(filename, "r", encoding="utf8") as file:
        words = file.read().split()
    for word in words:
        for char in word:
            if char in LISTE_ACCENTS:
                words_to_ban.append(word.lower().replace(' ', '').replace('-', ''))
    set_words = set(words)
    set_words_to_ban = set(words_to_ban)
    words_set = set_words - set_words_to_ban
    return list(words_set)


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


def win_label(label_word, input, buttons_list, word, disable_input, button_state, score_button):
    label_word.setFont(QFont("Times", 40))
    label_word.setText("\n---- Victoire du joueur ----\n"
                       f"Le bon mot était : {word}")
    disable_buttons(buttons_list)
    disable_input(input)
    button_state(score_button, True)


def lose_label(label_word, input, buttons_list, word, disable_input, button_state, score_button):
    label_word.setFont(QFont("Times", 40))
    label_word.setText("\n---- GAME OVER ---- \n"
                       f"Le bon mot était : {word}")
    disable_buttons(buttons_list)
    disable_input(input)
    button_state(score_button, True)


def difficulty_analysis(filename, difficulty: str):
    dictionnary = dico(FRENCH)
    sort_dictionnary = dict()
    easy_list = []
    medium_list = []
    hard_list = []
    max = 0
    for word in read_file(filename):
        total = 0
        for char in word:
            total += dictionnary.get(char, 0)
        total /= len(word)
        if total > max:
            max = total
        sort_dictionnary[word] = round(total)
        if sort_dictionnary[word] > 8:
            easy_list.append(word)
        elif 8 > sort_dictionnary[word] > 6:
            medium_list.append(word)
        elif 6 > sort_dictionnary[word] > 0:
            hard_list.append(word)

    if difficulty == "Niveau 1":
        return easy_list
    elif difficulty == "Niveau 2":
        return medium_list
    elif difficulty == "Niveau 3":
        return hard_list

