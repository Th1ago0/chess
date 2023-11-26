from .chess_piece import ChessPiece
from boardgame.position import Position

class Pawn(ChessPiece):
    def __init__(self, board, color):
        super().__init__(board, color)

    def __str__(self):
        if self.get_color() == "WHITE":
            return "\u2659"
        else:
            return "\u265F"
    
    def possible_moves(self):
        matrix = [[False for _ in range(8)] for _ in range(8)]
        pos = Position(0, 0)
        
        if self.get_color() == "WHITE":
            pos.set_values(self.position.get_row() - 1, self.position.get_column())
            one_above = self.get_board().position_exists(pos.get_row(), pos.get_column()) and not self.get_board().there_is_piece(pos)
            if one_above:
                matrix[pos.get_row()][pos.get_column()] = True
            
            pos.set_values(self.position.get_row() - 2, self.position.get_column())
            if self.get_board().position_exists(pos.get_row(), pos.get_column()) and not self.get_board().there_is_piece(pos) and self.get_move_count() == 0 and one_above:
                matrix[pos.get_row()][pos.get_column()] = True
            
            pos.set_values(self.position.get_row() - 1, self.position.get_column() - 1)
            if self.get_board().position_exists(pos.get_row(), pos.get_column()) and self.is_there_opponent_piece(pos):
                matrix[pos.get_row()][pos.get_column()] = "piece"
                
            pos.set_values(self.position.get_row() - 1, self.position.get_column() + 1)
            if self.get_board().position_exists(pos.get_row(), pos.get_column()) and self.is_there_opponent_piece(pos):
                matrix[pos.get_row()][pos.get_column()] = "piece"
        else:
            pos.set_values(self.position.get_row() + 1, self.position.get_column())
            one_above = self.get_board().position_exists(pos.get_row(), pos.get_column()) and not self.get_board().there_is_piece(pos)
            if one_above:
                matrix[pos.get_row()][pos.get_column()] = True
            
            pos.set_values(self.position.get_row() + 2, self.position.get_column())
            if self.get_board().position_exists(pos.get_row(), pos.get_column()) and not self.get_board().there_is_piece(pos) and self.get_move_count() == 0 and one_above:
                matrix[pos.get_row()][pos.get_column()] = True
            
            pos.set_values(self.position.get_row() + 1, self.position.get_column() + 1)
            if self.get_board().position_exists(pos.get_row(), pos.get_column()) and self.is_there_opponent_piece(pos):
                matrix[pos.get_row()][pos.get_column()] = "piece"
                
            pos.set_values(self.position.get_row() + 1, self.position.get_column() - 1)
            if self.get_board().position_exists(pos.get_row(), pos.get_column()) and self.is_there_opponent_piece(pos):
                matrix[pos.get_row()][pos.get_column()] = "piece"
        return matrix