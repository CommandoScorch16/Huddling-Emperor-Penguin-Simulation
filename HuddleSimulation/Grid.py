import math as Math
import sys

import matplotlib.cm as cm
import matplotlib.colors as col
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
        x_vals, y_vals, colors = [], [], []
        for penguin in penguins:
            x_vals.append(penguin.x)
            y_vals.append(penguin.y)
            colors.append(penguin.heat)

        # Set color map
        cmap = cm.coolwarm
        norm = col.Normalize(self.min(colors), self.max(colors))
        self.ax.cla()
        self.ax.scatter(x_vals, y_vals, c=colors, cmap=cmap, norm=norm)

        # Set plto range
        window = 25.0
        max_x, min_x = max(x_vals), min(x_vals)
        self.ax.set_xlim([Math.floor(min_x / window) * window,
                         Math.ceil(max_x / window) * window])

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
