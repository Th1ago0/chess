# Class to manipulate the position of each square and piece on the board
class Position:
    def __init__(self, row, column):
        self.__row = row
        self.__column = column
    
    # Returns the row and column in string format
    def str(self):
        return f"{self.__row}, {self.__column}"
        
    # Getters and Setters
    def set_row(self, row):
        self.__row = row
        
    def get_row(self):
        return self.__row
        
    def set_column(self, column):
        self.__column = column
        
    def get_column(self):
        return self.__column
    
    def set_values(self, row, column):
        self.__row = row
        self.__column = column
