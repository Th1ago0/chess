from boardgame.position import Position
from boardgame.board import Board
from chess.chess_match import ChessMatch
from graphics.UI import Graphic

class Game:
    def run(self):
        chess_match = ChessMatch();
        graphic = Graphic()
        graphic.print_graphics(chess_match.get_pieces())

chess_game = Game();
chess_game.run();