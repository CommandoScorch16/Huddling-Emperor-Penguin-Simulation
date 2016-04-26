import math as Math
import sys

import matplotlib.pyplot as plt


class Grid(object):
    """Draw grid of pengun position"""
    h1, = plt.plot([], [])

    def __init__(self):
        # Set interactive mode
        plt.ion()
        self.figure, self.ax = plt.subplots()
        self.lines, = self.ax.plot([], [], 'o')
        pass

    def update(self, penguins):
        x_vals, y_vals = [], []
        for penguin in penguins:
            x_vals.append(penguin.x)
            y_vals.append(penguin.y)

        window = 100.0
        self.lines.set_xdata(x_vals)
        max_x, min_x = max(x_vals), min(x_vals)
        self.ax.set_xlim([Math.floor(min_x / window) * window,
                         Math.ceil(max_x / window) * window])

        self.lines.set_ydata(y_vals)
        max_y, min_y = max(y_vals), min(y_vals)
        self.ax.set_ylim([Math.floor(min_y / window) * window,
                         Math.ceil(max_y / window) * window])
        self.figure.canvas.draw()

    def max(self, data):
        max_val = 0
        for value in data:
            if value > max_val:
                max_val = value
        return max_val

    def min(self, data):
        max_val = sys.maxint
        for value in data:
            if value < max_val:
                max_val = value
        return max_val
