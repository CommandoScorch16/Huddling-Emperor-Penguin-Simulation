"""Simulate"""
import csv
import random

from Penguin import Penguin


class Simulate(object):
    """Simuulate penguin movement"""

    def __init__(self, penguin_count):
        self.penguins = self.generate_penguins(penguin_count)
        self.output_dir = "../output"
        with open("../output.csv", 'wb') as file:
            wr = csv.writer(file, delimiter=' ', quoting=csv.QUOTE_MINIMAL)
            wr.writerow(['X-value', 'Y-value', 'Temperature'])

    def generate_penguins(self, penguin_count):
        """Generate initial penguins"""
        penguins = []
        for i in range(0, penguin_count):
            x = random.randint(0, 300)
            y = random.randint(0, 300)
            penguins.append(Penguin(x, y, random.uniform(38.0, 40.0)))
        return penguins

    def step(self):
        """Simulate movement for each penguin"""
        for penguin in self.penguins:
            penguin.lookAround(self.penguins)
        self.penguins[0].cycleBasedOffHeat(self.penguins)

    def save(self, file_name):
        """Save the current information as a csv"""
        with open("../output.csv", 'a') as file:
            wr = csv.writer(file, delimiter=' ', quoting=csv.QUOTE_MINIMAL)
            print("Saving iter: "+file_name)
            penguins = [pen.toList() for pen in self.penguins]
            penguins.sort()
            for penguin in penguins:
                wr.writerow(penguin)
