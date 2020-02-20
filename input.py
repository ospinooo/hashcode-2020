
def parse_input(filename):
    """Creates the dataset from the filename data

    Arguments:
        filename {FILE} -- Filename
    """
    with open(filename, 'r') as f:
        lines = f.readlines()

    # B: Number of different books
    # L: Number of libraries
    # D: Number of days
    B, L, D = [int(value) for value in lines[0].split()]
    
    scores = [int(value) for value in lines[1].split()]

    libraries = []
    for i in range(0, 2*L, 2):
        # Strip -> Get rid of 0s
        # Split -> split with the space into a list
        N, T, M = lines[i].split()

        libraries.append({
            'total_books':N,
            'sign_up_days': T, 
            'books_day':M,
            'books' : [int(value) for value in lines[i+1].split()]
        })

    return libraries, scores, D
