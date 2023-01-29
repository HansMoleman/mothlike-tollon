
### Deck ##
#
# EXEC: --
# DEPN: --
#
# This file defines the deck class, which provides functionality for
# storing, shuffling, and drawing cards.
#
# ---
#  ver-1.00 @ 01-28-23  |  rev-1.00 @ 01-28-23
# ---
##


from card import Card
from guiObjects import Widget
import random



class Deck:

    def __init__(self):
        self._deck = []
        self._size = 0

        # Widget attributes
        self._bgd_colour = (0, 0, 255)
        self._txt_colour = (255, 255, 255)
        self._label = "Deck"
        self._lbl_offset = (20, 40)
        self._widget = None

        # For testing
        self._deck.append(Card("10", "Clubs", "black"))
        self._deck.append(Card("King", "Diamonds", "red"))
        self._size += 2


    ## GETTERS & SETTERS -----#

    def getWidget(self):
        return self._widget



    ## HELPER METHODS -----#

    def build(self):
        pass

    def drawTop(self):
        self._size -= 1
        return self._deck.pop()

    def makeWidget(self, window, dimensions, position):
        self._widget = Widget(window, dimensions, position)
        self._widget.setColour(self._bgd_colour)
        self._widget.setTextColour(self._txt_colour)

        self._widget.addText(((position[0] + self._lbl_offset[0]), (position[1] + self._lbl_offset[1])), self._label)
        return self._widget


    def shuffle(self):
        pass
