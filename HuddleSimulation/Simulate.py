"""Simulate"""
import random

from Penguin import Penguin


class Simulate(object):
    """Simuulate penguin movement"""

    def __init__(self, penguin_count):
        self.penguins = self.generate_penguins(penguin_count)
        self.output_dir = "../output"
        pass

    def generate_penguins(self, penguin_count):
        """Generate initial penguins"""
        penguins = []
        for i in range(0, penguin_count):
            x, y = random.randint(0, 100), random.randint(0, 100)
            penguins.append(Penguin(x, y))
        return penguins

    def step(self):
        """Simulate a turn for the coldest penguin"""
        pass

    def save(self, file_name):
        """Save the current information as a csv"""
        for i in range(0, len(self.penguins)):
            pass
        pass
