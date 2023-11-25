from .board_exception import BoardException

# The chess board class;
class Board:
    def __init__(self, rows, columns):
        if rows != 8 or columns != 8:
            raise BoardException("Error when building the board: the board must have 8 rows and 8 columns");
        # Atributes to manipulate the board size and the pieces;
        self.__rows = rows;
        self.__columns = columns;
        self.pieces = [[None for _ in range(rows)] for _ in range(columns)];
    
    # Getters;
    def get_rows(self):
        return self.__rows;
        
    def get_columns(self):
        return self.__columns;
        
    # Returns the piece by the position;
    def piece(self, row, column):
        if not self.position_exists(row, column):
            raise BoardException("Position isn't on the board.");
        return self.pieces[row][column];
    
    # Places the piece in position;
    def place_piece(self, piece, position):
        if self.there_is_piece(position):
            raise BoardException(f"There is already a piece on position: {position.str()}");
        self.pieces[position.get_row()][position.get_column()] = piece;
        piece.position = position;
    
    # Checks if the position exists;
    def position_exists(self, row, column):
        return row >= 0 and row < self.__rows and column >= 0 and column < self.__columns;
    
    # Checks if there is a piece on the position;
    def there_is_piece(self, position):
        if not self.position_exists(position.get_row(), position.get_column()):
            raise BoardException("Position isn't on the board.");
        return self.piece(position.get_row(), position.get_column()) != None;
    
    # Removes the piece by the position;
    def remove_piece(self, position):
        if not self.position_exists(position.get_row(), position.get_column()):
            raise BoardException("Position isn't on the board");
        if self.piece(position.get_row(), position.get_column()) == None:
            return None;
        aux = self.piece(position.get_row(), position.get_column());
        self.pieces[position.get_row()][position.get_column()] = None;
        return aux;
