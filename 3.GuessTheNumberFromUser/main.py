#My answer to the challenge 
def computerNum(x,y):
    return random.randint(x, y)

def main():
    x = int(input("Insert the starting number of the range: "))
    y = int(input("Insert the ending number of the range: "))
    answer = int(input(f"Choose a number between {x} and {y}: "))
    comp_guess = (x+y)//2
    counter = 1
    print(f"The computer guess is: {comp_guess}  [{counter}]")
    while answer != comp_guess:
        # useless verification
        # if x-y == 2 and comp_guess == x:
        #     comp_guess = y
        #     counter += 1
        #     print(f"The computer guess is: {comp_guess}  [{counter}]")

        # elif x-y == 2 and comp_guess == y:
        #     comp_guess = x
        #     counter += 1
        #     print(f"The computer guess is: {comp_guess}  [{counter}]")
        # else:
            if comp_guess < answer:
                x = comp_guess
                counter += 1
                comp_guess = (y+comp_guess)//2
                print(f"The computer guess is: {comp_guess}  [{counter}]")
            else:
                y = comp_guess
                counter += 1
                comp_guess = (x+comp_guess)//2
                print(f"The computer guess is: {comp_guess}  [{counter}]")
    print("Computer won!")

main()



