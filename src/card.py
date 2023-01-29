
### Card ##
#
# EXEC: --
# DEPN: --
#
# This file defines a card class for emulating the functionality of a
# playing card.
#
# ---
#  ver-1.00 @ 01-28-23  |  rev-1.00 @ 01-28-23
# ---
##


from guiObjects import Widget


class Card:

    def __init__(self, faceval, suitval, colour):

        # Card attributes
        self._face_value = faceval
        self._suit_value = suitval
        self._colour_val = colour

        # Game object attributes
        self._bgd_colour = (255, 255, 255)
        self._txt_colour = (0, 0, 0) if self._colour_val == "black" else (255, 0, 0)
        self._face_offset = (8, 8)
        self._suit_offset = (4, 50)
        self._widget = None


    ## GETTERS & SETTERS -----#

    def getColour(self):
        return self._colour
    
    def getDimensions(self):
        return self._dimensions

    def getFaceValue(self):
        return self._face_value
    
    def getSuit(self):
        return self._suit_value



    ## HELPER METHODS -----#

    def makeWidget(self, window, dimensions, position):
        self._widget = Widget(window, dimensions, position)
        self._widget.setColour(self._bgd_colour)
        self._widget.setTextColour(self._txt_colour)

        self._widget.addText(((position[0] + self._face_offset[0]), (position[1] + self._face_offset[1])), self._face_value)
        self._widget.addText(((position[0] + self._suit_offset[0]), (position[1] + self._suit_offset[1])), self._suit_value)

        return self._widget