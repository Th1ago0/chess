from .chess_piece import ChessPiece
from boardgame.position import Position

## Rook piece
class Rook(ChessPiece):
    def __init__(self, board, color):
        super().__init__(board, color)
    
    def __str__(self):
        if self.get_color() == "WHITE":
            return "\u2656";
        else:
            return "\u265c";
    
    # Possible rook moves
    def possible_moves(self):
        
        # Two-dimensional vector containing the possible movements
        matrix = [[ False for _ in range(8)] for _ in range(8)]
        pos = Position(0, 0)

        # Above possible moves
        pos.set_values(self.position.get_row()-1,self.position.get_column())
        while self.get_board().position_exists(pos.get_row(), pos.get_column()) and not self.get_board().there_is_piece(pos):

            matrix[pos.get_row()][pos.get_column()] = True
            pos.set_row(pos.get_row()-1)
    
        if self.get_board().position_exists(pos.get_row(), pos.get_column()) and self.is_there_opponent_piece(pos):
            matrix[pos.get_row()][pos.get_column()] = "piece"

        # Below possible moves
        pos.set_values(self.position.get_row()+1,self.position.get_column())
        while self.get_board().position_exists(pos.get_row(), pos.get_column()) and not self.get_board().there_is_piece(pos):

            matrix[pos.get_row()][pos.get_column()] = True
            pos.set_row(pos.get_row()+1)
    
        if self.get_board().position_exists(pos.get_row(), pos.get_column()) and self.is_there_opponent_piece(pos):
            matrix[pos.get_row()][pos.get_column()] = "piece"

        # Left possible moves
        pos.set_values(self.position.get_row(), self.position.get_column()-1)
        while self.get_board().position_exists(pos.get_row(), pos.get_column()) and not self.get_board().there_is_piece(pos):

            matrix[pos.get_row()][pos.get_column()] = True
            pos.set_column(pos.get_column()-1)
    
        if self.get_board().position_exists(pos.get_row(), pos.get_column()) and self.is_there_opponent_piece(pos):
            matrix[pos.get_row()][pos.get_column()] = "piece"
        
        pos.set_values(self.position.get_row(), self.position.get_column()+1)

        # Right possible moves
        while self.get_board().position_exists(pos.get_row(), pos.get_column()) and not self.get_board().there_is_piece(pos):

            matrix[pos.get_row()][pos.get_column()] = True
            pos.set_column(pos.get_column()+1)
    
        if self.get_board().position_exists(pos.get_row(), pos.get_column()) and self.is_there_opponent_piece(pos):
            matrix[pos.get_row()][pos.get_column()] = "piece"

        return matrix
