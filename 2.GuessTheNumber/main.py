#My answer to the challenge 
import random

def computerNum(x,y):
    return random.randint(x, y)

def main():
    x = int(input("Insert the starting number of the range: "))
    y = int(input("Insert the ending number of the range: "))
    user_guess = int(input(f"Guess a number between {x} and {y}: "))
    answer = computerNum(x, y)
    while  answer != user_guess:
        if answer < user_guess:
            print("Try a lower number!")        
            user_guess = int(input(f"Guess a number between {x} and {y}: "))

        else:
            print("Try a higher number!")
            user_guess = int(input(f"Guess a number between {x} and {y}: "))
    print("You won!")

main()



