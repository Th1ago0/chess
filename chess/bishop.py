from .chess_piece import ChessPiece
from boardgame.position import Position

# Class to the bishop;
class Bishop(ChessPiece):
    def __init__(self, board, color):
        super().__init__(board, color)

    def __str__(self):
        if self.get_color() == "WHITE":
            return "\u2657";
        else:
            return "\u265D";
    
    # Possible bishop moves
    def possible_moves(self):
        
        # Two-dimensional vector containing the possible movements
        matrix = [[ False for _ in range(8)] for _ in range(8)];
        pos = Position(0, 0);

        # Possible movement to the northwest;
        pos.set_values(self.position.get_row()-1,self.position.get_column()-1);
        while self.get_board().position_exists(pos.get_row(), pos.get_column()) and not self.get_board().there_is_piece(pos):

            matrix[pos.get_row()][pos.get_column()] = True
            pos.set_values(pos.get_row()-1, pos.get_column()-1)
    
        if self.get_board().position_exists(pos.get_row(), pos.get_column()) and self.is_there_opponent_piece(pos):
            matrix[pos.get_row()][pos.get_column()] = "piece"

        # Ne
        pos.set_values(self.position.get_row()-1,self.position.get_column()+1)
        while self.get_board().position_exists(pos.get_row(), pos.get_column()) and not self.get_board().there_is_piece(pos):

            matrix[pos.get_row()][pos.get_column()] = True
            pos.set_values(pos.get_row()-1, pos.get_column()+1)
    
        if self.get_board().position_exists(pos.get_row(), pos.get_column()) and self.is_there_opponent_piece(pos):
            matrix[pos.get_row()][pos.get_column()] = "piece"

        # Se
        pos.set_values(self.position.get_row()+1, self.position.get_column()+1)
        while self.get_board().position_exists(pos.get_row(), pos.get_column()) and not self.get_board().there_is_piece(pos):

            matrix[pos.get_row()][pos.get_column()] = True
            pos.set_values(pos.get_row()+1, pos.get_column()+1)
    
        if self.get_board().position_exists(pos.get_row(), pos.get_column()) and self.is_there_opponent_piece(pos):
            matrix[pos.get_row()][pos.get_column()] = "piece"
        
        # Sw
        pos.set_values(self.position.get_row()+1, self.position.get_column()-1)

        while self.get_board().position_exists(pos.get_row(), pos.get_column()) and not self.get_board().there_is_piece(pos):

            matrix[pos.get_row()][pos.get_column()] = True
            pos.set_values(pos.get_row()+1, pos.get_column()-1)
    
        if self.get_board().position_exists(pos.get_row(), pos.get_column()) and self.is_there_opponent_piece(pos):
            matrix[pos.get_row()][pos.get_column()] = "piece"

        return matrix
