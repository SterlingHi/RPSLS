from choices import Choices


class Spock(Choices):
    def __init__(self):
        super().__init__()

    def get_hierarchy(self, player_one, player_two):
        if player_one.chosen_gesture == "Spock" and player_two.chosen_gesture == "scissors":
            player_one.score += 1
            print(f"{player_one.name} has won with {player_one.chosen_gesture}!")
            print(f"{player_one.name}:{player_one.score} {player_two.name}:{player_two.score}")
        if player_one.chosen_gesture == "Spock" and player_two.chosen_gesture == "rock":
            player_one.score += 1
            print(f"{player_one.name} has won with {player_one.chosen_gesture}!")
            print(f"{player_one.name}:{player_one.score} {player_two.name}:{player_two.score}")
        if player_two.chosen_gesture == "Spock" and player_one.chosen_gesture == "scissors":
            player_two.score += 1
            print(f"{player_two.name} has won with {player_two.chosen_gesture}!")
            print(f"{player_one.name}:{player_one.score} {player_two.name}:{player_two.score}")
        if player_two.chosen_gesture == "Spock" and player_one.chosen_gesture == "rock":
            player_two.score += 1
            print(f"{player_two.name} has won with {player_two.chosen_gesture}!")
            print(f"{player_one.name}:{player_one.score} {player_two.name}:{player_two.score}")
