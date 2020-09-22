from card import ChanceDeck, CommunityDeck

class Property:
    BROWN = 0
    TEAL = 1
    PINK = 2
    ORANGE = 3
    RED = 4
    YELLOW = 5
    GREEN = 6
    BLUE = 7

class Square:
    def __init__(self, name):
        self.name = name
        self.visits = 0

    def __lt__(self, other):
        return self.visits < other.visits


class Buyable:
    def buy(self, player):
        raise NotImplementedError


class Invokable:
    def invoke(self, player):
        raise NotImplementedError


class PropertySquare(Buyable, Square):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

    def buy(self, player):
        return True


class RailroadSquare(Buyable, Square):
    def __init__(self, name):
        super().__init__(name)

    def buy(self, player):
        return True


class CommunitySquare(Invokable, Square):
    def __init__(self):
        name = "Community Chest"
        super().__init__(name)

    def invoke(self, player, squares):
        deck = CommunityDeck()
        card = deck.pop()
        card.execute(player, squares)


class ChanceSquare(Invokable, Square):
    def __init__(self):
        name = "Chance"
        super().__init__(name)

    def invoke(self, player, squares):
        deck = ChanceDeck()
        card = deck.pop()
        card.execute(player, squares)
