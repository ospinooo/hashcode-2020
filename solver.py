

# Shows the score in the progress bar
# pbar = tqdm(range(n))
# pbar.set_postfix(score=show.score, avg_score=avg_score)
from tqdm import tqdm


def solve(libraries, scores, D):
    """
        N libraries:
        books per library
        ids
    """
    selected_libraries = []
    current_day = 0
    libraries_i = 0

    sign_up = False
    last = 0

    fin_libraries = []
    pbar = tqdm(range(D))
    score = 0
    for current_day in pbar:

        if not sign_up:
            if len(libraries) > libraries_i:
                selected_libraries.append(libraries[libraries_i])
                libraries_i += 1
                sign_up = True
        else:
            if selected_libraries[libraries_i - 1]['sign_up_days'] + last == current_day:
                selected_libraries[libraries_i - 1]['signed_up'] = True
                last += current_day
                sign_up = False

        for i in range(len(selected_libraries)):
            lib = selected_libraries[i]
            if lib['signed_up']:
                # Introduce books
                if lib['number_books'] < lib['total_books']:
                    ini = lib['total_books'] - lib['number_books'] - lib['books_day']
                    fin = lib['total_books'] - lib['number_books'] 
                    score += sum([i for i in lib['books'][ini:fin]])
                    lib['number_books'] = lib['number_books'] + lib['books_day']
                    if lib['number_books'] > lib['total_books']:
                        lib['number_books'] = lib['total_books']
                else:
                    fin_libraries.append(lib)
                    del selected_libraries[i]

        pbar.set_postfix(score=score)
        current_day += 1
    
    return fin_libraries + selected_libraries, score
