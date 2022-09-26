# Create your Phrase class logic here.
# phrase: this is the actual phrase the Phrase object is representing. This attribute
# should be set to the phrase parameter but converted to all lower case.
# The class should also have these methods:
#
# display(): this prints out the phrase to the console with guessed letters visibile and
# unguessed letters as underscores. For example, if the current phrase is "hello world"
# and the user has guessed the letter "o", the output should look like this: _ _ _ _ o    _ o _ _ _
# check_letter(): checks to see if the letter selected by the user matches a letter in the phrase.
# check_complete(): checks to see if the whole phrase has been guessed.
import game

class Phrase:

    def __init__(self):
        self.phrase = None

    def display(self):
        display = []
        for letter in game.active_phrase:
            for correct


if __name__ == '__main__':
    game = game.Game()
    phrase = Phrase()
    game.get_random_phrase()
    phrase.display()

