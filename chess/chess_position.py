from .chess_exception import ChessException
from boardgame.position import Position

class ChessPosition():
    def __init__(self, column, row):
        if column < "a" or column > "h" or row < 1 or row > 8:
            raise ChessPosition("Error at position: Position does not exist")
        self.__row = row;
        self.__column = column;
        self.__letters = {"a":0,"b":1,"c":2,"d":3,"e":4,"f":5,"g":6,"h":7}
        self.__letters_values = {value: key for key, value in self.__letters.items()}
    
    def get_row(self):
        return self.__row;
    
    def get_column(self):
        return self.__column;
    
    def to_position(self):
        return Position(8 - self.__row, self.__letters[self.__column])
    def from_position(self, position):
        return ChessPosition(self.__letters_values[position.get_column()], 8 - position.get_row())
    def str(self):
        return f"{self.__column}{self.__row}"