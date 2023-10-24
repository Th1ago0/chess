class Graphic:
    def print_graphics(self, pieces):
        for i in range(len(pieces)):
            print(8 - i, end="  ");
            for j in range(len(pieces)):
                self._print_piece(pieces[i][j]);
            print("\n");
        print("   a  b  c  d  e  f  g  h")
    def _print_piece(self, piece):
        if piece == None:
            print("-", end="  ");
        else:
            print(piece.str(), end="  ");