import math
import random

class Player:
    def __init__(self, letter):
        # x or o
        self.letter = letter
    def get_move(self,game):
        pass

class RandomComputerPlayer(Player): #inherits from Player
    def __init__(self, letter):
        super().__init__(letter) # call the init on Player
    
    def get_move(self,game):
        square = random.choice(game.avaiable_moves())
        return square
class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move (0-8): ')
            try:
                val = int(square)
                if val not in game.avaiable_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print("Invalid square. Try again.")
        return val
