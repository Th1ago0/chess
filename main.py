from boardgame.position import Position
from boardgame.board import Board
from chess.chess_match import ChessMatch
from graphics.UI import Graphic
from chess.chess_exception import ChessException
from multiplayer.server import Server
from multiplayer.client import Client
from multiplayer.multiplayer_exception import MultiplayerException
import sys

# Chess game class
class ChessGame:
    
    @classmethod
    def exec(self):
        if sys.argv[1:]:
            self.args = sys.argv[1:]
            if self.args[0] == "online":
                self.multiplayer()
            else:
                self.run()
        else:
            self.run()
    
    # Function to run the game
    @classmethod
    def run(self):
        
        # Instances
        chess_match = ChessMatch()
        graphic = Graphic()
        
        # Main game loop
        while not chess_match.get_check_mate():
            try:
                graphic.clear_screen()
                graphic.print_match(chess_match)
                print("Source: ", end="")
                source_raw = input()
                source = graphic.read_chess_position(source_raw)
                possible_moves = chess_match.possible_moves(source)
                graphic.clear_screen()
                graphic.print_graphics(chess_match.get_pieces(), possible_moves)
                print("Target: ", end="")
                target_raw = input()
                target = graphic.read_chess_position(target_raw)
                captured_piece = chess_match.perform_chess_move(source, target)
            except ChessException as e:
                input(e)
            #except Exception as e:
            #    input("Position is not valid")
        graphic.clear_screen()
        graphic.print_match(chess_match)
    
    @classmethod
    def run_multiplayer(self, host, port, server, color):
           
            # Instances
            chess_match = ChessMatch()
            graphic = Graphic()
            server.connect(host, port)

            letters = {"a":0,"b":1,"c":2,"d":3,"e":4,"f":5,"g":6,"h":7}
            # Main game loop
            while not chess_match.get_check_mate():
                try:
                    if chess_match.get_current_player() == color:
                            
                        graphic.clear_screen()
                        if color == "BLACK":
                            graphic.print_match(chess_match, range(7, -1, -1))
                        else:
                            graphic.print_match(chess_match)
                        print("Source: ", end="")
                        source_raw = input()
                        source = graphic.read_chess_position(source_raw)
                        possible_moves = chess_match.possible_moves(source)
                        graphic.clear_screen()
                        if color == "BLACK":
                            graphic.print_graphics(chess_match.get_pieces(), possible_moves, range(7, -1, -1))
                        else:
                            graphic.print_graphics(chess_match.get_pieces(), possible_moves)
                        print("Target: ", end="")
                        target_raw = input()
                        target = graphic.read_chess_position(target_raw)
                        captured_piece = chess_match.perform_chess_move(source, target)
                        server.send(f"{source_raw} {target_raw}")
                    else:
                        graphic.clear_screen()
                        if color == "BLACK":
                            graphic.print_match(chess_match, range(7, -1, -1))
                        else:
                            graphic.print_match(chess_match)
                        print("Waiting...")
                        response = server.receive()
                        response = response.split(" ")
                        print(response)
                        response[0] = Position(8 - int(response[0][1]), letters[response[0][0]])
                        response[1] = Position(8 - int(response[1][1]), letters[response[1][0]])
                        captured_piece = chess_match.perform_chess_move(response[0], response[1], True)
                except ChessException as e:
                        input(e)
                except Exception as e:
                        input(e)
                graphic.clear_screen()
                graphic.print_match(chess_match)
            server.close()
    
    @classmethod
    def multiplayer(self):
        if not len(self.args) == 1:
            if self.args[1] == "p1":
                graphic = Graphic()
                graphic.clear_screen()
                print("< CHESS GAME MULTIPLAYER MODE >\n")
                host = input("Host: ")
                port = int(input("Port: "))
                server = Server()
                
                print("Waiting a player...")
                self.run_multiplayer(host, port, server, "WHITE")
                
            elif self.args[1] == "p2":
                graphic = Graphic()
                graphic.clear_screen()
                print("< CHESS GAME MULTIPLAYER MODE >\n")
                host = input("Host: ")
                port = int(input("Port: "))
                client = Client()
                
                print("Waiting a player...")
                self.run_multiplayer(host, port, client, "BLACK")
            else:
                raise MultiplayerException("Arg Error: Invalid arguments")
        else:
            raise MultiplayerException("Arg Error: You must specify the player")

if __name__ == "__main__":
    ChessGame.exec()
