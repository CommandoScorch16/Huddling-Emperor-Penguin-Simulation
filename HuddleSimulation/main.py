#!/usr/bin/env python
import time

from Grid import Grid
from Simulate import Simulate


def main():
    """Manages the huddling simulation"""
    sim = Simulate(20)
    grid = Grid()

    # Iterate board
    iterations = 20
    for i in range(0, iterations):
        sim.step()
        grid.update(sim.penguins)
        time.sleep(0.5)
        sim.save("iter_" + str(i))

if __name__ == "__main__":
    main()
