from player import Player
import random


class AI(Player):
    def __init__(self):
        super().__init__()

    def player_choice(self):
        self.choice = random.randint(0, len(self.gestures))
