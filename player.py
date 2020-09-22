from random import randint


class Player:
    def __init__(self, name):
        self.name = name
        self._position = 0

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, value):
        self._position = value % 40


class Dice:
    @classmethod
    def roll(self):
        die1 = randint(1, 6)
        die2 = randint(1, 6)
        is_doubles = die1 == die2
        return die1+die2, is_doubles
