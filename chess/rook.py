from .chess_piece import ChessPiece

class Rook(ChessPiece):
    def __init__(self, board, color):
        super().__init__(board, color)
    
    def str(self):
        return "R";
