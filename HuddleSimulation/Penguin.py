"""Penguin"""

class Penguin(object):
    """Represents a penguin"""

    def __init__(self, posX, posY, heat=39):
        self.heat = heat
        self.x = posX
        self.y = posY

    def moveCycle(self):
        self.position = (self.position[0]+1, self.position[1]+1)

    def lookAround(self):
        pass
