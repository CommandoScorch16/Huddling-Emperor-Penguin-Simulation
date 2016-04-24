"""Penguin"""
import math as Math


class Penguin(object):
    """Represents a penguin"""

    def __init__(self, posX, posY, heat=39):
        self.heat = heat
        self.x = posX
        self.y = posY

    def moveCycle(self, xMove, yMove, penguinsAround):

        self.x = (self.x+xMove)
        self.y = (self.y+yMove)
        penguinTooClose = False
        for penguin in penguinsAround:
            if self.dist(penguin) < 1.5:
                penguinTooClose = True

        if penguinTooClose:
            self.x = self.x-xMove
            self.y = self.y-yMove

    def dist(self, Penguin):
        delta_x = self.x - Penguin.x
        delta_y = self.y - Penguin.y
        return Math.sqrt(delta_x*delta_x + delta_y*delta_y)

    # penguinList is the list of all penguins
    # returns a list of all the penguins within a distance of 2.5
    def penguinsAround(self, penguinList):
        penguinsAround = []
        for penguin in penguinList:
            dist = self.dist(penguin)
            if dist < 2.5 and dist != 0:
                penguinsAround.append(penguin)
        return penguinsAround

    def lookAround(self, penguinList):
        """Calculate how much a penguin will move next step"""
        deltaX, deltaY = 0.0, 0.0
        pengAround = []
        for penguin in penguinList:
            pengAround = self.penguinsAround(penguinList)

            if self.x != penguin.x:
                deltaX += (penguin.x-self.x)

            if self.y != penguin.y:
                deltaY += (penguin.y-self.y)
        if deltaX != 0:
            deltaX = (deltaX/50)/24
        if deltaY != 0:
            deltaY = (deltaY/50)/24
        if len(pengAround) < 5:
            self.moveCycle(deltaX, deltaY, pengAround)

    def toList(self):
        """Convert penguin to CSV row"""
        return [self.heat, self.x, self.y]
