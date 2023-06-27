import random
#klasa zawodnik
class Player:
    def __init__(self,name):
        self.score=[]
        self.name=name
#klasa gra
class Game:
    def __init__(self,trials=5):
        self.trials=trials
        self.points=0
        self.rounds=0

    def draw_the_number(self):
        self.number=random.randint(1,5)

    def choose_number(self):
        x=int(input("Choose the number 1-5:"))
        if x in range(1,6):
            print(f"Your number is: {x}")
            return x
        else:
            print("Invalid number.Please choose another one between 1 and 5")
            return None

    def play_round(self):
        self.rounds+=1
        self.draw_the_number()
        chosen_number=self.choose_number()

        if chosen_number is not None:
            if chosen_number==self.number:
                self.points+=1
                print("Congrats! You have earned one point")
            else:
                print(f"I am sorry! The correct answer was {self.number}")

    def play_game(self):
        for _ in range(self.trials):
            self.play_round()

        print(f"Game over. Your total score is {self.points} out of {self.rounds}")

player_name=input("Put Your name: ")
player=Player(player_name)
game=Game()
game.play_game()


#wylosuj numer
#wybierz numer
#liczba prób
#wygrałeś/przegrałeś
#liczba punktów
#liczba rund
