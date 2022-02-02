from UserInterface import *
from login import *

WORDFILE = "../data/mots.txt"


def main():
    app = QApplication(sys.argv)

    words_list = read_file(WORDFILE)
    word = random_word(words_list)
    print(word)
    plate = display(word)
    ihm = UserInterface(word, plate)
    # ihm.layout()
    user = Login(ihm)
    user.layout()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
