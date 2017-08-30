import pygame

from chess_piece import Piece, Pawn, Rook, Bishop, Knight, King, Queen
from player import Player
from chess_game import PlayGame
from chess_game import BoardView

WIDTH = 50
HEIGHT = 50
class Board():
    def __init__(self, current_player):
        self.current_player = current_player
        self.game = PlayGame()
        self.game.start()
        self.lastPosition = [-1,-1]
        self.dragging_place = [-1,-1]

        pygame.init()
        pygame.font.init()
        self.board = pygame.display.set_mode(
            (WIDTH * 8, HEIGHT * 8),
            pygame.HWSURFACE | pygame.DOUBLEBUF)
        pygame.display.set_caption('Chess')



    def on_event(self,event):
        if event.type == pygame.QUIT:
            self.running = False
        else:
            pos = pygame.mouse.get_pos()
            c = pos[0] // HEIGHT
            r = pos[1] // WIDTH
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.game.start_drag_piece_in_position([r,c])
                self.dragging_place = pos

            elif event.type == pygame.MOUSEBUTTONUP:
                self.game.place_dragging_piece_in_position([r,c])
                self.dragging_place = [-1,-1]

            elif event.type == pygame.MOUSEMOTION:
                pos = pygame.mouse.get_pos()
                self.dragging_place = pos
        # check win

    def on_render(self):
        self.render_chess_piece()
        self.render_dragging_piece()
        self.render_available_moves()

        self.render_last_position()
        pygame.display.update()

    def on_execute(self):
        while self.game.playing():
            self.init_chess_board()
            for event in pygame.event.get():
                self.on_event(event)
            self.on_render()
        self.on_cleanup()

    def on_cleanup(self):
        pygame.quit()
    def init_chess_board(self):
        for row in range(8):
            for column in range(8):
                BoardView.render_chess_board(self.board,
                                             [row,column],
                                             (WIDTH * row,
                                             HEIGHT * column,
                                             WIDTH,
                                             HEIGHT))
    def render_available_moves(self):
        for m in self.game.available_moves():
            center = [m[1] * WIDTH + WIDTH // 2, m[0] * HEIGHT + HEIGHT // 2]
            BoardView.render_available_moves(self.board, center)
    def render_dragging_piece(self):
        p = self.game.dragging_piece()
        if p is not None:
            BoardView.render_piece(self.board, p.name,
                        (self.dragging_place[0] - WIDTH // 2,
                        self.dragging_place[1] - HEIGHT // 2))


    def render_chess_piece(self):
        for r in range(8):
            for c in range(8):
                p = self.game.piece_in_position([r,c])
                if p is not None:
                    BoardView.render_piece(self.board, p.name, (HEIGHT * c, WIDTH * r))

    def render_last_position(self):
        if self.lastPosition[0] > 0 and self.lastPosition[1] > 0:
            BoardView.render_last_position(self.board,
                                (WIDTH * self.lastPosition[0] + WIDTH // 2,
                                 HEIGHT * self.lastPosition[1] + HEIGHT // 2,
                                 WIDTH,
                                 HEIGHT))
