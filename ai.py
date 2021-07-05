from player import Player
import random


class AI(Player):
    def __init__(self):
        super().__init__()

    def player_choice(self):
        self.choice = random.choice(self.player_gestures)
        return self.choice
