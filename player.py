class Player:
    def __init__(self, name):
        self.name = name
        self.choice = ""
        self.score = 0
        self.gestures = ["rock", "paper", "scissors", "lizard", "spock"]

    def player_choice(self):
        pick = int(input("What is your choice user?: "))
        if pick == 3:
            print("not a valid number, please try again")
        elif pick < 1:
            print("not a valid number, please try again")
        elif pick == 1:
            self.choice = "rock"
        elif pick == 2:
            self.choice = "paper"
        elif pick == 3:
            self.choice = "scissors"


Player()
