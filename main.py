class Player:
    def __init__(self):
        self.name = " "
        self.choice = ""
        self.score = 0
        self.gestures = ["rock", "paper", "scissors", "lizard", "spock"]

    def choice(self):
        pass


class Human(Player):
    pass


class AI(Player):
    pass


class Game:
    def __init__(self):
        self.player_one = Human
        self.player_two = None

    def run_game(self):
        pass

    def choose_mode(self):
        print("single or mulit?")
        
        response = input()
        if response == 2:
            self.player_one = Human()
        else:
            response == 1
            self.player_two = AI()

