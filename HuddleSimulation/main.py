#!/usr/bin/env python
from Grid import Grid
from Simulate import Simulate


def main():
    """Manages the huddling simulation"""
    sim = Simulate(10)
    Grid(sim.penguins)

    # Iterate board
    iterations = 100
    for i in range(0, iterations):
        sim.step()
        Grid(sim.penguins)
    sim.save("iter_" + str(iterations))
    #sleep(1)


#    Grid(sim.penguins)
if __name__ == "__main__":
    main()
