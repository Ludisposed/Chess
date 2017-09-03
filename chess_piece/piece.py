
class Piece(object):
    def __init__(self, position, colour):
        self.name = ""
        self.position = position
        self.colour = colour


    def available_moves(self, direction, board):
        possible_moves = []

        for d in direction:
            pos = self.position
            i = 0

            while 0 <= pos[0] + d[0]*i <= 7 and 0 <= pos[1] + d[1]*i <= 7:
                r, c = [pos[0] + d[0]*i, pos[1] + d[1]*i]
                if board[r][c] is None:
                    if [r, c] != pos:
                        possible_moves.append([r,c])
                    i += 1
                else:
                    if board[r][c].colour != self.colour:
                        possible_moves.append([r, c])
                    break
                
        return possible_moves
