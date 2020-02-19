import time


def save(filename, data, score):
    """Save data in the filename given. The result's score will be in the file filename.

    Arguments:
        filename {filename} -- Refers to the input data
        data {list} -- Result data to write in the filename
        score {int} -- Score we have achieve
    """

    with open("results/" + filename + "_" + str(score) + "_" + time.time(), 'w') as f:

        for d in data:
            f.write()
