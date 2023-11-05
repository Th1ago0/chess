from abc import ABC, abstractmethod

class Piece(ABC):
    def __init__(self, board):
        self.__board = board;
        self.position = None;
        
    def get_board(self):
        return self.__board;
    
    @abstractmethod
    def possible_moves(self):
        pass

    def possible_move(self, position):
        return self.possible_moves()[position.get_row()][position.get_column()]
        
    def is_there_any_possible_move(self):
        matrix = self.possible_moves()
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if matrix[i][j]:
                    return True;
        return False;
