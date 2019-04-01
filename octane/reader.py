# Goal is to take a .dat file and extract a set of vectors

import os
import numpy as np


def load(name):
    path = get_path(name)
    file = open(path, "r")

    big_list = []
    for line in file:
        current_list = line.split()
        for i in range(len(current_list)):
            current_list[i] = float(current_list[i])
        big_list.append(current_list)

    return np.matrix(big_list)


def get_path(name):
    here = os.path.dirname(os.path.realpath(__file__))  # Current path directory
    file_name = name + ".dat"
    data_folder_path = "data"
    file_path = os.path.join(here, os.pardir, data_folder_path, file_name)
    return file_path
