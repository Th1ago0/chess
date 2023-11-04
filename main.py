from boardgame.position import Position
from boardgame.board import Board
from chess.chess_match import ChessMatch
from graphics.UI import Graphic
from chess.chess_exception import ChessException

# Chess game class;
class Game:
    
    # Function to run tue game;
    def run(self):
        
        # Instances;
        chess_match = ChessMatch();
        graphic = Graphic()
        
        # Main game loop;
        while True:
            try:
                graphic.clear_screen();
                graphic.print_graphics(chess_match.get_pieces());
                print("Source: ", end="");
                source = graphic.read_chess_position();
                print("Target: ", end="");
                target = graphic.read_chess_position();
                captured_piece = chess_match.perform_chess_move(source, target)
            except ChessException as e:
                print(e)
                input()
            except Exception as e:
                print(e)
                input()
                

chess = Game();
chess.run();