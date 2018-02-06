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
global_min = -1
global_max = -1

print "Computing maximum and minimum"

# for file_path in list_files("/home/akaruvally/data_main/"):
    
#     print file_path," : ",

#     a = np.loadtxt(file_path)

#     local_max = np.max(a)
#     local_min = np.min(a)

#     if global_max == -1 or global_max < local_max:
#         global_max = local_max

#     if global_min == -1 or global_min > local_min:
#         global_min = local_min

global_max = 17
global_min = 0

global_mean = (global_max+global_min)/2

print "Saving files"

with open("file_index_map.txt", "w") as f:
    for file_path in list_files("/home/akaruvally/data_main/"):
        entropy_file_index+=1
        f.write(str(entropy_file_index) + "," + file_path.split("/")[-1] + "\n")
        
        arr = get_arr(file_path)

        arr = (arr - global_mean)/(global_max - global_min)

        split_arr_into_files(arr, "p" + str(entropy_file_index), "/home/akaruvally/data/entropy_files/p" + str(entropy_file_index) + "/")
        print file_path," : complete"
