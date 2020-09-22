from random import randint


class Player:
    def __init__(self, name, position=0):
        self.name = name
        self._position = position
        self._cash = 1500

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, value):
        self._position = value % 40

    @property
    def cash(self):
        return self._cash

    @cash.setter
    def cash(self, value):
        self._cash = value


class Dice:
    @classmethod
    def roll(cls):
        die1 = randint(1, 6)
        die2 = randint(1, 6)
        is_doubles = die1 == die2
        return die1+die2, is_doubles
