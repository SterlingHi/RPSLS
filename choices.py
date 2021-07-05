from human import Human
from ai import AI


class Choices:

    def __init__(self):
        self.choice_names = ["rock", "paper", "scissors", "lizard", "Spock"]
        self.player_one = Human("name")
        self.player_one.score = 0
        self.player_two = Human("name") or AI()
        self.player_two.score = 0

    def get_hierarchy(self):
        if self.player_one == self.choice_names and self.player_two == self.choice_names:
            self.player_one.score += 1
