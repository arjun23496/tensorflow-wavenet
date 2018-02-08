import os
from os import listdir
from os.path import isfile, join, isdir
import shutil

import numpy as np

def list_files(folder_path):
    return [join(folder_path, f) for f in listdir(folder_path) if isfile(join(folder_path, f))]

def list_dirs(folder_path):
	return [join(folder_path, f) for f in listdir(folder_path) if isdir(join(folder_path, f))]

entropy_folder_path = "/home/akaruvally/corpus/entropy_files/"
for folder_path in list_dirs(entropy_folder_path):
	all_files = list_files(folder_path)
	rand_indices = np.random.randint(0,high=len(all_files),size=5)
	for rand_idx in rand_indices:
		file_path = all_files[rand_idx]
		if isfile(file_path):
			shutil.move(file_path,"/home/akaruvally/corpus/test-corpus/" + file_path.split("/")[-1])
