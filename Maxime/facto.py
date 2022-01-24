from math import factorial

def facto():
    a = int(input("Saisir nombre : "))
    b = 1
    while a != 1:
        b *= a
        a -= 1
    return b

def fact(n):
    return factorial(n)

print(fact(1))

