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

WORDS = ["PYTHON", "MOMENT", "CODING", "MANSION",
         "TROUBLE", "SKAKE", "CODEINSTITUTE"]

max_WRONG = len(HANGMAN) - 1

# Initialize Variables

# Pick a word
word = random.choice(WORDS)

# Dashes for letters in the word
current_guess = "-" * len(word)

# Incorrect Guess Count
# this will count the action of all the incorrect attempts
wrong_guesses = 0

# Used Letter
used_letters = []

# MLoop
print("Welcome To Hangman")
print("Go Try and Guess The Word to Win")

while wrong_guesses < max_WRONG and current_guess != word:
    print(HANGMAN[wrong_guesses])
    print("You have used the following letters: ", used_letters)
    print("Currently, the word is", current_guess)

    guess = input("Enter your guess:")
    guess = guess.upper()

    # Letter Check (This will check the letters that the user has inputted already)
    while guess in used_letters:
      print("Sorry, you have already inputted this letter. Please choose another letter.", guess)
      guess = input("Enter your guess")
      guess = guess.upper()

# Adds new guessed letters to a new list of guessed letters
used_letters.append(guess)