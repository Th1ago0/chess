from boardgame.piece import Piece
from .chess_position import ChessPosition

class ChessPiece(Piece):
    def __init__(self, board, color):
        super().__init__(board);
        self.__color = color;

    def get_chess_position(self):
        chess_position = ChessPosition()
        return chess_position.from_position(self.position)

    def get_color(self):
        return self.__color;
    
    def is_there_opponent_piece(self, position):
        piece = self.get_board().piece(position.get_row(), position.get_column())
        return piece != None and piece.get_color() != self.__color;