from square import Square

def get_squares():
    return [
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


def turn(player, dice, squares):
    is_doubles = True
    while is_doubles:
        tiles_moved, is_doubles = dice.roll()
        move(tiles_moved, player, squares)


def move(tiles_moved, player, squares):
    teleport(tiles_moved + player.position, player, squares)


def teleport(square_num, player, squares):
    player.position = square_num
    square = squares[player.position]
    square.visits += 1

    if issubclass(type(square), Invokable):
        square.invoke(player, squares)


def play():
    squares = get_squares()

    players = [Player('player1'), Player('player2')]
    dice = Dice()

    for i in range(100):
        for player in players:
            turn(player, dice, squares)

    squares.sort(reverse=True)
    for square in squares:
        print(f"{square.name} had {square.visits} visits")


if __name__ == '__main__':
    play()