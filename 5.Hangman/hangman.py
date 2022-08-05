import random
import string
from words import words

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word: #search for another word
        word = random.choice(words)
    return word

def hangman():
    word = get_valid_word(words).upper()
    word_letters = set(word) #split into a list with letters
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    lives = 7

    while len(word_letters) > 0 and lives > 0:

        print(f"You have {lives} lives left and your have used these letters: ", ' '.join(used_letters))

        word_list = [letter if letter in used_letters else "-" for letter in word]
        print("Current word: ", ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives -= 1 
                print("Letter is not in the word.")
        elif user_letter in used_letters:
            print("You have already used that letter. Try again.")
        else:
            print("Invalid character")
    if lives == 0:
        print(f"You died, sorry. The word was {word}")
    else:
        print(f"You gessed the word {word}!!")
hangman()