from square import *
from player import *


class Property:
    BROWN = 0
    TEAL = 1
    PINK = 2
    ORANGE = 3
    RED = 4
    YELLOW = 5
    GREEN = 6
    BLUE = 7


def get_squares():
    squares = [
        Square('GO'),
        PropertySquare('Mediterranean Avenue', Property.BROWN),
        CommunitySquare(),
        PropertySquare('Baltic Avenue', Property.BROWN),
        Square('Income Tax'),
        RailroadSquare('Reading Railroad'),
        PropertySquare('Oriental Avenue', Property.TEAL),
        ChanceSquare(),
        PropertySquare('Vermont Avenue', Property.TEAL),
        PropertySquare('Connecticut Avenue', Property.TEAL),
        Square('In Jail / Just Visiting'),
        PropertySquare('St. Charles Place', Property.PINK),
        Square('Electric Company'),
        PropertySquare('States Avenue', Property.PINK),
        PropertySquare('Virginia Avenue', Property.PINK),
        RailroadSquare('Pennsylvania Railroad'),
        PropertySquare('St. James Place', Property.ORANGE),
        CommunitySquare(),
        PropertySquare('Tennessee Avenue', Property.ORANGE),
        PropertySquare('New York Avenue', Property.ORANGE),
        Square('Free Parking'),
        PropertySquare('Kentucky Avenue', Property.RED),
        ChanceSquare(),
        PropertySquare('Indiana Avenue', Property.RED),
        PropertySquare('Illinois Avenue', Property.RED),
        RailroadSquare('B. & O. Railroad'),
        PropertySquare('Atlantic Avenue', Property.YELLOW),
        PropertySquare('Ventnor Avenue', Property.YELLOW),
        Square('Water Works'),
        PropertySquare('Marvin Gardens', Property.YELLOW),
        Square('Go to Jail'),
        PropertySquare('Pacific Avenue', Property.GREEN),
        PropertySquare('North Carolina Avenue', Property.GREEN),
        CommunitySquare(),
        PropertySquare('Pennsylvania Avenue', Property.GREEN),
        RailroadSquare('Short Line'),
        ChanceSquare(),
        PropertySquare('Park Place', Property.BLUE),
        Square('Luxury Tax'),
        PropertySquare('Boardwalk', Property.BLUE),
    ]
    return squares


def turn(player, dice, squares):
    is_doubles = True
    while is_doubles:
        tiles_moved, is_doubles = dice.roll()
        player.position += tiles_moved
        square = squares[player.position]
        square.visits += 1
        # print(square.name)

        if square is Invokable:
            square.invoke(player)


def play():
    squares = get_squares()
    players = [Player('player1'), Player('player2')]
    dice = Dice()

    for i in range(10000):
        for player in players:
            turn(player, dice, squares)

    squares.sort(reverse=True)
    for square in squares:
        print(f"{square.name} had {square.visits} visits")


if __name__ == '__main__':
    play()