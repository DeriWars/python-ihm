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


def display(word):
    plate = "_ " * len(word)
    if "-" in word:
        s = list(word).index("-")
        plate = " ".join(["_" for i in range(s)]) + " - " + " ".join(["_" for i in range(s + 1, len(word))])
    return plate


def random_word(data):
    word = data[randint(0, len(data) - 1)]
    if 4 > len(word) > 15:
        random_word(data)
    return word


