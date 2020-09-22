from main import move, teleport
from random import shuffle


class Card:
    def execute(self, player, squares):
        raise NotImplementedError


class AdvanceTo(Card):
    def __init__(self, square_num):
        self.square_num = square_num

    def execute(self, player, squares):
        teleport(self.square_num, player, squares)


class Nearest(Card):
    def __init__(self, square_num_list):
        assert type(square_num_list) == list
        self.square_num_list = square_num_list

    def execute(self, player, squares):
        nearest_square = self.find_nearest(player)
        assert nearest_square
        teleport(nearest_square, player, squares)

    def find_nearest(self, player):
        closest_distance = 50
        nearest_square = None
        for pos in self.square_num_list:
            assert 0 <= pos <= 39
            assert 0 <= player.position <= 39

            possible_nearest = pos - player.position
            if possible_nearest < 0:
                possible_nearest += 40

            if possible_nearest < closest_distance:
                closest_distance = possible_nearest
                nearest_square = pos

        return nearest_square


class GetCash(Card):
    def __init__(self, amount):
        self.amount = amount

    def execute(self, player, squares):
        player.cash += self.amount


class JailFreeCard(Card):
    def __init__(self):
        pass

    def execute(self, player, squares):
        pass


class GoBack(Card):
    def __init__(self, tiles_back):
        self.tiles_back = tiles_back

    def execute(self, player, squares):
        move(-1 * self.tiles_back, player, squares)


class GoToJail(Card):
    def __init__(self):
        pass

    def execute(self, player, squares):
        pass


class Repairs(Card):
    def __init__(self, tax_per_hotel):
        self.tax_per_hotel = tax_per_hotel

    def execute(self, player, squares):
        pass


class LoseCash(Card):
    def __init__(self, amount):
        self.amount = amount

    def execute(self, player, squares):
        player.cash -= self.amount


class PayEach(Card):
    def __init__(self, amount):
        self.amount = amount

    def execute(self, player, squares):
        pass


class CollectFromEach(Card):
    def __init__(self, amount):
        self.amount = amount

    def execute(self, player, squares):
        pass


class Deck:
    def __init__(self, cards):
        self.cards = cards
        self.flipped = []
        self.shuffle()

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


# Singleton
class ChanceDeck(Deck):
    __instance = None
    cards = [
        AdvanceTo(0),
        AdvanceTo(24),
        AdvanceTo(11),
        Nearest([12, 28]),
        Nearest([5, 10, 15, 20]),
        GetCash(50),
        JailFreeCard(),
        GoBack(3),
        GoToJail(),
        Repairs([25, 100]),
        LoseCash(15),
        AdvanceTo(5),
        AdvanceTo(39),
        PayEach(50),
        GetCash(150),
    ]

    def __new__(cls):
        if not cls.__instance:
            cls.__instance = Deck(cls.cards)
        return cls.__instance


# Singleton
class CommunityDeck(Deck):
    __instance = None
    cards = [
        AdvanceTo(0),
        GetCash(200),
        LoseCash(50),
        GetCash(50),
        JailFreeCard(),
        GoToJail(),
        CollectFromEach(50),  # give each
        GetCash(100),
        GetCash(20),
        CollectFromEach(10),  # give each
        GetCash(100),
        LoseCash(50),
        LoseCash(50),
        GetCash(25),
        Repairs([40, 115]),
        GetCash(10),
        GetCash(100),
    ]

    def __new__(cls):
        if not cls.__instance:
            cls.__instance = Deck(cls.cards)
        return cls.__instance
