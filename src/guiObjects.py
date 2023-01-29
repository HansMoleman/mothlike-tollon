
### GUI Objects ##
#
# EXEC: --
# DEPN: --
#
# This file defines two classes, widget and panel, which are used
# to draw game objects to the screen and allow user to interact
# with them.
#
# ---
#  ver-1.00 @ 01-28-23  |  rev-1.00 @ 01-28-23
# ---
##


from pygame.math import Vector2 as V2D
import pygame as pyg



### Widget(tuple: dimensions, tuple: position) ##
#
##
class Widget:

    def __init__(self, window, dimensions, position):

        ## Core attributes
        self._colour = (0, 0, 0)
        self._dimensions = V2D(dimensions[0], dimensions[1])
        self._position = V2D(position[0], position[1])
        self._rect = pyg.Rect(self._position.x, self._position.y,
                            self._dimensions.x, self._dimensions.y
                        )
        self._root_win = window
        self._surface = pyg.Surface((self._dimensions.x, self._dimensions.y))
        self._surface.fill(self._colour)

        ## Extra attributes

        # Font
        self._font_colour = (255, 255, 255)
        self._font_name = "ubuntumono"
        self._font_size = 14
        self._font = pyg.font.SysFont(self._font_name, self._font_size)

        # Text
        self._text = ""
        self._text_surf = None
        self._text_rect = None
        self.editText(self._text)


    ## GETTERS & SETTERS -----#

    def getColour(self):
        return self._colour

    def getDimensions(self):
        return (self._dimensions.x, self._dimensions.y)

    def getPosition(self):
        return (self._position.x, self._position.y)

    def getRect(self):
        return (self._rect)

    def getText(self):
        return self._text


    def setColour(self, newcolour):
        self._colour = newcolour
        self._surface.fill(self._colour)


    ## HELPERS METHODS -----#

    def draw(self):
        self._root_win.blit(self._surface, self._rect)
        self._root_win.blit(self._text_surf, self._text_rect)


    def editText(self, newtext):
        self._text = newtext
        self._text_surf = self._font.render(self._text, True, self._font_colour)
        self._text_rect = self._text_surf.get_rect()

        text_x = self._position.x + (self._dimensions.x / 2)
        text_y = self._position.y + (self._dimensions.y / 2)
        self._text_rect.center = (text_x, text_y)


    def isWithinRect(self, apoint):
        return self._rect.collidepoint(apoint)


    def move(self, newpos):
        pass


    def resize(self, newdims):
        pass




### Panel(Surface:window, tuple:dimensions, tuple:position) ##
#
##
class Panel:

    def __init__(self, window, dimensions, position):

        ## Core attributes
        self._colour = (0, 0, 0)
        self._contents = []
        self._dimensions = V2D(dimensions[0], dimensions[1])
        self._position = V2D(position[0], position[1])
        self._rect = pyg.Rect(self._position.x, self._position.y,
                            self._dimensions.x, self._dimensions.y
                        )
        self._root_win = window
        self._root_win = window
        self._surface = pyg.Surface((self._dimensions.x, self._dimensions.y))
        self._surface.fill(self._colour)


    ## GETTERS & SETTERS -----#

    def getColour(self):
        return self._colour

    def getContents(self):
        return self._contents

    def getDimensions(self):
        return(self._dimensions.x, self._dimensions.y)

    def getPosition(self):
        return(self._position.x, self._position.y)

    def setColour(self, newcolour):
        self._colour = newcolour
        self._surface.fill(self._colour)


    ## HELPER METHODS -----#

    def addWidget(self, awidget):
        self._contents.append(awidget)

    def draw(self):
        self._root_win.blit(self._surface, self._rect)

        for widg in self._contents:
            widg.draw()

    def isWithinRect(self, apoint):
        return self._rect.collidepoint(apoint)
