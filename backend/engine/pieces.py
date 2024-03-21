import abc


class Piece:
    def __init__(self, color, position):
        self.color = color
        self.position = position

    @abc.abstractmethod
    def get_possible_moves(self):
        pass


class Pawn(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)

    def get_possible_moves(self):
        row, col = self.position
        if self.color == 'white':
            return [(row - 1, col)]
        else:  # black pawn
            return [(row + 1, col)]

    def promote(self, new_piece_type):
        if new_piece_type == 'Queen':
            return Queen(self.color, self.position)
        elif new_piece_type == 'Rook':
            return Rook(self.color, self.position)
        elif new_piece_type == 'Bishop':
            return Bishop(self.color, self.position)
        elif new_piece_type == 'Knight':
            return Knight(self.color, self.position)
        else:
            raise ValueError("Invalid piece type for promotion")

    def en_passant_eligible(self):
        # TODO: Implement this logic
        pass


class Rook(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)

    def get_possible_moves(self):
        row, col = self.position
        return [(i, col) for i in range(8)] + [(row, i) for i in range(8)]


class Knight(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)

    def get_possible_moves(self):
        row, col = self.position
        moves = [(row - 2, col - 1), (row - 2, col + 1), (row - 1, col - 2), (row - 1, col + 2),
                 (row + 1, col - 2), (row + 1, col + 2), (row + 2, col - 1), (row + 2, col + 1)]
        return [(r, c) for r, c in moves if 0 <= r < 8 and 0 <= c < 8]


class Bishop(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)

    def get_possible_moves(self):
        row, col = self.position
        moves = []
        for i in range(1, 8):
            moves.append((row + i, col + i))
            moves.append((row + i, col - i))
            moves.append((row - i, col + i))
            moves.append((row - i, col - i))
        return [(r, c) for r, c in moves if 0 <= r < 8 and 0 <= c < 8]


class Queen(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)

    def get_possible_moves(self):
        return (
                Rook(self.color, self.position).get_possible_moves() +
                Bishop(self.color, self.position).get_possible_moves()
        )


class King(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)

    def get_possible_moves(self):
        row, col = self.position
        moves = [
            (row - 1, col),
            (row + 1, col),
            (row, col - 1),
            (row, col + 1),
            (row - 1, col - 1),
            (row - 1, col + 1),
            (row + 1, col - 1),
            (row + 1, col + 1)
        ]
        return [(r, c) for r, c in moves if 0 <= r < 8 and 0 <= c < 8]
