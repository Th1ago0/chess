from boardgame.board import Board
from .rook import Rook
from boardgame.position import Position

class ChessMatch:
    def __init__(self):
        self.board = Board(8, 8);
        self.setup();
    
    def get_pieces(self):
        matrix = [[None for _ in range(self.board.get_rows())] for _ in range(self.board.get_columns())];
        for i in range(self.board.get_rows()):
            for j in range(self.board.get_columns()):
                matrix[i][j] = self.board.piece(i, j);
        return matrix;
    
    def setup(self):
        self.board.place_piece(Rook(self.board, "WHITE"), Position(5, 2));
        self.board.place_piece(Rook(self.board, "WHITE"), Position(5, 2));