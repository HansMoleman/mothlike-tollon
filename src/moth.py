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
panel_x = (SCRN_WIDTH / 2) - 112
panel_y = (SCRN_HEIGHT / 2) - 62
test_panel = Panel(window, (224, 124), (panel_x, panel_y))

border_size = 8
btn_width = 100
btn_height = 50

btn1_x = panel_x + border_size
btn1_y = panel_y + border_size
btn1 = Widget(window, (btn_width, btn_height), (btn1_x, btn1_y))
btn1.setColour((255, 0, 0))
btn1.editText("Button 1")

test_panel.addWidget(btn1)

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
    test_panel.draw()
    pyg.display.update()
    clock.tick(FRAME_RATE)


# Quit & cleanup:
pyg.quit()