import pygame

from chess_piece import Piece, Pawn, Rook, Bishop, Knight, King, Queen
from player import Player

DARK=(8,118,49)
LIGHT=(181,221,196)
WIDTH = 50
HEIGHT = 50
LAST_POSTION_COLOUR = (0,0,0)
AVAILABLE_MOVE_COLOUR = (0,0,0)

BLACK = "black"
WHITE = "white"

'''
Class of the board
'''
class Board():
    def __init__(self, current_player):
        self.current_player = current_player
        self.grid = [[None for _ in range(8)] for _ in range(8)]
        self.grid_init()
        self.lastPosition = [-1,-1]
        self.running = True
        self.dragging = False
        self.dragging_piece = None
        self.dragging_place = [-1,-1]
        self.available_moves = []

        pygame.init()
        pygame.font.init()
        self.board = pygame.display.set_mode(
            (WIDTH * 8, HEIGHT * 8),
            pygame.HWSURFACE | pygame.DOUBLEBUF)
        pygame.display.set_caption('Chess')

    def grid_init(self):
        self.grid[0] = [Rook([0,0],BLACK),
                        Knight([0,1],BLACK),
                        Bishop([0,2],BLACK),
                        Queen([0,3],'black'),
                        King([0,4],'black'),
                        Bishop([0,5],'black'),
                        Knight([0,6],'black'),
                        Rook([0,7],'black')]

        self.grid[-1] = [Rook([7,0],'white'),
                         Knight([7,1],'white'),
                         Bishop([7,2],'white'),
                         Queen([7,3],'white'),
                         King([7,4],'white'),
                         Bishop([7,5],'white'),
                         Knight([7,6],'white'),
                         Rook([7,7],'white')]

        self.grid[1] = [Pawn([1, i], 'black') for i in range(8)]
        self.grid[-2] = [Pawn([6, i], 'white') for i in range(8)]

    def on_event(self,event):
        if event.type == pygame.QUIT:
            self.running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            c = pos[0] // HEIGHT
            r = pos[1] // WIDTH

            if self.grid[r][c] is not None:
                self.dragging = True
                self.dragging_piece = self.grid[r][c]
                self.dragging_place = pos
                self.grid[r][c] = None
                self.available_moves = self.dragging_piece.available_moves()

        elif event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            c = pos[0] // HEIGHT
            r = pos[1] // WIDTH
            if self.dragging:
                if self.grid[r][c] is not None:
                    p = self.grid[r][c]
                    if p.colour == self.dragging_piece.colour:
                        pos = self.dragging_piece.position
                        self.grid[pos[0]][pos[1]] = self.dragging_piece
                    else:
                        #identify if the dragging win
                        if False:
                            pass
                        else:
                            pos = self.dragging_piece.position
                            self.grid[pos[0]][pos[1]] = self.dragging_piece

                else:
                    self.dragging_piece.position = [r,c]
                    self.grid[r][c] = self.dragging_piece
            else:
                pos = self.dragging_piece.position
                self.grid[pos[0]][pos[1]] = self.dragging_piece

            self.dragging = False
            self.dragging_piece = None
            self.dragging_place = [-1,-1]
            self.available_moves = []

        elif event.type == pygame.MOUSEMOTION:
            pos = pygame.mouse.get_pos()
            if self.dragging:
                self.dragging_place = pos

        #check win


    def on_render(self):
        self.render_chess_piece()
        self.render_dragging_piece()
        self.render_available_moves()
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
                colour = DARK
                if (row % 2 == 0 and column % 2 == 0) or (row % 2 == 1 and column % 2 == 1):
                    colour = LIGHT
                pygame.draw.rect(self.board, colour, (WIDTH * column, HEIGHT * row, WIDTH, HEIGHT), 0)


    def render_available_moves(self):
        if not self.available_moves is None:
            moves = []
            for m in self.available_moves:
                if self.grid[m[0]][m[1]] is None:
                    moves.append(m)
            for m in moves:
                center = [m[1] * WIDTH + WIDTH // 2, m[0] * HEIGHT + HEIGHT // 2]
                radius = 10
                pygame.draw.circle(self.board, AVAILABLE_MOVE_COLOUR, center, radius, 0)

    def render_dragging_piece(self):
        if self.dragging:
            piece = pygame.image.load('Images/' + self.dragging_piece.name + '.png')
            self.board.blit(piece ,(self.dragging_place[0] - WIDTH // 2, self.dragging_place[1] - HEIGHT // 2))

    def render_chess_piece(self):
        for r in range(8):
            for c in range(8):
                if self.grid[r][c] is not None:
                    p = self.grid[r][c]
                    piece = pygame.image.load('Images/' + p.name + '.png')
                    self.board.blit(piece,(HEIGHT * c, WIDTH * r))

    def render_last_position(self):
        if self.lastPosition[0] > 0 and self.lastPosition[1] > 0:
            pygame.draw.rect(self._display_surf, LAST_POSTION_COLOUR,
                             (WIDTH * self.lastPosition[0] + WIDTH // 2,
                              WIDTH * self.lastPosition[1] + WIDTH // 2,
                              WIDTH,
                              WIDTH), 1)
