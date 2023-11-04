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

    # Prints the graphics and the coordinates;
    def print_graphics(self, pieces):
        for i in range(len(pieces)):
            print(8 - i, end="  ");
            for j in range(len(pieces)):
                if (i+j) % 2 == 0:
                    self._print_piece(pieces[i][j], "WHITE");
                else:
                    self._print_piece(pieces[i][j], "BLACK");
            print();
        print("    a  b  c  d  e  f  g  h")

    # Prints the piece and identifies the piece color;
    def _print_piece(self, piece, color):
        if color == "WHITE":
            board_color = "\033[100m"
        else:
            board_color = "\033[47m"
        if piece == None:
            print(f"{board_color}   \033[0m", end="");
        else:
            if piece.get_color() == "WHITE":
                #board_color = f"{board_color[:4]}97;{board_color[4:]}"
                print(f"{board_color}\033[30m {piece.str()} \033[0m", end="");
            else:
                #board_color = f"{board_color[:4]}30;{board_color[4:]}"
                print(f"{board_color}\033[30m {piece.str_black()} \033[0m", end="");

    # Reads the chess position given by the user, it receives the coordinates ("a", 1) and not the literal position (0, 0);
    def read_chess_position(self):
        try:
            arg = input();
            column = arg[0];
            row = int(arg[1]);
            return ChessPosition(column, row);
        except ValueError as e:
            raise ValueError("Chess position format is invalid") from e;