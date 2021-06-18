import random





class Human(Player):
    pass

    class AI(Player):
        choice = random.randint(1, 3)


class Game:
    def __init__(self):
        self.player_one = Human
        self.player_two = None

    def run_game(self):
        pass

    def choose_mode(self):
        print("single or multi?")

        response = input()
        if response == 2:
            self.player_one = Human()
        else:
            response == 1
            self.player_two = AI()
