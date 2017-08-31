
class Piece(object):
    def __init__(self, position, colour):
        self.name = ""
        self.position = position
        self.colour = colour


    def available_moves(self, direction):
        possible_moves = []

        for d in direction:
            pos = self.position
            i = 0

            while 0 <= pos[0] + d[0]*i <= 7 and 0 <= pos[1] + d[1]*i <= 7:
                possible_moves.append([pos[0] + d[0]*i, pos[1] + d[1]*i])
                i += 1
                
        return possible_moves
