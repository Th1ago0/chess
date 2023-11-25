from chess.chess_position import ChessPosition
import os

## Class to manipulate the user interface and graphics;
class Graphic:
    def clear_screen(self):
       # For Windows
       if os.name == 'nt':
            os.system('cls')
       # For Unix based systems;
       else:
            os.system('clear')
    
    #def print_captured_pieces(self, pieces):
    #    white = list(filter(lambda x: x.get_color() == "WHITE", pieces))
    #    white = list(filter(lambda x: x.get_color() == "BLACK", pieces))


    def print_match(self, chess_match):
        self.print_graphics(chess_match.get_pieces())
        print()
        print(f"Turn: {chess_match.get_turn()}")
        if not chess_match.get_check_mate():
            print(f"Waiting Player: {chess_match.get_current_player()}")
            if chess_match.get_check():
                print("CHECK!")
        else:
            print("CHECKMATE!")
            print(f"Winner: {chess_match.get_current_player()}")
        
    # def print_match_mtplr(self, chess_match, host_type):
    #     self.print_graphics(chess_match.get_pieces())
    #     print()
    #     print(f"Turn: {chess_match.get_turn()}")
    #     if not chess_match.get_check_mate():
    #         print(f"Waiting Player: {chess_match.get_current_player()}")
    #         if chess_match.get_check():
    #             print("CHECK!")
    #     else:
    #         print("CHECKMATE!")
    #         print(f"Winner: {chess_match.get_current_player()}")

    # Prints the graphics and the coordinates;
    def print_graphics(self, pieces, possible_moves=False):
        for i in range(len(pieces)):
            print(8 - i, end="  ");
            for j in range(len(pieces)):
                if (i+j) % 2 == 0:
                    if possible_moves:
                        self.print_piece_bg(pieces[i][j], "BLACK", possible_moves[i][j]);
                    else:
                        self.print_piece_bg(pieces[i][j], "BLACK");
                else:
                    if possible_moves:
                        self.print_piece_bg(pieces[i][j], "WHITE", possible_moves[i][j]);
                    else:
                        self.print_piece_bg(pieces[i][j], "WHITE");

            print();
        print("    a  b  c  d  e  f  g  h")

    # Prints the piece and the background;
    def print_piece_bg(self, piece, bg_color, possible_move=False):
        content = " "
        if bg_color == "WHITE":
            board_color = "\033[48;2;128;160;96m"
        else:
            board_color = "\033[48;2;238;238;210m"
        if possible_move == True:
            #board_color = "\033[48;5;195m"
            content = "\033[38;5;252m\u25CF"
        elif possible_move == "piece":
            board_color = "\033[48;5;195m"
        
            
        if piece == None:
            print(f"{board_color} {content} \033[0m", end="");
        else:

            print(f"{board_color}\033[30m {piece.__str__()} \033[0m", end="");

    # Reads the chess position given by the user, it receives the coordinates ("a", 1) and not the literal position (0, 0);
    def read_chess_position(self, arg):
        try:
            column = arg[0];
            row = int(arg[1]);
            return ChessPosition(column, row);
        except ValueError as e:
            raise ValueError("Chess position format is invalid") from e;