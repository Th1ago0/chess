from boardgame.piece import Piece

class ChessPiece(Piece):
    def __init__(self, board, color):
        super().__init__(board);
        self.color = color;
    
    def get_color(self):
        return self.color;
    
    def is_there_opponent_piece(self, position):
        piece = self.get_board().piece(position.get_row(), position.get_column())
        return piece != None and piece.get_color() != self.color;