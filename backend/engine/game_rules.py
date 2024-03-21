from backend.engine.pieces import King


class GameRules:
    def __init__(self, board):
        self.board = board

    def is_move_valid(self, piece, start_position, end_position):
        # Simulate the move
        original_position = piece.position
        piece.position = end_position

        # Check if the move puts the king in check
        if self.is_check(piece.color):
            # Undo the move
            piece.position = original_position
            return False

        # Undo the move
        piece.position = original_position

        if end_position in piece.get_possible_moves():
            return True
        return False

    def is_opponent_in_check(self, piece, end_position):
        # Store the original position and piece at the end position
        original_position = piece.position
        original_piece_at_end_position = self.board.get_piece(end_position)

        # Simulate the move
        piece.position = end_position
        self.board.set_piece(end_position, piece)

        # Check if the move puts the opponent's king in check
        opponent_color = 'black' if piece.color == 'white' else 'white'
        is_in_check = self.is_check(opponent_color)

        # Undo the move
        piece.position = original_position
        self.board.set_piece(end_position, original_piece_at_end_position)

        return is_in_check

    def is_check(self, color):
        # Get the position of the king
        king_position = next(
            piece.position for piece in self.board.pieces if isinstance(piece, King) and piece.color == color)

        # Check if any opponent piece can reach the king
        for piece in self.board.pieces:
            if piece.color != color and king_position in piece.get_possible_moves():
                return True

        return False

    def is_checkmate(self, color):
        # Check if the king is in check
        if not self.is_check(color):
            return False

        # Check if there are no valid moves left
        for piece in self.board.pieces:
            if piece.color == color:
                for move in piece.get_possible_moves():
                    if self.is_move_valid(piece, piece.position, move):
                        return False

        return True

    def is_castling_valid(self, king, rook):
        # Check if the king and rook have not moved yet
        if king.has_moved or rook.has_moved:
            return False

        # Check if squares between king and rook are unoccupied
        start = min(king.position[1], rook.position[1])
        end = max(king.position[1], rook.position[1])
        for i in range(start + 1, end):
            if self.board.get_piece((king.position[0], i)) is not None:
                return False

        # Check if king is not in check and will not pass through check
        if self.is_check(king.color):
            return False
        for i in range(start + 1, end):
            king.position = (king.position[0], i)
            if self.is_check(king.color):
                king.position = (king.position[0], start)
                return False
        king.position = (king.position[0], start)

        return True

    def is_en_passant_valid(self, pawn, opponent_pawn):
        # TODO: Implement the logic to check en passant eligible
        if opponent_pawn.en_passant_eligible:
            # Check if pawn is in the correct position to perform en passant
            return True
        return False

    def is_promotion_valid(self, pawn):
        if pawn.color == 'white' and pawn.position[0] == 0:
            return True
        elif pawn.color == 'black' and pawn.position[0] == 7:
            return True
        return False
