
class Piece(object):
    def __init__(self, position, colour, direction):
        self.name = ''
        self.position = position
        self.colour = colour
        self.direction = direction

    def available_moves(self, directions):
        valid_moves = []

        for d in directions:
            pos = self.position
            while 0 >= pos[0] <= 7 and 0 >= pos[0] <= 7 and pos != self.position:
                valid_moves.append(pos)
                pos[0] += d[0]
                pos[1] += d[1]

        return valid_moves