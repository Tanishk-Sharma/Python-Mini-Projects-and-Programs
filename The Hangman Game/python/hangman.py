import random
from tkinter import *


class Hangman:

    def __init__(self):
        window = Tk()

        window.title("The Hangman Game")
        window.geometry('800x500')

        



        window.mainloop()
        ########################################
        self.word_length_MIN = 4  # lower bound for word length in database
        self.word_length_MAX = 11  # upper bound for word length in database

        self.incorrect_attempts = 0  # Input BEFORE start of new game. Counter Variable for tracking Game Over state
        self.min_word_length = 0  # Input BEFORE start of new game. Selected word criteria

        self.chosen_word = dict()  # dictionary of distinct letters and their indexes
        self.revealed_word = list()  # initially a list of '*' characters, will change with correct guesses.
        self.previous_guesses = set()  # With each turn - show all previously guessed letter made by player

    def start_new_game(self):
        """Starts a new game of hangman and drives it till Game Over"""
        print('Starting a game of Hangman ...\n')
        line_break = '\n#########################################################\n'  # For readability between turns

        proceed = 'N'  # Till player says No to proceed, keep asking for parameters

        # Below 2 parameters: incorrect_attempts, min_word_length set the criteria to select the word

        while proceed in ['N', 'n']:
            self.set_game_parameters()  # Setting the game parameters
            print(line_break)

            print(
                f'You have chosen:\nIncorrect attempts: {self.incorrect_attempts}\nMinimum word length: {self.min_word_length}')

            proceed = input('Would you like to proceed? [Y/N] ')

        print(line_break)

        print('Selecting a word ...')
        self.selecting_word()  # Selecting a word based on parameters entered
        won = False  # Local variable to track progress of player status and display corresponding message accordingly

        # From below: each iteration of the loop is a turn

        while self.game_over() is not True:

            print(line_break)

            self.print_word()  # Show the word

            # Show current status
            print(f'Attempts Remaining: {self.incorrect_attempts}')
            print(f'Previous Guesses: {self.get_previous_guesses()}')

            letter_choice = input('Choose the next letter: ').strip()  # Guessed letter by player
            go_ahead = False  # Boolean variable to check if ok to move to next step of game iff guessed letter is ok
            if len(letter_choice) == 0:
                print('Empty input')
            elif len(letter_choice) > 1:
                print(f'Multiple letters entered. Taking only the first letter: {letter_choice[0]}')
                go_ahead = True
            else:
                go_ahead = True

            if go_ahead:
                self.check_if_letter_in_selected_word(
                    letter_choice[
                        0])  # Check if guessed letter is in the selecting word and marking it revealed if found
                self.add_to_previous_guesses(letter_choice[0])  # Add the guessed letter to the set of previous_guesses
            won = game.did_i_win()
            if won:
                break

        print(line_break)
        if won:
            print(f"-->  {self.word}  <--\nYAYY! YOU WON !!")
        else:
            print(f"Aww! Game over!\nThe word was: {self.word}")
        print(line_break)

    def set_game_parameters(self):
        """Sets the value for incorrect_attempts parameter BEFORE starting a new game"""
        while True:
            try:
                t1 = int(input("How many incorrect attempts do you want? [1-25]: "))
                t2 = int(
                    input(f"What minimum word length do you want? [{self.word_length_MIN}-{self.word_length_MAX}] "))
                if (t1 in range(1, 26)) and (t2 in range(self.word_length_MIN, self.word_length_MAX + 1)):
                    self.incorrect_attempts = t1
                    self.min_word_length = t2
                    break
                else:
                    print('Input is not in the given range. Please try again ...')

            except ValueError:
                print('Invalid Input. Please try again ...')

    def selecting_word(self):
        """Selects a word from the stored list of words in text files in data directory"""
        chosen_word_length = random.randrange(self.min_word_length,
                                              self.word_length_MAX) if self.min_word_length in range(
            self.word_length_MIN,
            self.word_length_MAX) else self.word_length_MAX  # Choosing a random length for selecting word

        text_filename_to_open = '../data/words_length_' + str(chosen_word_length) + '.txt'
        with open(text_filename_to_open, "r") as words_file:
            words_list = tuple(
                words_file.read().split(","))  # Reading words from text file and storing each word as a tuple element
            random_word_position_in_words_list = random.randrange(0, len(
                words_list))  # Choosing the position of word to select inside fetched tuple of words
            self.word = words_list[random_word_position_in_words_list]  # Setting the class variable to the chosen word
        # word is chosen. Now breaking it into dictionary form

        self.chosen_word = dict.fromkeys(set(list(self.word)), 1)
        for letter in self.chosen_word.keys():
            matches = re.finditer(letter, self.word)
            all_indexes = tuple([match.start() for match in matches])
            self.chosen_word[letter] = all_indexes
        self.revealed_word = ['*'] * chosen_word_length

    def print_word(self):
        """Displays the word's letters as per the revealed attribute of letter object"""
        print(''.join(self.revealed_word))

    def get_previous_guesses(self):
        """fetches the previous guesses as a space separated string"""
        guesses = " ".join(self.previous_guesses)
        return guesses

    def check_if_letter_in_selected_word(self, letter):
        """Marks revealed as True if letter found in selected word"""
        found = False
        if letter in self.chosen_word.keys():
            found = True
            indexes = self.chosen_word[letter]
            self.chosen_word.pop(letter, 0)  # removed the letter as it has been guessed now
            for index in indexes:
                self.revealed_word[index] = letter

        if not found and letter not in self.previous_guesses:
            self.incorrect_attempts -= 1

    def add_to_previous_guesses(self, letter):
        """Adds letter to the set of previous guesses"""
        self.previous_guesses.add(letter)

    def did_i_win(self):
        """Determines if game won based on letter revealed or not"""
        if '*' in self.revealed_word:
            return False
        return True

    def game_over(self):
        """Game is over once incorrect_attempts are exhausted"""
        if self.incorrect_attempts == 0:
            return True


while True:
    print('\nBegin new game? [Y/N]: ')
    choice = input()
    if choice in ['y', 'Y']:
        game = Hangman()
        game.start_new_game()
    elif choice in ['n', 'N']:
        break

print('Thanks for playing !!')
