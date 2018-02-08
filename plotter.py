import os
import sys

import matplotlib
matplotlib.use('GTK')

import matplotlib.pyplot as plt

generated_file = sys.argv[1]
ground_truth = sys.argv[2]
save_dir = sys.argv[3]

plt.plot(generated_file, label='generated')
plt.plot(ground_truth, label='ground truth', alpha=0.7)

plt.legend()

file_name = ground_truth.split('/')[-1]
plt.savefig(save_dir+'/'+file_name+'.png')