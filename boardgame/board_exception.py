from builtins import Exception

class BoardException(Exception):
    def __init__(self, msg):
        super().__init__(msg)
