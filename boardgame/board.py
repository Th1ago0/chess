from .board_exception import BoardException

class Board:
    def __init__(self, rows, columns):
        if rows != 8 or columns != 8:
            raise BoardException("Error when building the board: the board must have 8 rows and 8 columns");
        
        self.rows = rows;
        self.columns = columns;
        self.pieces = [[None for _ in range(rows)] for _ in range(columns)];
        
    def get_rows(self):
        return self.rows;
        
    def get_columns(self):
        return self.columns;
        
    def piece(self, row, column):
        if not self.position_exists(row, column):
            raise BoardException("Position isn't on the board.");
        return self.pieces[row][column];
        
    def place_piece(self, piece, position):
        if self.there_is_piece(position):
            raise BoardException(f"There is already a piece on position: {position.str()}");
        self.pieces[position.get_row()][position.get_column()] = piece;
        piece.position = position;
        
    def position_exists(self, row, column):
        return row >= 0 and row < self.rows and column >= 0 and column < self.columns;
    
    def there_is_piece(self, position):
        if not self.position_exists(position.get_row(), position.get_column()):
            raise BoardException("Position isn't on the board.");
        return self.piece(position.get_row(), position.get_column()) != None;
    
    def remove_piece(self, position):
        if not self.position_exists(position.get_row(), position.get_column()):
            raise BoardException("Position isn't on the board");
        if self.piece(position.get_row(), position.get_column()) == None:
            return None;
        aux = self.piece(position.get_row(), position.get_column());
        self.pieces[position.get_row()][position.get_column()] = None;
        return aux;