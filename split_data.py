import os
from os import listdir
from os.path import isfile, join

import numpy as np


def split_arr_into_files(entropy_vals, file_id, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    len_entropy_vals = len(entropy_vals)
    split_index = 0
    arr_index = 0
    while True:
        split_index+=1
        rand_val = np.random.normal(0.0, 0.15)
        with open(output_dir + str(file_id) + "_" + str(split_index) + ".entropy", "w") as f:
            new_index = arr_index + int(0.02*len_entropy_vals*(1 + rand_val))
            for temp_val in entropy_vals[arr_index:min(new_index, len_entropy_vals)]:
                f.write(temp_val + "\n")

        arr_index = new_index
        if arr_index >= len_entropy_vals:
            break

def list_files(folder_path):
    return [join(folder_path, f) for f in listdir(folder_path) if isfile(join(folder_path, f))]

def get_arr(f_path):
    x = []
    for l in open(f_path):
        x.append(l.strip())
    return np.array(x)


entropy_file_index = 0
with open("file_index_map.txt", "w") as f:
    for file_path in list_files("/home/arjun/chaos/work/data/"):
        entropy_file_index+=1
        f.write(str(entropy_file_index) + "," + file_path.split("/")[-1] + "\n")
        split_arr_into_files(get_arr(file_path), "p" + str(entropy_file_index), "/home/arjun/chaos/work/corpus/entropy_files/p" + str(entropy_file_index) + "/")