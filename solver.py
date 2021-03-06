

# Shows the score in the progress bar
# pbar = tqdm(range(n))
# pbar.set_postfix(score=show.score, avg_score=avg_score)
from tqdm import tqdm
import random
import time


def solve(libraries, scores, D):
    """
        N libraries:
        books per library
        ids
    """
    # ORDER
    libraries = sorted(libraries, key=lambda k: k['sign_up_days'] * (1/(k['all_sum']*k['books_day'])))
    # SHUFFLE
    # random.seed(time.time())
    # random.shuffle(libraries)

    selected_libraries = []
    current_day = 0
    libraries_i = 0

    sign_up = False
    last = 0

    fin_libraries = []
    pbar = tqdm(range(D))
    indices_introduced = set()

    score = 0
    total_books = 0
    for current_day in pbar:
        
        if sign_up and selected_libraries[libraries_i - 1]['sign_up_days'] + last == current_day:
            selected_libraries[libraries_i - 1]['signed_up'] = True
            last = current_day
            sign_up = False

        if not sign_up:
            if libraries_i < len(libraries):
                selected_libraries.append(libraries[libraries_i])
                libraries_i += 1
                sign_up = True
        
        for i in range(len(selected_libraries)):
            lib = selected_libraries[i]
            if lib['signed_up'] and lib['index_selected'] >= 0:
                # Introduce books
                sel = []
                while lib['index_selected'] >= 0 and len(sel) < lib['books_day']:
                    i_insert = lib['books'][lib['index_selected']]
                    if i_insert not in indices_introduced:
                        sel.append(i_insert)
                        lib['number_books'] += 1
                        score += scores[i_insert]
                        indices_introduced.add(i_insert)
                        total_books += 1

                    lib['index_selected'] -= 1

                lib['selected'] += sel
            
        pbar.set_postfix(score=score, total_books=total_books)
    print(total_books, "/", len(scores))
    return selected_libraries, score
