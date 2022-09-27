# Create the Phrase class in the phrase.py file
# The class should include an initializer or def __init__ that receives a phrase parameter and
# holds this phrase in an instance attribute on the Phrase object.
#
# phrase: this is the actual phrase the Phrase object is representing. This attribute should be
# set to the phrase parameter but converted to all lower case.
# The class should also have these methods:
#
# display(): this prints out the phrase to the console with guessed letters visibile and unguessed
# letters as underscores. For example, if the current phrase is "hello world" and the user has
# guessed the letter "o", the output should look like this: _ _ _ _ o    _ o _ _ _
# check_letter(): checks to see if the letter selected by the user matches a letter in the phrase.
# check_complete(): checks to see if the whole phrase has been guessed.
import game

class Phrase:
    def __init__(self, phrase):
        self.phrase = phrase

    def display(self):
        display = []
        for charachter in self.phrase:
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

