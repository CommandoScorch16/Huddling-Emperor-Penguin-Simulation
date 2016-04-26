"""Penguin"""
import math as Math
import random


class Penguin(object):
    """Represents a penguin"""

    def __init__(self, posX, posY, heat):
        self.heat = heat
        self.x = posX
        self.y = posY

    def moveCycle(self, xMove, yMove, penguinsAround):
        """Move a penguin if no one else is around"""
        self.x = (self.x+xMove)
        self.y = (self.y+yMove)
        penguinTooClose = False
        for penguin in penguinsAround:
            if self.dist(penguin) < 3:
                penguinTooClose = True

        if penguinTooClose:
            self.x = self.x-xMove
            self.y = self.y-yMove

    def dist(self, Penguin):
        delta_x = self.x - Penguin.x
        delta_y = self.y - Penguin.y
        return Math.sqrt(delta_x*delta_x + delta_y*delta_y)

    def penguinsAround(self, distance, penguinList):
        """Find penguins within a given distance of each other"""
        penguinsAround = []
        for penguin in penguinList:
            dist = self.dist(penguin)
            if dist < distance and dist != 0:
                penguinsAround.append(penguin)
        return penguinsAround

    def lookAround(self, penguinList):
        """Calculate how much a penguin will move next step"""
        deltaX, deltaY = 0.0, 0.0
        pengAround = []

        for penguin in penguinList:
            pengAround = self.penguinsAround(2, penguinList)
            deltaX += (penguin.x-self.x)

            deltaY += (penguin.y-self.y)
        # Normalize distance
        deltaX = (deltaX/len(penguinList))
        deltaY = (deltaY/len(penguinList))
        # Scale movment to match maximum radius
        max_radius = 2.0
        scale = max_radius / Math.sqrt(deltaX*deltaX + deltaY*deltaY)
        deltaX *= scale
        deltaY *= scale
        # Add randomization
        rnd_range = 2
        deltaX += (rnd_range - (random.random() * 2 * rnd_range))
        deltaY += (rnd_range - (random.random() * 2 * rnd_range))
        if len(pengAround) < 10:
            self.moveCycle(deltaX, deltaY, pengAround)

    def cycleBasedOffHeat(self, penguinList):
        allPenguins = {}

        heatChange = 0.0
        for penguin in penguinList:
            pengAround = penguin.penguinsAround(5, penguinList)
            allPenguins[penguin] = pengAround
            if len(pengAround) > 8:
                for peng in pengAround:
                    heatChange += peng.heat
                heatChange = heatChange/len(pengAround)
                diff = abs(39.0-heatChange)
                if diff > .3:
                    diff = .3
                penguin.heat += diff
            heatChange = 0.0

            if len(pengAround) < 2:
                penguin.heat -= .05

    def toList(self):
        """Convert penguin to CSV row"""
        return [self.heat, self.x, self.y]
