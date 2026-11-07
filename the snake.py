from pycparser.c_ast import While


def is_happy(n):
    while n != 1 :
        n = sum(int(chiffre))**2  for chiffre str(n)


