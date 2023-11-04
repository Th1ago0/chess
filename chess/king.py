from .chess_piece import ChessPiece

class King(ChessPiece):
    def __init__(self, board, color):
        super().__init__(board, color)
    
    def str(self):
        return "\u2654";
    def str_black(self):
        return "\u265a";
    def possible_moves(self):
        matrix = [[ False for _ in range(8)] for _ in range(8)]
        return matrix