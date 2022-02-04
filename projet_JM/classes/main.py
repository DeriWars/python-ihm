from UserInterface import *
from login import *
from start import *

WORDFILE = "../data/mots.txt"


def main():
    app = QApplication(sys.argv)
    starter = Start()
    starter.start_layout()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
