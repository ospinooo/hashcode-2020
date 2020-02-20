

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
    # libraries = sorted(libraries, key=lambda k: k['all_sum'], reverse=True)
    # SHUFFLE
    random.seed(int(time.time()))
    random.shuffle(libraries)

    selected_libraries = []
    current_day = 0
    libraries_i = 0

    sign_up = False
    last = 0

    fin_libraries = []
    pbar = tqdm(range(D))
    indices_introduced = set()

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
            if lib['signed_up'] and lib['index_selected'] > 0:
                # Introduce books
                sel = []
                while lib['index_selected'] >= 0 and len(sel) < lib['books_day']:
                    if lib['books'][lib['index_selected']] not in indices_introduced:
                        i_insert = lib['books'][lib['index_selected']]
                        sel.append(i_insert)
                        lib['number_books'] += 1
                        score += scores[i_insert]
                        indices_introduced.add(lib['index_selected'])

                    lib['index_selected'] -= 1

                lib['selected'] += sel
            
        pbar.set_postfix(score=score)
        current_day += 1
    
    return selected_libraries, score
