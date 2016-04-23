#!/usr/bin/env python
from Grid import Grid
from Simulate import Simulate


def main():
    """Manages the huddling simulation"""
    sim = Simulate(10)
    Grid(sim.penguins)

    # Iterate board
    iterations = 2
    for i in range(0, iterations):
        sim.step()
    sim.save("iter_" + str(iterations))


if __name__ == "__main__":
    main()
