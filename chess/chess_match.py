from boardgame.board import Board
from .rook import Rook
from .king import King
from .pawn import Pawn
from .bishop import Bishop
from .knight import Knight
from .queen import Queen
from .chess_position import ChessPosition
from .chess_exception import ChessException
from boardgame.position import Position

class ChessMatch:
    def __init__(self):
        self.board = Board(8, 8);
        self.__turn = 1
        self.__current_player = "WHITE"
        self.__check = False
        self.__check_mate = False
        self.pieces_on_the_board = []
        self.captured_pieces = []
        self.setup();
    def get_check(self):
        return self.__check

    def get_check_mate(self):
        return self.__check_mate
        

    def test_check_mate(self, color):
        if not self.test_check(color):
            return False
        
        filtered_list = list(filter(lambda el: el.get_color() == color, self.pieces_on_the_board))
        for el in filtered_list:
            matrix = el.possible_moves()
            for i in range(self.board.get_rows()):
                for j in range(self.board.get_columns()):
                    if matrix[i][j]:
                        source = el.position
                        target = Position(i, j)
                        captured_piece = self.make_move(source, target)
                        test_check = self.test_check(color)
                        self.undo_move(source, target, captured_piece)
                        if not test_check:
                            return False
        return True
        

    def test_check(self, color):
        king_position = self.king(color).get_chess_position().to_position()
        opponent_pieces = list(filter(lambda el: el.get_color() == self.opponent(color), self.pieces_on_the_board))
        for piece in opponent_pieces:
            matrix = piece.possible_moves()
            if matrix[king_position.get_row()][king_position.get_column()]:
                return True
        return False
        
        

    def king(self, color):
        filtered_list = list(filter(lambda el: el.get_color() == color, self.pieces_on_the_board))
        for el in filtered_list:
            if isinstance(el, King):
                return el
        raise ChessException(f"There is no {color} king on the board")
    
    def next_turn(self):
        self.__turn += 1
        if self.__current_player == "WHITE":
            self.__current_player = "BLACK" 
        else:
            self.__current_player = "WHITE" 
        
    def opponent(self, color):
        if color == "WHITE":
            return "BLACK"
        else:
            return "WHITE"

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
        if self.test_check(self.get_current_player()):
            self.undo_move(source, target, captured_piece)
            raise ChessException("You can not put yourself in check")
        if self.test_check(self.opponent(self.get_current_player())):
            self.__check = True
        else:
            self.__check = False
            
        if self.test_check_mate(self.opponent(self.get_current_player())):
            self.__check_mate = True
        else:
            self.next_turn()
        return captured_piece;
    
    def undo_move(self, source, target, captured_piece):
        piece = self.board.remove_piece(target)
        piece.decrease_move_count()
        self.board.place_piece(piece, source)
        if captured_piece != None:
            self.board.place_piece(captured_piece, target)
            self.captured_pieces.remove(captured_piece)
            self.pieces_on_the_board.append(captured_piece)
            
    
    def make_move(self, source, target):
        piece = self.board.remove_piece(source);
        piece.increase_move_count()
        captured_piece = self.board.remove_piece(target);
        self.board.place_piece(piece, target);
        
        if captured_piece != None:
            self.pieces_on_the_board.remove(captured_piece)
            self.captured_pieces.append(captured_piece)
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
        self.pieces_on_the_board.append(piece)
    
    def setup(self):
        # White pieces
        self.place_new_piece("a", 1, Rook(self.board, "WHITE"))
        self.place_new_piece("h", 1, Rook(self.board, "WHITE"))
        self.place_new_piece("c", 1, Bishop(self.board, "WHITE"))
        self.place_new_piece("f", 1, Bishop(self.board, "WHITE"))
        self.place_new_piece("b", 1, Knight(self.board, "WHITE"))
        self.place_new_piece("g", 1, Knight(self.board, "WHITE"))
        self.place_new_piece("a", 2, Pawn(self.board, "WHITE"))
        self.place_new_piece("b", 2, Pawn(self.board, "WHITE"))
        self.place_new_piece("c", 2, Pawn(self.board, "WHITE"))
        self.place_new_piece("d", 2, Pawn(self.board, "WHITE"))
        self.place_new_piece("e", 2, Pawn(self.board, "WHITE"))
        self.place_new_piece("f", 2, Pawn(self.board, "WHITE"))
        self.place_new_piece("g", 2, Pawn(self.board, "WHITE"))
        self.place_new_piece("h", 2, Pawn(self.board, "WHITE"))
        self.place_new_piece("d", 1, King(self.board, "WHITE"))
        self.place_new_piece("e", 1, Queen(self.board, "WHITE"))

        # Black pieces
        self.place_new_piece("a", 8, Rook(self.board, "BLACK"))
        self.place_new_piece("h", 8, Rook(self.board, "BLACK"))
        self.place_new_piece("c", 8, Bishop(self.board, "BLACK"))
        self.place_new_piece("f", 8, Bishop(self.board, "BLACK"))
        self.place_new_piece("b", 8, Knight(self.board, "BLACK"))
        self.place_new_piece("g", 8, Knight(self.board, "BLACK"))
        self.place_new_piece("a", 7, Pawn(self.board, "BLACK"))
        self.place_new_piece("b", 7, Pawn(self.board, "BLACK"))
        self.place_new_piece("c", 7, Pawn(self.board, "BLACK"))
        self.place_new_piece("d", 7, Pawn(self.board, "BLACK"))
        self.place_new_piece("e", 7, Pawn(self.board, "BLACK"))
        self.place_new_piece("f", 7, Pawn(self.board, "BLACK"))
        self.place_new_piece("g", 7, Pawn(self.board, "BLACK"))
        self.place_new_piece("h", 7, Pawn(self.board, "BLACK"))
        self.place_new_piece("d", 8, King(self.board, "BLACK"))
        self.place_new_piece("e", 8, Queen(self.board, "BLACK"))