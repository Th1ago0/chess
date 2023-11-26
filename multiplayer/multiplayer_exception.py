from builtins import Exception

class MultiplayerException(Exception):
    def __init__(self, msg):
        super().__init__(msg)
