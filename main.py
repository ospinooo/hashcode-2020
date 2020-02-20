
# Import all libraries
import sys
import numpy as np
import random  # seed, shuffle and randint
import itertools
import os
import time
import math

input_file = sys.argv[1]

# Import local libraries
from input import parse_input
from output import save
from solver import solve


if __name__ == "__main__":
    # Read data
    libraries, scores, D = parse_input(filename=input_file)

    # Execute algorithm
    result, score = solve(libraries, scores, D)
    
    print("Score: ", score)
    # Save data
    save(input_file, result, score)
