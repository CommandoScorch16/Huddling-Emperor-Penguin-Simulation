"""Simulate"""
import csv
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
            penguins.append(Penguin(x, y, random.randint(0, 10)))
        return penguins

    def step(self):
        """Simulate a turn for the coldest penguin"""
        for penguin in self.penguins:
            penguin.lookAround(self.penguins)
        pass

    def save(self, file_name):
        """Save the current information as a csv"""
        with open(self.output_dir+'/'+file_name, 'wb') as file:
            wr = csv.writer(file, delimiter=' ', quoting=csv.QUOTE_MINIMAL)
            wr.writerow(['Temperature', 'X-value', 'Y-value'])
            penguins = [pen.toList() for pen in self.penguins]
            penguins.sort()
            for penguin in penguins:
                wr.writerow(penguin)
        pass
    
    
