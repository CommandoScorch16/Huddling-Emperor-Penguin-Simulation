import matplotlib.pyplot as plt


class Grid(object):
    """Draw grid of pengun position"""

    def __init__(self):
        pass

    def draw(self, penguins):
        x_vals, y_vals = [], []
        for penguin in penguins:
            x_vals.append(penguin.x)
            y_vals.append(penguin.y)
            pass

        plt.plot(x_vals, y_vals, 'ro')
        plt.axis([-100, 200, -100, 200])
        plt.show()
