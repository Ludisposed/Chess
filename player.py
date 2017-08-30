
class Player():
    def __init__(self, colour, name):
        self.colour = colour
        self.name = name
        self.castle_long = False
        self.castle_short = False

    def __str__(self):
        return '{} as {}'.format(self.name, self.colour)
