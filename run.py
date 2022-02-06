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

HANGMANPICS = ['''
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
# 

WORDS = ["PYTHON", "MOMENT", "CODING", "MANSION", "TROUBLE", "SKAKE", "CODEINSTITUTE"]