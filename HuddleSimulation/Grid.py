import matplotlib.pyplot as plt


class Grid(object):
    """Draw grid of pengun position"""

    h1, = plt.plot([], [])

    def __init__(self):
        # Set interactive mode
        plt.ion()
        self.figure, self.ax = plt.subplots()
        self.lines, = self.ax.plot([], [], 'o')
        self.ax.set_xlim([-5, 105])
        self.ax.set_ylim([-5, 105])
        self.ax.grid()
        pass

    def update(self, penguins):
        x_vals, y_vals = [], []
        for penguin in penguins:
            x_vals.append(penguin.x)
            y_vals.append(penguin.y)

        self.lines.set_xdata(x_vals)
        self.lines.set_ydata(y_vals)
        self.figure.canvas.draw()
        pass
