from boardgame.board import Board
from .rook import Rook
from .king import King
from .chess_position import ChessPosition
from .chess_exception import ChessException

class ChessMatch:
    def __init__(self):
        self.board = Board(8, 8);
        self.__turn = 1
        self.__current_player = "WHITE"
        self.setup();
    
    def next_turn(self):
        self.__turn += 1
        if self.__current_player == "WHITE":
            self.__current_player = "BLACK" 
        else:
            self.__current_player = "WHITE" 
            

    def get_turn(self):
        return self.__turn

    def get_current_player(self):
        return self.__current_player

    def possible_moves(self, source_position):
        source = source_position.to_position()
        self.validate_source_position(source)
        return self.board.piece(source.get_row(), source.get_column()).possible_moves()
    
    def perform_chess_move(self, source_position, target_position):
        source = source_position.to_position();
        target = target_position.to_position();
        self.validate_source_position(source);
        self.validate_target_position(source, target)
        captured_piece = self.make_move(source, target);
        self.next_turn()
        return captured_piece;
    
    def make_move(self, source, target):
        piece = self.board.remove_piece(source);
        captured_piece = self.board.remove_piece(target);
        self.board.place_piece(piece, target);
        return captured_piece;
    
    def validate_target_position(self, source, target):
        if not self.board.piece(source.get_row(), source.get_column()).possible_move(target):
            raise ChessException("The chosen piece can not move to target position ")
            
    
    def validate_source_position(self, position):
        piece = self.board.piece(position.get_row(), position.get_column())
        if not self.board.there_is_piece(position):
            raise ChessException("There is no piece on source position");
        
        if self.get_current_player() != piece.get_color():
            raise ChessException("The chosen piece is not yours")
        
        if not piece.is_there_any_possible_move():
            raise ChessException("The chosen piece has no possible move")
    
    def get_pieces(self):
        matrix = [[None for _ in range(self.board.get_rows())] for _ in range(self.board.get_columns())];
        for i in range(self.board.get_rows()):
            for j in range(self.board.get_columns()):
                matrix[i][j] = self.board.piece(i, j);
        return matrix;
    
    def place_new_piece(self, column, row, piece):
        self.board.place_piece(piece, ChessPosition(column, row).to_position())
    
    def setup(self):
        self.place_new_piece("b", 1, Rook(self.board, "WHITE"))
        self.place_new_piece("b", 2, Rook(self.board, "WHITE"))
        self.place_new_piece("c", 1, Rook(self.board, "WHITE"))
        self.place_new_piece("c", 2, Rook(self.board, "WHITE"))
        self.place_new_piece("b", 7, Rook(self.board, "BLACK"))
        self.place_new_piece("b", 8, Rook(self.board, "BLACK"))
        self.place_new_piece("c", 7, Rook(self.board, "BLACK"))
        self.place_new_piece("c", 8, Rook(self.board, "BLACK"))

        self.place_new_piece("d", 4, King(self.board, "BLACK"))
        self.place_new_piece("e", 5, King(self.board, "WHITE"))