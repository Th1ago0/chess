from .chess_exception import ChessException
from boardgame.position import Position

class ChessPosition():
    def __init__(self, column, row):
        if column < "a" or column > "h" or row < 1 or row > 8:
            raise ChessPosition("Error at position: Position does not exist")
        self.row = row;
        self.column = column;
        self.letters = {"a":0,"b":1,"c":2,"d":3,"e":4,"f":5,"g":6,"h":7}
        self.letters_values = {value: key for key, value in self.letters.items()}
    
    def get_row(self):
        return self.row;
    
    def get_column(self):
        return self.column;
    
    def to_position(self):
        return Position(8 - self.row, self.letters[self.column])
    def from_position(self, position):
        return ChessPosition(self.letters_values[position.get_column()], 8 - position.get_row())
    def str(self):
        return f"{self.column}{self.row}"