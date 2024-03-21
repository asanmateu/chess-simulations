class GameEngine:
    def __init__(self, game):
        self.game = game

    # TODO: Send logic to players and write game loop
    def update_points(self, player, points):
        if player == self.game.player1:
            self.game.player1_points += points
        elif player == self.game.player2:
            self.game.player2_points += points

    def update_beaten_pieces(self, player, piece):
        if player == self.game.player1:
            self.game.player1_beaten_pieces.append(piece)
        elif player == self.game.player2:
            self.game.player2_beaten_pieces.append(piece)
