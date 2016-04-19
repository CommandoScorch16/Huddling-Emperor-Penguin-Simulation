"""Simulate"""
from Penguin import Penguin

class Simulate(object):
    """Simualte penguin movement"""

    def __init__(self, penguin_count):
        self.penguins = []
        self.generate_penguins(penguin_count)
        pass

    def generate_penguins(self, penguin_count):
        """Generate initial penguins"""
        for i in range(0, penguin_count):
            self.penguins[i] = Penguin(0, 0)

    def step(self):
        """Simulate a turn for the coldest penguin"""
        pass

    def save(self, file_name):
        """Save the current information as a csv"""
        for i in range(0, len(self.penguins)):
            pass
        pass



