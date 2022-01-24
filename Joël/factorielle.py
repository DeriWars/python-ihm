

def factorielle(n):
    res = 1
    for i in range(1, n+1):
        res = res * i
    return res


def main():
    n = int(input("Entrez un nombre : "))
    print(factorielle(n))


if __name__ == main():
    main()
