# Create your Game class logic in here.
# Create the Game class in the game.py file
# The class should include an initializer or def __init__ method that sets the following attributes:
#
# missed: used to track the number of incorrect guesses by the user. The initial value is 0 since no
# guesses have been made at the start of the game.
# phrases: a list of five Phrase objects to use with the game. A phrase should only include letters
# and spaces -- no numbers, puntuation or other special characters.
# active_phrase: This is the Phrase object that's currently in play. The initial value will be None.
# Within the start() method, this property will be set to the Phrase object returned from a call to the
# get_random_phrase() method.
# guesses: This is a list that contains the letters guessed by the user.
# The class should also have these methods:
#
# start(): Calls the welcome method, creates the game loop, calls the get_guess method, adds the
# user's guess to guesses, increments the number of missed by one if the guess is incorrect, calls
# the game_over method.
# get_random_phrase(): this method randomly retrieves one of the phrases stored in the phrases list
# and returns it.
# welcome(): this method prints a friendly welcome message to the user at the start of the game
# get_guess(): this method gets the guess from a user and records it in the guesses attribute
# game_over(): this method displays a friendly win or loss message and ends the game.
# The Game instance might be responsible for things like: starting the game loop, getting player's
# input() guesses to pass to a Phrase object to perform its responsibilities against, determining
# if a win/loss happens after the player runs out of turns or the phrase is completely guessed.
import random
import string

class Game:

    def __init__(self):
        self.missed = 0
        self.phrases = ['make hay while the sun shines', 'easy does it', 'keep it simple stupid',
                   'another day another dollar', 'the strong survive and the weak are consumed']
        self.active_phrase: None
        self.guesses = []

    def welcome(self):
        print('''Welcome to Phrase Hunters!
Guess letters to complete the hidden phrase!''')

    def get_random_phrase(self):
        self.active_phrase = random.choice(self.phrases)

    def get_guess(self):
        guessing = True
        while guessing:
            try:
                current_guess = input("Enter your next guess here:   ")
                if current_guess.isalpha():
                    self.guesses.append(current_guess)
                    guessing = False
                else:
                    raise ValueError('You can only guess letters A-Z. Try again.')
            except ValueError as err:
                print(f'{err}')
        return current_guess

if __name__ == '__main__':
    game = Game()
    game.get_random_phrase()
    game.get_guess()

