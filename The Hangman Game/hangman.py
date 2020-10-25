import requests
import html2text
from bs4 import BeautifulSoup
import random
import math


class Hangman:

    def __init__(self):
        self.incorrect_attempts = 0  # Input BEFORE start of new game. Counter Variable for tracking Game Over state
        self.chosen_word = ''  # dictionary of distinct letters and their indexes
        self.won = False  # initially a list of '*' characters, will change with correct guesses.
        self.previous_guesses = set()  # With each turn - show all previously guessed letter made by player
        self.hangman_pics = [r'''
                  +
                  |
                  |
                  |
                  |
                  |
            =========''', r'''
               ---+
                  |
                  |
                  |
                  |
                  |
            =========''', r'''
              +---+
                  |
                  |
                  |
                  |
                  |
            =========''', r'''
              +---+
              |   |
                  |
                  |
                  |
                  |
            =========''', r'''
              +---+
              |   |
              O   |
                  |
                  |
                  |
            =========''', r'''
              +---+
              |   |
              O   |
              |   |
                  |
                  |
            =========''', r'''
              +---+
              |   |
              O   |
             /|   |
                  |
                  |
            =========''', r'''
              +---+
              |   |
              O   |
             /|\  |
                  |
                  |
            =========''', r'''
              +---+
              |   |
              O   |
             /|\  |
             /    |
                  |
            =========''', r'''
              +---+
              |   |
              O   |
             /|\  |
             / \  |
                  |
            =========''']
        self.hangman_pics_jumper = 0

    def start_new_game(self):
        """Starts a new game of hangman and drives it till Game Over"""
        print('Starting a game of Hangman ...\n')
        line_break = '\n#########################################################\n'  # For readability between turns

        proceed = 'N'  # Till player says No to proceed, keep asking for parameters

        # Below 2 parameters: incorrect_attempts, min_word_length set the criteria to select the word

        while proceed in ['N', 'n']:
            self.set_game_parameters()  # Setting the game parameters
            print(line_break)

            print(f'You have chosen:\nIncorrect attempts: {self.incorrect_attempts}')

            proceed = input('Would you like to proceed? [Y/N] ')

        print(line_break)

        print('Selecting a word ...')
        self.get_random_word()  # Selecting a word based on parameters entered
        # From below: each iteration of the loop is a turn
        ###############################################################################################################
        while not self.won:
            print(line_break)

            self.print_word()
            if self.won:
                break
            # Show current status
            print(f'Attempts Remaining: {self.incorrect_attempts}')
            print(f'Previous Guesses: {self.get_previous_guesses()}')
            # Show hangman status
            print(self.hangman_pics[self.hangman_pics_jumper])
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
                # Check if guessed letter is in the selecting word and marking it revealed if found
                self.check_if_letter_in_selected_word(letter_choice[0])
            if self.incorrect_attempts == 0:
                break
        print(line_break)

        if self.won:
            print(f"-->  {''.join(self.chosen_word)}  <--\nYAYY! YOU WON !!")
        else:
            print(f"Aww! Game over!\nThe word was: **{''.join(self.chosen_word)}**")
            print(self.hangman_pics[-1])
        print(line_break)

    def set_game_parameters(self):
        """Sets the value for incorrect_attempts parameter BEFORE starting a new game"""
        while True:
            try:
                t1 = int(input("How many incorrect attempts do you want? [1-25]: "))
                if t1 in range(1, 26):
                    self.incorrect_attempts = t1
                    break
                else:
                    print('Input is not in the given range. Please try again ...')

            except ValueError:
                print('Invalid Input. Please try again ...')

    def get_random_word(self):
        alphabets = [chr(i) for i in range(97, 123)]
        url = 'https://learnersdictionary.com/3000-words/alpha/'
        alpha = random.choice(alphabets)
        url += alpha
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        words = soup.findAll('ul', class_="a_words")
        h = html2text.HTML2Text()
        h.ignore_links = True
        h.ignore_images = True
        list_words = h.handle(str(words[0])).split('\n')
        list_words = [x.replace('* ', '').strip() for x in list_words]
        list_words = [x[:x.find(' ')] for x in list_words if '(' in x]
        self.chosen_word = list(random.choice(list_words))

    def print_word(self):
        """Displays the word's letters as per the revealed attribute of letter object"""
        print('\t\t', end='')
        count = 0
        for letter in self.chosen_word:
            if letter in self.previous_guesses:
                print(letter, end='')
                count += 1
            else:
                self.won = False
                print('*', end='')
        print()
        if count == len(self.chosen_word):
            self.won = True

    def get_previous_guesses(self):
        """fetches the previous guesses as a space separated string"""
        guesses = " ".join(self.previous_guesses)
        return guesses

    def check_if_letter_in_selected_word(self, letter):
        """Marks revealed as True if letter found in selected word"""
        # check if letter already guessed. if yes, then do nothing
        if letter in self.previous_guesses:
            return
        # if not guessed earlier, check if letter is in chosen word
        if letter in self.chosen_word:
            # if yes, then put it into previous guesses, it will be revealed with checks
            self.previous_guesses.add(letter)
            return
        # if not, add to previous guesses and reduce incorrect attempts
        # Using Newton's equations of motion to determine rate of change of jumper
        self.previous_guesses.add(letter)
        
        acc = 2 * ((len(self.hangman_pics) - self.hangman_pics_jumper) / self.incorrect_attempts ** 2)
        v = math.sqrt(self.hangman_pics_jumper ** 2 + (2 * acc * len(self.hangman_pics)))
        self.hangman_pics_jumper = round(v)

        if self.hangman_pics_jumper >= len(self.hangman_pics) - 2:
            self.hangman_pics_jumper = len(self.hangman_pics) - 2
        self.incorrect_attempts -= 1


while True:
    print('\nBegin new game? [Y/N]: ')
    choice = input()
    if choice in ['y', 'Y']:
        game = Hangman()
        game.start_new_game()
    elif choice in ['n', 'N']:
        break

print('Thanks for playing !!')
