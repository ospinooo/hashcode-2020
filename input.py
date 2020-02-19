
def parse_input(filename):
    """Creates the dataset from the filename data

    Arguments:
        filename {FILE} -- Filename
    """
    with open(filename, 'r') as f:
        lines = f.readlines()

    value = lines[0]
    value2 = lines[1]

    dataset = []
    for line in lines[2:]:
        # Strip -> Get rid of 0s
        # Split -> split with the space into a list
        line
        dataset.append()

    return dataset
