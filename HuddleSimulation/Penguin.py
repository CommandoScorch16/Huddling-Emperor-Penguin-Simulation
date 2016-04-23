"""Penguin"""

class Penguin(object):
    """Represents a penguin"""

    def __init__(self, posX, posY, heat=39):
        self.heat = heat
        self.x = posX
        self.y = posY

    def moveCycle(self,xMove,yMove):
        self.x = (self.x+xMove)
        self.y = (self.y+yMove)

    def lookAround(self,penguinList):
        distances = []
        xMove = 0.0
        yMove = 0.0
        for penguin in penguinList:
            if self.x != penguin.x:
                xMove = xMove + 1.0/(penguin.x-self.x)

            if self.y != penguin.y:
                yMove = yMove + 1.0/(penguin.y-self.y)
        if xMove != 0:
            xMove = 5* xMove/abs(xMove) 
        if yMove != 0:
            yMove = 5* yMove/abs(yMove)
        print xMove
        print yMove
        self.moveCycle(xMove,yMove)
