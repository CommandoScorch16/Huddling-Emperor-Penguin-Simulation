#!/usr/bin/env python


from Penguin import Penguin
from Simulate import Simulate

def main():
    """Manages the huddling simulation"""
    sim = Simulate(10)

    # Iterate board
    iterations = 2
    for i in range(0, iterations):
        sim.step()
    sim.save("iter_"+iterations)


if __name__ == "__main__":
    main()
