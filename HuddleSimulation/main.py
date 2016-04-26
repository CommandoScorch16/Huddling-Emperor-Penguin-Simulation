#!/usr/bin/env python
import time

from Grid import Grid
from Simulate import Simulate


def main():
    """Manages the huddling simulation"""
    sim = Simulate(60)
    grid = Grid()

    # Iterate board
    iterations = 80
    for i in range(0, iterations):
        sim.step()
        sim.stepWithHeat()
        grid.update(sim.penguins)
        # time.sleep(0.1)
        #sim.save("iter_" + str(i))
    time.sleep(3)

if __name__ == "__main__":
    main()
