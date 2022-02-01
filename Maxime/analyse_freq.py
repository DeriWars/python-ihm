from string import ascii_lowercase

FRENCH = [8.173, 0.901, 3.345, 3.669, 16.734, 1.066, 0.866, 0.737, 7.579, 0.613, 0.049, 5.456, 2.968, 7.095, 5.819,
          2.521, 1.362, 6.693, 7.948, 7.244, 6.429, 1.838, 0.074, 0.427, 0.128, 0.326]

TRANSTABLE = str.maketrans('áàâãäçèéêëìíîïñòóôõöšùúûüýÿž', 'aaaaaceeeeiiiinooooosuuuuyyz')

WORDFILE = "../projet_JM/data/mots.txt"


def dico(liste):
    d = dict()
    for index, letter in enumerate(ascii_lowercase):
        d[letter] = liste[index]
    return d

def read_file_difficile(filename):
    words_list = []
    with open(filename, "r", encoding="utf8") as file:
        words = file.read().split()
    for word in words:
        words_list.append(word.lower().translate(TRANSTABLE).replace(' ', ''))
    return words_list

def read_file_facile(filename):
    words_list = []
    with open(filename, 'r', encoding="utf8") as file:
        words = file.read().split()
    for word in words:
        for i in word:
            pass


def analyse_frequentielle():
    difficulte = str(input("Saisissez le niveau de difficulté : facile, intermediaire ou difficile"))
    if difficulte == "difficile":
        return read_file_difficile(WORDFILE)


print(dico(FRENCH))
#print(read_file(WORDFILE))
#print(frequential_analys())
