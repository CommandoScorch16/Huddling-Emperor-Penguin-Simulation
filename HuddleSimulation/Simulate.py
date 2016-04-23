"""Simulate"""
import random
from Penguin import Penguin


class Simulate(object):
    """Simuulate penguin movement"""

    def __init__(self, penguin_count):
        self.penguins = []
        self.generate_penguins(penguin_count)
        self.output_dir = "../output"
        pass

    def generate_penguins(self, penguin_count):
        """Generate initial penguins"""
        for i in range(0, penguin_count):
            x, y = random.randint(0, 100), random.randint(0, 100)
            self.penguins.append(Penguin(x, y))

    def step(self):
        """Simulate a turn for the coldest penguin"""
        for penguin in self.penguins:
            penguin.lookAround(self.penguins)
        pass

    def save(self, file_name):
        """Save the current information as a csv"""
        for i in range(0, len(self.penguins)):
            pass
        pass
    
    
