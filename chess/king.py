from .chess_piece import ChessPiece
from boardgame.position import Position

class King(ChessPiece):
    def __init__(self, board, color):
        super().__init__(board, color)

    def __str__(self):
        if self.get_color() == "WHITE":
            return "\u2654";
        else:
            return "\u265a";
        
    def can_move(self, position):
        piece = self.get_board().piece(position.get_row(), position.get_column())
        return piece == None or piece.get_color() != self.get_color()
        
    def possible_moves(self):
        matrix = [[ False for _ in range(8)] for _ in range(8)]
        pos = Position(0, 0)
        
        # Above possible moves
        pos.set_values(self.position.get_row() - 1, self.position.get_column())
        if self.get_board().position_exists(pos.get_row(), pos.get_column()) and self.can_move(pos):
            if self.is_there_opponent_piece(pos):
                matrix[pos.get_row()][pos.get_column()] = "piece"
            else:
                matrix[pos.get_row()][pos.get_column()] = True
        
        # Below possible moves
        pos.set_values(self.position.get_row() + 1, self.position.get_column())
        if self.get_board().position_exists(pos.get_row(), pos.get_column()) and self.can_move(pos):
            if self.is_there_opponent_piece(pos):
                matrix[pos.get_row()][pos.get_column()] = "piece"
            else:
                matrix[pos.get_row()][pos.get_column()] = True
        
        # Left possible moves
        pos.set_values(self.position.get_row(), self.position.get_column() - 1)
        if self.get_board().position_exists(pos.get_row(), pos.get_column()) and self.can_move(pos):
            if self.is_there_opponent_piece(pos):
                matrix[pos.get_row()][pos.get_column()] = "piece"
            else:
                matrix[pos.get_row()][pos.get_column()] = True
        
        # Right possible moves
        pos.set_values(self.position.get_row(), self.position.get_column() + 1)
        if self.get_board().position_exists(pos.get_row(), pos.get_column()) and self.can_move(pos):
            if self.is_there_opponent_piece(pos):
                matrix[pos.get_row()][pos.get_column()] = "piece"
            else:
                matrix[pos.get_row()][pos.get_column()] = True
        
        # Nw possible moves
        pos.set_values(self.position.get_row() - 1, self.position.get_column() - 1)
        if self.get_board().position_exists(pos.get_row(), pos.get_column()) and self.can_move(pos):
            if self.is_there_opponent_piece(pos):
                matrix[pos.get_row()][pos.get_column()] = "piece"
            else:
                matrix[pos.get_row()][pos.get_column()] = True
        
        # Ne
        pos.set_values(self.position.get_row() - 1, self.position.get_column() + 1)
        if self.get_board().position_exists(pos.get_row(), pos.get_column()) and self.can_move(pos):
            if self.is_there_opponent_piece(pos):
                matrix[pos.get_row()][pos.get_column()] = "piece"
            else:
                matrix[pos.get_row()][pos.get_column()] = True
        
        # Se
        pos.set_values(self.position.get_row() + 1, self.position.get_column() + 1)
        if self.get_board().position_exists(pos.get_row(), pos.get_column()) and self.can_move(pos):
            if self.is_there_opponent_piece(pos):
                matrix[pos.get_row()][pos.get_column()] = "piece"
            else:
                matrix[pos.get_row()][pos.get_column()] = True

        # Sw
        pos.set_values(self.position.get_row() + 1, self.position.get_column() - 1)
        if self.get_board().position_exists(pos.get_row(), pos.get_column()) and self.can_move(pos):
            if self.is_there_opponent_piece(pos):
                matrix[pos.get_row()][pos.get_column()] = "piece"
            else:
                matrix[pos.get_row()][pos.get_column()] = True
        
        return matrix