
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

import copy
if __name__ == "__main__":
    # Read data
    libraries, scores, D = parse_input(filename=input_file)

    # Execute algorithm
    max_score = 0
    max_result = None
    for x in range(0,100):
        result, score = solve(copy.deepcopy(libraries), scores, D)
        if max_score < score:
            max_score = score
            max_result = result
    
    print("Score: ", max_score)
    # Save data
    save(input_file, max_result, max_score)
