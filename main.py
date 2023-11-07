from boardgame.position import Position
from boardgame.board import Board
from chess.chess_match import ChessMatch
from graphics.UI import Graphic
from chess.chess_exception import ChessException

# Chess game class;
class ChessGame:
    
    # Function to run the game;
    @classmethod
    def run(self):

        # Instances;
        chess_match = ChessMatch();
        graphic = Graphic()
        
        # Main game loop;
        while not chess_match.get_check_mate():
            try:
                graphic.clear_screen();
                graphic.print_match(chess_match);
                print("Source: ", end="");
                source = graphic.read_chess_position();
                possible_moves = chess_match.possible_moves(source)
                graphic.clear_screen()
                graphic.print_graphics(chess_match.get_pieces(), possible_moves);
                print("Target: ", end="");
                target = graphic.read_chess_position();
                captured_piece = chess_match.perform_chess_move(source, target)
            except ChessException as e:
                input(e)
            except Exception as e:
                input("Position is not valid")
        graphic.clear_screen()
        graphic.print_match(chess_match)

if __name__ == "__main__":
    ChessGame.run();