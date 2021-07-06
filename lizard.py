from choices import Choices


class Lizard(Choices):
    def __init__(self):
        super().__init__()

    def get_hierarchy(self, player_one, player_two):
        if player_one.chosen_gesture == "lizard" and player_two.chosen_gesture == "Spock":
            player_one.score += 1
            print(f"{player_one.name} has won with {player_one.chosen_gesture}!")
            print(f"{player_one.name}:{player_one.score} {player_two.name}:{player_two.score}")
        if player_one.chosen_gesture == "lizard" and player_two.chosen_gesture == "Paper":
            player_one.score += 1
            print(f"{player_one.name} has won with {player_one.chosen_gesture}!")
            print(f"{player_one.name}:{player_one.score} {player_two.name}:{player_two.score}")
        if player_two.chosen_gesture == "lizard" and player_one.chosen_gesture == "Spock":
            player_two.score += 1
            print(f"{player_two.name} has won with {player_two.chosen_gesture}!")
            print(f"{player_one.name}:{player_one.score} {player_two.name}:{player_two.score}")
        if player_two.chosen_gesture == "lizard" and player_one.chosen_gesture == "Paper":
            player_two.score += 1
            print(f"{player_two.name} has won with {player_two.chosen_gesture}!")
            print(f"{player_one.name}:{player_one.score} {player_two.name}:{player_two.score}")
