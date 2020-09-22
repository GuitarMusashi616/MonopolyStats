from player import *
from square import *
from main import *
from random import shuffle

class Card:
    def __init__(self):
        pass


class AdvanceTo(Card):
    def __init__(self, square_num):
        self.square_num = square_num

    def execute(self, player, squares):
        teleport(self.square_num, player, squares)


class Deck:
    def __init__(self, cards):
        self.cards = cards
        self.flipped = []

    def shuffle(self):
        shuffle(self.cards)

    def pop(self):
        if not self.cards:
            self.reset()

        card = self.cards.pop(0)
        self.flipped.append(card)
        return card

    def reset(self):
        for _ in range(len(self.flipped)):
            card = self.flipped.pop(0)
            self.cards.append(card)
        self.shuffle()


class ChanceDeck(Deck):
    def __init__(self):
        cards = [
        AdvanceTo(0),
        AdvanceTo(24),
        AdvanceTo(11),
        NearestUtility(),
        NearestRailroad(),
        GetCash(50),
        JailFreeCard(),
        GoBack(3),
        GoToJail(),
        Repairs(25),
        LoseCash(15),
        AdvanceTo(5),
        AdvanceTo(39),
        PayCash(50),
        GetCash(150),
        ]
        super().__init__(cards)
        self.shuffle()







class CommunityDeck(Deck):
    pass
