# https://python-poetry.org/docs/pyproject/

from art import *
from time import sleep


def message(name):
    for _ in range(30):
        print(text2art("Bonne Fete {}".format(name), font="rand", decoration="heart4"))
        sleep(1)


if __name__ == '__main__':
    message('Mich')
