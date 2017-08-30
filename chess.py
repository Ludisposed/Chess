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
        self.grid = [['' for _ in range(8)] for _ in range(8)]
        self.grid_init()
        self.lastPosition = [-1,-1]
        self.running = True
        self.dragging = False
        self.dragging_piece = ''
        self.dragging_place = [-1,-1]
        self.last_position_before_drag = [-1,-1]

        pygame.init()
        pygame.font.init()
        self.board = pygame.display.set_mode(
            (WIDTH * 8, HEIGHT * 8),
            pygame.HWSURFACE | pygame.DOUBLEBUF)
        pygame.display.set_caption('Chess')
    def grid_init(self):
        self.grid[0] = ['black_rook','black_knight','black_bishop','black_queen','black_king','black_bishop','black_knight','black_rook']
        self.grid[-1] = ['white_rook','white_knight','white_bishop','white_queen','white_king','white_bishop','white_knight','white_rook']
        self.grid[1] = ['black_pawn' for _ in range(8)]
        self.grid[-2] = ['white_pawn' for _ in range(8)]

    def on_event(self,event):
        if event.type == pygame.QUIT:
            self.running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            c = pos[0] // HEIGHT
            r = pos[1] // WIDTH
            if len(self.grid[r][c])>0:
                self.dragging = True
                self.dragging_piece = self.grid[r][c]
                self.dragging_place = pos
                self.grid[r][c] = ''
                self.last_position_before_drag = [r,c]
        elif event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            c = pos[0] // HEIGHT
            r = pos[1] // WIDTH
            if self.dragging:
                if len(self.grid[r][c]) > 0:

                    if self.grid[r][c].split('_')[0] == self.dragging_piece.split('_')[0]:
                        self.grid[self.last_position_before_drag[0]][self.last_position_before_drag[1]] = self.dragging_piece
                    else:
                        #identify if the dragging win
                        if False:
                            pass
                        else:
                            self.grid[self.last_position_before_drag[0]][self.last_position_before_drag[1]] = self.dragging_piece

                else:
                    self.grid[r][c] = self.dragging_piece

            self.dragging = False
            self.dragging_piece = None
            self.dragging_place = [-1,-1]
            self.last_position_before_drag = [-1,-1]
        elif event.type == pygame.MOUSEMOTION:
            pos = pygame.mouse.get_pos()
            if self.dragging:
                self.dragging_place = pos

        #check win


    def on_render(self):
        self.render_chess_piece()
        self.render_dragging_piece()
        self.render_last_position()
        pygame.display.update()

    def on_execute(self):
        while self.running:
            self.chess_board_init()
            for event in pygame.event.get():
                self.on_event(event)
            self.on_render()
        self.on_cleanup()

    def on_cleanup(self):
        pygame.quit()

    def chess_board_init(self):
        for row in range(8):
            for column in range(8):
                color = DARK
                if (row % 2 == 0 and column % 2 == 0) or (row % 2 == 1 and column % 2 == 1):
                    color = LIGHT
                pygame.draw.rect(self.board, color, (WIDTH * column, HEIGHT * row, WIDTH, HEIGHT), 0)
    def render_dragging_piece(self):
        if self.dragging:
            piece = pygame.image.load('Images/' + self.dragging_piece + '.png')
            self.board.blit(piece ,(self.dragging_place[0] - WIDTH // 2, self.dragging_place[1] - HEIGHT // 2))

    def render_chess_piece(self):
        for r in range(8):
            for c in range(8):
                if len(self.grid[r][c]) > 0:
                    piece = pygame.image.load('Images/' + self.grid[r][c] + '.png')
                    self.board.blit(piece,(HEIGHT * c, WIDTH * r))

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
    board.on_execute()
