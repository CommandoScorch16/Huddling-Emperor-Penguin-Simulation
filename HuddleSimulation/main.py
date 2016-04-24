#!/usr/bin/env python
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
        grid.draw(sim.penguins)
    sim.save("iter_" + str(iterations))


if __name__ == "__main__":
    main()
