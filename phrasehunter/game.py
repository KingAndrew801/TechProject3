
import random
from phrasehunter.phrase import Phrase

class Game:
    def __init__(self):
        self.missed = 0
        self.phrases = []
        self.active_phrase = None
        self.guesses = []

    def welcome(self):
        print('''Welcome to Phrase Hunters!
Guess letters to complete the hidden phrase!''')

    def get_random_phrase(self):
        phraselist = ['make hay while the sun shines', 'easy does it', 'keep it simple stupid',
                   'another day another dollar', 'the strong survive and the weak are consumed']
        for phrase in phraselist:
            self.phrases.append(Phrase(phrase))
        self.active_phrase = random.choice(self.phrases)

    def get_guess(self):
        guessing = True
        print(self.active_phrase.display(self.guesses))
        while guessing:
            try:
                current_guess = input("Enter your next guess here:   ")
                if current_guess.isalpha() and len(current_guess) == 1:
                    self.guesses.append(current_guess)
                    if self.active_phrase.check_letter(current_guess):
                        print('That is correct! \n')
                    else:
                        self.missed += 1
                        print (f"That letter is not in the phrase. You've missed {self.missed} times!\n")
                    guessing = False
                else:
                    raise ValueError('You can only guess single letters A-Z. Try again. \n')
            except ValueError as err:
                print(f'{err}')
        return current_guess

    def game_over(self):
        if self.missed >= 5:
            print("You LOSE, sir. Good DAY!")
            return True
        else:
            return False

    def start(self):
        playing = True
        while playing == True:
            self.get_random_phrase()
            self.welcome()
            while self.active_phrase.complete(self.guesses) == False and self.game_over() == False:
                self.get_guess()
            trying = True
            while trying:
                try:
                    again = input("Do you want to play again? Select Y/N   ").lower()
                    print('--------------------------------\n')
                    if again == 'y' or 'n':
                        if again == 'y':
                            self.guesses = []
                            self.missed = 0
                            self.get_random_phrase()
                            trying = False
                        if again =='n':
                            print('Alright then, thanks for playing!')
                            playing = False
                            trying = False
                    else:
                        raise ValueError('You have to select Y or N\n')
                except ValueError as err:
                    print('{err}')



if __name__ == '__main__':
    game = Game()
    game.start()

