
# Import all libraries
import sys
import tqdm


# Import local libraries
from input import parse_input
from output import save
from solver import solve


if __name__ == "__main__":
    # Read data
    dataset = parse_input(filename=sys.argv[0])

    # Execute algorithm
    result, score = solve()

    # Save data
    save(sys.argv[0], result, score)
