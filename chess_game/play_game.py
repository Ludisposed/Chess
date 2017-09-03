from chess_piece import Piece, Pawn, Rook, Bishop, Knight, King, Queen

BLACK = "black"
WHITE = "white"

class PlayGame(object):
    def __init__(self):
        self.__pieces = self.init_game_pieces()
        self.__dragging_piece = None
        self.__playing = False
        self.__available_moves = []

    def start_drag_piece_in_position(self, position):
        self.__dragging_piece = self.__pieces[position[0]][position[1]]
        self.__pieces[position[0]][position[1]] = None
        self.__available_moves = self.__dragging_piece.available_moves(self.__pieces)

    def place_dragging_piece_in_position(self, position):
        valid_movement = True
        p = self.__pieces[position[0]][position[1]]

        if position in self.__available_moves and (p is None or self.__check_dragging_piece_win_piece_in_position(position)):
            self.__dragging_piece.position = position
            self.__pieces[position[0]][position[1]] = self.__dragging_piece
            
            # Pawn check if moved
            if valid_movement and self.__dragging_piece.name == self.__dragging_piece.colour + '_pawn':
                if not self.__dragging_piece.moved:
                    self.__dragging_piece.if_moved()
        else:
            self.__place_drag_piece_back()
            valid_movement = False

        self.__stop_dragging()
        return valid_movement

    def __place_drag_piece_back(self):
        if self.__dragging_piece is not None:
            pos = self.__dragging_piece.position
            self.__pieces[pos[0]][pos[1]] = self.__dragging_piece

    def __stop_dragging(self):
        self.__dragging_piece = None
        self.__available_moves = []

    def __check_dragging_piece_win_piece_in_position(self, position):
        p = self.__pieces[position[0]][position[1]]
        if p.colour == self.__dragging_piece.colour:
            return False
        return True

    def dragging_piece(self):
        return self.__dragging_piece
    def available_moves(self):
        return self.__available_moves
    def piece_in_position(self, position):
        return self.__pieces[position[0]][position[1]]
    def playing(self):
        return self.__playing
    def start(self):
        self.__playing = True

    def finish(self):
        self.__playing = False

    def init_game_pieces(self):
        pieces = [[None for _ in range(8)] for _ in range(8)]
        pieces[0] = [Rook([0,0],BLACK),
                    Knight([0,1],BLACK),
                    Bishop([0,2],BLACK),
                    Queen([0,3],BLACK),
                    King([0,4],BLACK),
                    Bishop([0,5],BLACK),
                    Knight([0,6],BLACK),
                    Rook([0,7],BLACK)]

        pieces[-1] = [Rook([7,0],WHITE),
                     Knight([7,1],WHITE),
                     Bishop([7,2],WHITE),
                     Queen([7,3],WHITE),
                     King([7,4],WHITE),
                     Bishop([7,5],WHITE),
                     Knight([7,6],WHITE),
                     Rook([7,7],WHITE)]

        pieces[1] = [Pawn([1, i], BLACK) for i in range(8)]
        pieces[-2] = [Pawn([6, i], WHITE) for i in range(8)]

        return pieces
