class ChessBoard(object):
    def __init__(self):
        self.pieces = {}    # Piece: Location

    def reset_board(self):
        pass

    def add_piece(self, piece, location):
        # TODO: validation for extra piece or out of loc...
        pass

    @staticmethod
    def move_piece(piece):
        if not piece.isalive():
            raise ValueError("This piece is dead")
        # TODO: organise movement sync with Location and ChessPieces

    def get_location(self, piece):
        if piece not in self.pieces:
            raise ValueError("Piece not in board")
        return self.pieces[piece]

