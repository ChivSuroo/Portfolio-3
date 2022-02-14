# The Hangman Game
# Computer will automatically give you a word to guess
# The player will make one guess with
# one letter at a time

# Imports - random selection
import random

# Constants -
# the below will show all the constants
# the new constant will trigger when the
# player answers a letter incorrectly

HANGMAN = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

# These will be the words used when
# it comes to the user guessing.
# These words will be completely random when
# the game begins // only one word will active

WORDS = ["PYTHON", "LETTER", "CODING", "MANSION",
         "TROUBLE", "SNAKE", "CODEINSTITUTE"]

MAX_WRONG = len(HANGMAN) - 1

# Variables Initialize

# Word Selection
# 
word = random.choice(WORDS)

# Dashes to Represent Each Letter in Word
current_guess = "-" * len(word)

# Incorrect Guess Count
# this will count the action of all the incorrect attempts
wrong_guesses = 0

# Used Letters Tracker
used_letters = []

# Main Game Loop
print("Welcome to Python Hangman")
print("Try your best to guess the word")

while wrong_guesses < MAX_WRONG and current_guess != word:
    print(HANGMAN[wrong_guesses])
    print("You have used the following letters: ")
    print("Currently, the word is: ", current_guess)

    guess = input("Enter your letter guess:")
    guess = guess.upper()

    # The letter checker to see if the 'letter' has been inputted already
    while guess in used_letters:
        print("Sorry, you have already guessed that letter", guess)
        guess = input("Enter your guess")
        guess = guess.upper()

    # Adds the newly guessed letters to a list.
    used_letters.append(guess)

    # Checks guess
    if guess in word:
        print("You have guessed the letter correctly!!")

        # Give a new version of the word with mixed letter and dashes

        new_current_guess = ""
        for letter in range(len(word)):
            if guess == word[letter]:
                new_current_guess += guess
            else:
                new_current_guess += current_guess[letter]

        current_guess = new_current_guess
    else:
        print("Your guess was incorrect")
        # Increase the wrong number by 1
        wrong_guesses += 1

# The End Game
# The Notification showing if they've won or not.
if wrong_guesses == MAX_WRONG:
    print(HANGMAN[wrong_guesses])
    print("You have lost the game, BETTER LOOK NEXT TIME!")
    print("The correct word is", word)

else:
    print("You have won, congratulations!!!")
