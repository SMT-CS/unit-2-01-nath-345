#!/usr/bin/env python3
"""
Created by: Nathan
Created on: Feb 25
This program calculates the circumference of a circle 
    with a diameter of 42 mm.
"""

import math

DIAMETER = 42
CIRCUMFERENCE = math.pi * DIAMETER


def main() -> None:
    """
    The main function calculates the diameter of a 42 mm circle,
        returns None.
    """
    print("if a circle has a diameter of 42 mm:")
    print("")
    print(f"circumference is {(math.pi * DIAMETER)} mm")

    print("\nDone")


if __name__ == "__main__":
    main()
