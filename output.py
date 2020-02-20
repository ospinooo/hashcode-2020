import time


def save(filename, libraries, score):
    """Save data in the filename given. The result's score will be in the file filename.

    Arguments:
        filename {filename} -- Refers to the input data
        data {list} -- Result data to write in the filename
        score {int} -- Score we have achieve
    """

    with open(f"./results/{filename}_{str(score)}_{time.time()}.txt", 'w') as f:

        libraries = [lib for lib in libraries if lib["number_books"] > 0]

        f.write(str(len(libraries)))
        for lib in libraries:
            f.write("\n" + str(lib['id']) + " " + str(lib["number_books"]))
            f.write("\n")
            f.write(" ".join([str(lib["books"].pop()) for i in range(lib["number_books"])]))
                

        f.close()
