#!/usr/bin/python3

### Moth ##
#
# EXEC: ./moth.py
# DEPN: panel.py, widget.py
#
# This file is the main file of the system ...
#
#
# ---
#  Stble:   ver-1.00 @ 01-28-23
#  Revsn:   ver-1.00 @ 01-28-23
# ---
##

from card import Card
from guiObjects import Widget, Panel
import pygame as pyg



# GAME CONSTS -----#
BGD_COLOUR = (96, 96, 96)
FRAME_RATE = 32
SCRN_WIDTH = 600
SCRN_HEIGHT = 500
WIN_TITLE = "Mothlike Tollon (ver-1.00)"



# GAME METHODS -----#



# MAIN CODE -----#

# Initialize PyGame:
pyg.init()
window = pyg.display.set_mode((SCRN_WIDTH, SCRN_HEIGHT))
clock = pyg.time.Clock()

# Initialize game:
test_card = Card("7", "Clubs", "black")
card_size = test_card.getDimensions()
pos_x = (SCRN_WIDTH / 2) - (card_size[0] / 2)
pos_y = (SCRN_HEIGHT / 2) - (card_size[1] / 2)
test_card_widget = test_card.makeWidget(window, (pos_x, pos_y))


# Game Loop:
run = True

while run:
    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            run = False

        if event.type == pyg.MOUSEBUTTONUP:
            pass

    # Do game updates:
    window.fill(BGD_COLOUR)
    test_card_widget.draw()
    pyg.display.update()
    clock.tick(FRAME_RATE)


# Quit & cleanup:
pyg.quit()