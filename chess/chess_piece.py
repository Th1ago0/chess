from boardgame.piece import Piece

class ChessPiece(Piece):
    def __init__(self, board, color):
        super().__init__(board);
        self.color = color;
    
    def get_color(self):
        return self.color;