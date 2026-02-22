"""
Tim Koh's Sigma Capstone Project: Hangman in Python

Basic structure
1. Com chooses a random word from a collection of words?
2. Player guesses letters
3. Player has limited guesses
    - correct + incorrect chosen letters are shown
    - hangman graphic is displayed (growing with incorrect guesses)
4. Player wins / loses and is offered to play again or quit program

Program must be run in the terminal.

Credit to MichaelWehar for the txt file of 5000 common English words (license: public domain)
--> https://github.com/MichaelWehar/Public-Domain-Word-Lists.git

Words of length 2 - 14.

"""

import pathlib
from pathlib import Path
import random
# 1. constants - use caps
# 2. pathlib is your friend


def get_word_list(filepath: pathlib.Path) -> list[str]:
    # function to read word_list from file using pathlib
    with filepath.open("r") as file:
        return file.read().splitlines()

FILE_NAME = "5000_words.txt"
WORD_LIST = get_word_list(Path.cwd() / FILE_NAME)

def find_word(word_list: list[str], word_length: int = 8) -> str:
    # function to get answer for player to guess
    while True:
        word = random.choice(word_list)
        if len(word) == word_length:
            return word

def get_word_length() -> int:
    # function to retrieve length of answer from player with error handling
    while True:
        word_length = input("\nPlease enter a whole number between 5 and 14: ")
        try:
            word_length = int(word_length)
            if word_length >= 5 and word_length <= 14:
                print("Got it.\n")
                return word_length
            else:
                print("That number's not between 5 and 14. Try again.")
        except ValueError:
            print("That's not a positive integer. Try again.")

# # open 5000_words.txt file and save words into list
# with open("5000_words.txt", "r") as file:
#     WORD_LIST = file.read().splitlines()

print("""
    
================== Welcome to ==================
 _   _    _    _   _  ____ __  __    _    _   _ 
| | | |  / \  | \ | |/ ___|  \/  |  / \  | \ | |
| |_| | / _ \ |  \| | |  _| |\/| | / _ \ |  \| |
|  _  |/ ___ \| |\  | |_| | |  | |/ ___ \| |\  |
|_| |_/_/   \_\_| \_|\____|_|  |_/_/   \_\_| \_|

================================ by Tim Koh ===
      """)


# ask for difficulty (answer length) and check validity - integer between 5 and 14
print("How long a word would you like to guess?")

word_length = get_word_length()
ANSWER = find_word(WORD_LIST, word_length)

guessed_letters = "_ "*word_length
guessed_letters = guessed_letters[:-1]  # remove the last space

print(f"This is your word: {guessed_letters}. Let's start!")

# begin a loop - ending when the word is guessed correctly or the hangman is finished
lives = 8
lives_lost = 0
previous_guesses = []

def get_guess(previous_guesses: list[str]) -> str:
    while True:
        guess = str(input("What's your guess? "))
        if not guess.isalpha():
            print("Guess a letter. Try again.")
        elif len(guess) > 1:
            print("Just one letter please. Try again.")
        elif guess in previous_guesses:
            print("Already guessed that one. Try another one.")
        else:
            return guess.lower()

while True:
    print(f"\nYou have {lives - lives_lost} lives left.")

    guess = get_guess(previous_guesses)
    previous_guesses.append(guess)

    if guess in ANSWER:
        print("That's right!")


        
    else:
        print("Not that one.")
        lives_lost += 1
    
    if lives_lost == 8:
        print("===== Game over =====")
        break

"""
Question to consider - how do we build and display a hangman?
"""