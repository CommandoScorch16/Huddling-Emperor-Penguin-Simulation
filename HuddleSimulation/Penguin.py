"""Penguin"""


class Penguin(object):
    """Represents a penguin"""

    def __init__(self, posX, posY, heat=39):
        self.heat = heat
        self.x = posX
        self.y = posY

    def moveCycle(self, xMove, yMove):
        self.x = (self.x+xMove)
        self.y = (self.y+yMove)

    def lookAround(self, penguinList):
        """Calculate how much a penguin will move next step"""
        deltaX, deltaY = 0.0, 0.0
        for penguin in penguinList:
            if self.x != penguin.x:
                deltaX += (penguin.x-self.x)

            if self.y != penguin.y:
                deltaY += (penguin.y-self.y)
        if deltaX != 0:
            deltaX = 5 * deltaX/abs(deltaX)
        if deltaY != 0:
            deltaY = 5 * deltaY/abs(deltaY)
        self.moveCycle(deltaX, deltaY)

    def toList(self):
        """Convert penguin to CSV row"""
        return [self.heat, self.x, self.y]
