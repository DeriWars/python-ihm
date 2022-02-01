from UserInterface import *
from login import *

WORDFILE = "../data/mots.txt"


def main():
    words_list = read_file(WORDFILE)
    word = random_word(words_list)
    print(word)
    plate = display(word)
    ihm = UserInterface(word, plate)
    # ihm.layout()
    user = Login("trésor", ihm)
    user.layout()


if __name__ == "__main__":
    main()
