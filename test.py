from main import *
from card import *
from player import *
from square import *


def test_nearest():
    p = Player('player1', 18)
    rr = Nearest([5, 10, 15, 20])
    n = rr.find_nearest(p)
    print(n)


if __name__ == '__main__':
    test_nearest()
