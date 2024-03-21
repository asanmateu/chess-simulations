class Board:
    def __init__(self):
        self.grid = [[None for _ in range(8)] for _ in range(8)]

    def get_piece(self, position):
        return self.grid[position[0]][position[1]]

    def set_piece(self, position, piece):
        self.grid[position[0]][position[1]] = piece

    def remove_piece(self, position):
        self.grid[position[0]][position[1]] = None

    def move_piece(self, start_position, end_position):
        piece = self.get_piece(start_position)
        self.remove_piece(start_position)
        self.set_piece(end_position, piece)
