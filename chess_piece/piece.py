
class Piece(object):
    def __init__(self, position, colour):
        self.name = ""
        self.position = position
        self.colour = colour


    def available_moves(self, direction):
        possible_moves = []

        for d in direction:
            print 'Direction ', d

            pos = self.position[:]
            print 'Initial Position ', pos

            # Issues overwriting possible_moves, out of bounds
            while 0 <= pos[0] <= 7 and 0 <= pos[1] <= 7:
                possible_moves.append(pos)
                pos[0] += d[0]
                pos[1] += d[1]
                print 'Possible move ', pos

        print possible_moves
        return possible_moves
