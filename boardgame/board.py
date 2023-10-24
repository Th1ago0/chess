class Board:
    def __init__(self, rows, columns):
        self.rows = rows;
        self.columns = columns;
        self.pieces = [[None for _ in range(rows)] for _ in range(columns)];
        
    def get_rows(self):
        return self.rows;
        
    def set_rows(self, rows):
        self.rows = rows;
        
    def get_columns(self):
        return self.columns;
        
    def set_columns(self, columns):
        self.columns = columns;
        
    def piece(self, rows, columns):
        return self.pieces[rows][columns];
        
    def piece_at_position(self, position):
        return self.pieces[position.get_row][position.get_column];
    def place_piece(self, piece, position):
        self.pieces[position.get_row()][position.get_column()] = piece;
        piece.position = position;
