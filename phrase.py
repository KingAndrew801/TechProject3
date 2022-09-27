# Create your Phrase class logic here.
# The class should also have these methods:
#
# check_letter(): checks to see if the letter selected by the user matches a letter in the phrase.
# check_complete(): checks to see if the whole phrase has been guessed.
import game

class Phrase:
    def __init__(self):
        self.phrase = None

    def display(self):
        display = []
        for charachter in game.active_phrase:
            if str.isalpha(charachter):
                display.append('_')
            else: display.append(' ')
        dex = -1
        for charachter in display:
            dex += 1
            for guess in game.guesses:
                if guess == game.active_phrase[dex]:
                    display[dex] = guess
        return ''.join(display)

    def check_letter(self):
        correct = None
        current = self.display()
        game.get_guess()
        new = self.display()
        if current == new:
            correct = False
        else: correct = True
        return correct

    def complete(self):
        complete = False
        for char in self.display():
            if char == '_':
                complete = False
                break
            else:
                complete = True
        return complete



if __name__ == '__main__':
    game = game.Game()
    phrase = Phrase()
    game.get_random_phrase()
    phrase.display()

