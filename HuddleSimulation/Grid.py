import matplotlib.pyplot as plt

from Penguin import Penguin


class Grid(object):
    """Draw grid of pengun position"""

    def __init__(self, penguins):
        x_vals, y_vals = [], []
        for penguin in penguins:
            x_vals.append(penguin.x)
            y_vals.append(penguin.y)
            pass

        plt.plot(x_vals, y_vals, 'ro')
        plt.show()
    pass
