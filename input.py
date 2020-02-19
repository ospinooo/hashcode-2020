
def parse_input(filename):
    """Takes the whole dataset and outputs the list with all the data

    Arguments:
        filename {FILE} -- Filename
    """
    with open(filename, 'r') as f:
        lines = f.readlines()

    dataset = []
    for line in lines:
        # Strip -> Get rid of 0s
        # Split -> split with the space into a list
        line

    return dataset
