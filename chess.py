import itertools
import pygame

DARK=(8,118,49)
LIGHT=(181,221,196)
WIDTH = 50
HEIGHT = 50
LAST_POSTION_COLOR = (0,0,0)

'''
Class of the Player
'''
class Player():
    def __init__(self, colour, name):
        self.colour = colour
        self.name = name
        self.castle_long = False
        self.castle_short = False

    def __str__(self):
        return '{} as {}'.format(self.name, self.colour)

'''
Class of the board
'''
class Board():
    def __init__(self, current_player):
        self.current_player = current_player
        self.grid = [[0 for _ in range(8)] for _ in range(8)]
        self.lastPosition = [-1,-1]

        pygame.init()
        pygame.font.init()
        self.board = pygame.display.set_mode(
        (WIDTH * 8, HEIGHT * 8),
        pygame.HWSURFACE | pygame.DOUBLEBUF
        )
        pygame.display.set_caption('Chess')

    def on_event(self,event):
        #something mouse drag event or click event, change piece in 'a' postion to 'b'
        k = self.grid[a[0]][a[1]]
        self.grid[a[0]][a[1]] = 0
        self.grid[b[0]][b[1]] = k
        self.lastPosition = b

        #check win

    def on_render(self):
        self.render_chess_piece()
        self.render_last_position()

        pygame.display.update()

    def on_execute(self):
        while True:
            self.chess_board_init()
            for event in pygame.event.get():
                self.on_event(event)
            self.on_render()
        self.remove_piece()

    def chess_board_init(self):
        for row in range(8):
            for column in range(8):
                color = DARK
                if (row % 2 == 0 and column % 2 == 0) or (row % 2 == 1 and column % 2 == 1):
                    color = LIGHT
                pygame.draw.rect(self.board, color, (WIDTH * column, HEIGHT * row, WIDTH, HEIGHT), 0)

    def remove_piece(self):
        pass

    def render_chess_piece(self):
        for r in range(8):
            for c in range(8):
                if self.grid[r][c] > 0:
                    pass
                    #identify which piece it is
                    #pic = piece image
                    #piece = pygame.image.load(pic)
                    #self.board.blit(piece,(WIDTH * r, HEIGHT * c))
    def render_last_position(self):
        if self.lastPosition[0] > 0 and self.lastPosition[1] > 0:
            pygame.draw.rect(self._display_surf, LAST_POSTION_COLOR,
                             (WIDTH * self.lastPosition[0] + WIDTH // 2,
                              WIDTH * self.lastPosition[1] + WIDTH // 2,
                              WIDTH,
                              WIDTH), 1)

'''
Class of the chess Pieces
'''
class Piece():
    def __init__(self, name, position, colour):
        self.name = name
        self.position = position
        self.colour = colour

'''
Classes for individual pieces derived from Piece class
'''
class Pawn(Piece):
    def __init__(self, name, position, colour):
        super().__init__()

class Knight(Piece):
    def __init__(self, name, position, colour):
        super().__init__()

class Rook(Piece):
    def __init__(self, name, position, colour):
        super().__init__()

class Bishop(Piece):
    def __init__(self, name, position, colour):
        super().__init__()

class Queen(Piece):
    def __init__(self, name, position, colour):
        super().__init__()

class King(Piece):
    def __init__(self, name, position, colour):
        super().__init__()

if __name__ == '__main__':
    board = Board('White')
