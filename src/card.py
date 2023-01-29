
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



class Card:

    def __init__(self, faceval, suitval, colour):
        self._face_value = faceval
        self._suit_value = suitval
        self._colour = colour


    ## GETTERS & SETTERS -----#



    ## HELPER METHODS -----#