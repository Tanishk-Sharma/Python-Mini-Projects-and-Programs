import random
import re

class Hangman:

    def __init__(self):
        self.incorrect_attempts = 0  # Input BEFORE start of new game. Counter Variable for tracking Game Over state
        self.min_word_length = 0  # Input BEFORE start of new game. Selected word criteria

        self.chosen_word = dict() # dictionary of distinct letters and their indexes
        self.revealed_word = list() # initially a list of '*' characters, will change with correct guesses.
        self.previous_guesses = set()  # With each turn - show all previously guessed letter made by player

        self.word_length_MIN = 4   # lower bound for word length in database
        self.word_length_MAX = 11  # upper bound for word length in database

    def start_new_game(self):
        pass

    def set_game_parameters(self):
        pass

    def selecting_word(self):
        pass

    def print_word(self):
        pass

    def get_previous_guesses(self):
        pass

    def check_if_letter_in_selected_word(self, letter):
        pass

    def add_to_previous_guesses(self, letter):
        pass

    def did_i_win(self):
        pass

    def game_over(self):
        pass

