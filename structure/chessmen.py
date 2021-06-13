from abc import ABC, abstractmethod
import random


class ChessPiece(ABC):
    ID = 0

    def __init__(self, alive=True):
        self.piece_type = self.__class__
        self.alive = alive
        self.id = ChessPiece.ID

    def __str__(self):
        return f"{self.get_piece_type()}: {int(self.is_alive())}"

    def get_piece_type(self):
        return self.piece_type

    def is_alive(self):
        return self.alive

    def set_dead(self):
        self.alive = False

    @abstractmethod
    def choose_move(self):
        pass

    @abstractmethod
    def can_kill(self):
        pass


class Pawn(ChessPiece):
    def __init__(self):
        super().__init__()
        self.num_moves = 0

    def get_move_number(self):
        return self.num_moves

    def can_kill(self):
        # TODO: Complete once location and field enable it
        pass

    @staticmethod
    def kill(other):
        other.set_dead()
        # TODO: Add

    def choose_move(self):
        if self.can_kill():
            # TODO: Make move on top of other
            pass
        elif self.get_move_number() == 0:
            moves = [(0.0, 1.0), (0.0, 2.0)]
            return random.choice(moves)
        else:
            return tuple((0.0, 1.0))


class Knight(ChessPiece):
    pass


class Bishop(ChessPiece):
    pass


class Rook(ChessPiece):
    pass


class Queen(ChessPiece):
    pass


class King(ChessPiece):
    pass

