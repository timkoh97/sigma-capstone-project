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

Things to add:
    1. Display hangman - done
    2. Offer to play again

    3. Collect overall game data (games won, lost etc)
    4. Offer difficulty levels (more lives etc)

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

# # open 5000_words.txt file and save words into list
# with open("5000_words.txt", "r") as file:
#     WORD_LIST = file.read().splitlines()

FILE_NAME = "5000_words.txt"
WORD_LIST = get_word_list(Path.cwd() / FILE_NAME)

def find_word(word_list: list[str], word_length: int = 8) -> str:
    # function to get answer for player to guess
    while True:
        word = random.choice(word_list)
        if len(word) == word_length:
            return word

def get_word_length() -> int:
    print("Choose your word length.")
    # function to retrieve length of answer from player with error handling
    while True:
        word_length = input("\nEnter a whole number between 5 and 14: ")
        print("")
        try:
            word_length = int(word_length)
            if word_length >= 5 and word_length <= 14:
                print("Got it.\n")
                return word_length
            else:
                print("That number's not between 5 and 14. Try again.")
        except ValueError:
            print("That's not a positive integer. Try again.")

def get_guess(previous_guesses: list[str]) -> str:
    # function to get guess of letter from player
    # with error handling for non-alphabetic chars, multiple chars and previously guessed letters
    while True:
        guess = str(input("What's your guess? "))
        if not guess.isalpha():
            print("Guess a letter. Try again.\n")
        elif len(guess) > 1:
            print("Just one letter please. Try again.\n")
        elif guess in previous_guesses:
            print("Already guessed that one. Try another one.\n")
        else:
            return guess.lower()
        
def get_letter_positions(ANSWER: str, guess: str) -> list[int]:
    # function to find position of correctly guessed letters in answer str
    # returns the positions as list of int indices
    letter_positions = []
    start_of_search = 0
    
    while True:
        start_of_search = ANSWER.find(guess,start_of_search)
        if start_of_search == -1:
            return letter_positions
        letter_positions.append(start_of_search)
        start_of_search += 1

def print_player_data(max_lives: int, lives_lost: int, previous_guesses: list[str], correct_letters: list[str], difficulty_offset: int) -> None:
    # prints all player data - lives left, construction of gallows, guessed letters and correct letters so far
    print("\n===== Player data =====\n")

    if max_lives == 10:
        print("Difficulty: easy")
    elif max_lives == 8:
        print("Difficulty: medium")
    elif max_lives == 6:
        print("Difficulty: hard")

    lives_left = max_lives - lives_lost
    if lives_left != 1:
        print(f"\nYou have {lives_left} lives left.")
    else:
        print(f"\nYou have {lives_left} life left.")

    previous_guesses_str = " ".join(previous_guesses)
    print(f"So far you have guessed: {previous_guesses_str}")
    print(HANGMAN_DIAGRAMS[lives_lost + difficulty_offset])

    correct_letters_str = " ".join(correct_letters)
    print(f"\n\n{correct_letters_str}")
    
    print("\n=======================\n")

def get_difficulty() -> int:
    # function to ask for difficulty level - easy (10 lives), medium (8 lives) or hard (6 lives)
    # return max lives
    
    print("Choose your difficulty: easy (10 lives) / medium (8 lives) / hard (6 lives)\n")
    
    while True:
        options = ["e","m","h"]
        guess = str(input("Easy(e), medium(m) or hard(h): "))
        print("")
        if guess not in options:
            print("Invalid. Choose again.\n")
        elif guess == "e":
            print("Understood.")
            return 10
        elif guess == "m":
            print("Understood.")
            return 8
        elif guess == "h":
            print("Understood.")
            return 6
        
HANGMAN_DIAGRAMS = ["""
        
    ***BEWARE***
       gallows
        under
    construction     

             ""","""


        
        
        
        
+===========+""","""

        ||
        ||
        ||
        ||
        ||
+===========+""","""             
  ==+===++
        ||
        ||
        ||
        ||
        ||
+===========+""", """
  ==+===++
    |   ||
        ||
        ||
        ||
        ||
+===========+""", """
  ==+===++
    |   ||
    O   ||
        ||
        ||
        ||
+===========+""", """
  ==+===++
    |   ||
    O   ||
    |   ||
        ||
        ||
+===========+""", """
  ==+===++
    |   ||
    O   ||
   /|   ||
        ||
        ||
+===========+""", """
  ==+===++
    |   ||
    O   ||
   /|\  ||
        ||
        ||
+===========+""", """
  ==+===++
    |   ||
    O   ||
   /|\  ||
   /    ||
        ||
+===========+""", """
  ==+===++
    |   ||
    O   ||
   /|\  ||
   / \  ||
        ||
+===========+"""]

def game() -> None:
    print("""
        
    ================== Welcome to ==================
    _   _    _    _   _  ____ __  __    _    _   _ 
    | | | |  / \  | \ | |/ ___|  \/  |  / \  | \ | |
    | |_| | / _ \ |  \| | |  _| |\/| | / _ \ |  \| |
    |  _  |/ ___ \| |\  | |_| | |  | |/ ___ \| |\  |
    |_| |_/_/   \_\_| \_|\____|_|  |_/_/   \_\_| \_|

    ================================ by Tim Koh ===
        """)

    # ask for answer length and check validity - integer between 5 and 14
    word_length = get_word_length()
    ANSWER = find_word(WORD_LIST, word_length)

    # save the guessed letters as a list of chars
    # strings are immutable and we want to update for the player when they guess correctly
    correct_letters = ["_"]*word_length

    # ask for difficulty level - easy (10 lives), medium (8 lives) or hard (6 lives)
    max_lives = get_difficulty()
    difficulty_offset = 10 - max_lives

    print("Begin.")

    # begin a loop - ending when the word is guessed correctly or the hangman is finished
    lives_lost = 0
    previous_guesses = []

    while True:
        print_player_data(max_lives, lives_lost, previous_guesses, correct_letters, difficulty_offset)

        # get a guess from the player
        guess = get_guess(previous_guesses)

        # update previously guessed letters for player
        previous_guesses.append(guess)

        # check if the player is right or wrong
        if guess in ANSWER:
            print("\n*** That's right. ***")
            # check where the guessed letter is in the answer
            letter_positions = get_letter_positions(ANSWER, guess)

            # update known letters for player
            for index in letter_positions:
                correct_letters[index] = guess
        else:
            print("\n::: Not that one. :::")
            lives_lost += 1

        # check if the player has won
        if "_" not in correct_letters:
            print("\n===== Winner =====")
            print(f"\nThe word was: *** {ANSWER} ***.")
            break
        # check if the player has lost
        elif lives_lost == max_lives:
            print("\n===== Game over =====\n")
            print(HANGMAN_DIAGRAMS[lives_lost + difficulty_offset])
            print("\nYou ran out of lives.\n")
            break

game()