from .chess_piece import ChessPiece
from boardgame.position import Position

class Rook(ChessPiece):
    def __init__(self, board, color):
        super().__init__(board, color)
    
    def str(self):
        return "\u2656";
        
    def str_black(self):
        return "\u265c";
    def possible_moves(self):
        
        matrix = [[ False for _ in range(8)] for _ in range(8)]
        
        pos = Position(0, 0)
        # Up
        pos.set_values(self.position.get_row()-1,self.position.get_column())
        while self.get_board().position_exists(pos.get_row(), pos.get_column()) and not self.get_board().there_is_piece(pos):

            matrix[pos.get_row()][pos.get_column()] = True
            pos.set_row(pos.get_row()-1)
    
        if self.get_board().position_exists(pos.get_row(), pos.get_column()) and self.is_there_opponent_piece(pos):
            matrix[pos.get_row()][pos.get_column()] = True
            
            
        # Below
        pos.set_values(self.position.get_row()+1,self.position.get_column())
        while self.get_board().position_exists(pos.get_row(), pos.get_column()) and not self.get_board().there_is_piece(pos):

            matrix[pos.get_row()][pos.get_column()] = True
            pos.set_row(pos.get_row()+1)
    
        if self.get_board().position_exists(pos.get_row(), pos.get_column()) and self.is_there_opponent_piece(pos):
            matrix[pos.get_row()][pos.get_column()] = True
            
            
            
        # Left
        pos.set_values(self.position.get_row(), self.position.get_column()-1)
        while self.get_board().position_exists(pos.get_row(), pos.get_column()) and not self.get_board().there_is_piece(pos):

            matrix[pos.get_row()][pos.get_column()] = True
            pos.set_column(pos.get_column()-1)
    
        if self.get_board().position_exists(pos.get_row(), pos.get_column()) and self.is_there_opponent_piece(pos):
            matrix[pos.get_row()][pos.get_column()] = True
        
        # Right
        pos.set_values(self.position.get_row(), self.position.get_column()+1)
        while self.get_board().position_exists(pos.get_row(), pos.get_column()) and not self.get_board().there_is_piece(pos):

            matrix[pos.get_row()][pos.get_column()] = True
            pos.set_column(pos.get_column()+1)
    
        if self.get_board().position_exists(pos.get_row(), pos.get_column()) and self.is_there_opponent_piece(pos):
            matrix[pos.get_row()][pos.get_column()] = True

        return matrix
