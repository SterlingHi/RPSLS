class Player:
    def __init__(self, name):
        self.name = name
        self.choice = ""
        self.score = 0
        self.gestures = ["rock", "paper", "scissors", "lizard", "spock"]

    def player_choice(self):

        gesture_index = 0
        for gesture in self.gestures:
            print(f"Press {gesture_index} for {gesture}.")
            gesture_index += 1
        self.choice = input("Choose your gesture.")
        if int(self.choice) > 4:
            print("Sorry, choose zero through four.")
            self.choice()
        self.choice = self.gestures[int(self.choice)]
        return self.choice
