from abc import ABC, abstractmethod

# The class to the piece
class Piece(ABC):
    def __init__(self, board):
        self.__board = board
        self.position = None
    
    # Getter
    def get_board(self):
        return self.__board
    
    # Abstract method for the possible moves of each chess piece
    @abstractmethod
    def possible_moves(self):
        pass

    # Checks if any move is possible by the position
    
    def possible_move(self, position):
        return self.possible_moves()[position.get_row()][position.get_column()]
    
    # Checks if there is at least one possible move
    def is_there_any_possible_move(self):
        matrix = self.possible_moves()
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if matrix[i][j]:
                    return True
        return Fals
