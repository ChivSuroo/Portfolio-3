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

WORDS = ["PYTHON", "MOMENT", "CODING", "MANSION", "TROUBLE", "SKAKE", "CODEINSTITUTE"]

MAX_WORDS = len(HANGMAN) - 1

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
print("Go Try and Guess The Word")