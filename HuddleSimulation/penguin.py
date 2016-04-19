import random


class Penguin(object):

    def __init__(self, posX, posY, heat):
        self.heat = heat
        self.position = (posX,posY)
       
    def moveCycle(self):
        self.position = (self.position[0]+1,self.position[1]+1)

    def lookAround(self):
    
pengiunone = Penguin(0,0,55)
pengiunone.moveCycle()

print pengiunone.position
