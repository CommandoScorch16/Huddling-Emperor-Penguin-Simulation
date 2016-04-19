import random

class Penguin(object):
"""Represents a penguin"""

    def __init__(self, posX, posY, heat):
        self.heat = heat
        self.position = (posX,posY)
       
    def moveCycle(self):
        self.position = (self.position[0]+1,self.position[1]+1)

    def lookAround(self):
        pass
    
penguin = Penguin(0,0,55)
penguin.moveCycle()

print penguin.position
