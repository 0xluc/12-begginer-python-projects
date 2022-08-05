from sample_madlibs import hp, code, zombie, hungergames
import random

if __name__ == "__main__":
    #choose a random storyline
    m = random.choice([hp, code, zombie, hungergames])
    m.madlib()