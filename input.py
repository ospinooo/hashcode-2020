
import numpy as np


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
    
    scores = np.array([int(value) for value in lines[1].split()])

    libraries = []
    for i in range(2, 2*L + 1, 2):
        N, T, M = [int(value) for value in lines[i].split()]
        books_i = np.array([int(value) for value in lines[i+1].split()])
        all_books_sum = np.sum(scores[books_i])
        books_ordered_i = books_i[np.argsort(scores[books_i]).tolist()]
        books = books_ordered_i.tolist()
        
        libraries.append({
            'id': i//2 - 1,
            'total_books': N,
            'sign_up_days': T, 
            'books_day': M,
            'books': books,
            'selected': [],
            'number_books': 0,
            'all_sum':all_books_sum,
            'index_selected': len(books) - 1,
            'signed_up': False
        })

    return libraries, scores, D


if __name__ == "__main__":
    print(parse_input("inputs/a_in.txt"))