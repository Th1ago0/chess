from boardgame.board_exception import BoardException

class ChessException(BoardException):
    def __init__(self, msg):
        super().__init__(msg)
