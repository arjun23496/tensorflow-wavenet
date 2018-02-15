import os
import sys

import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import numpy as np

print sys.argv

generated_file = sys.argv[1]
save_dir = sys.argv[3]
index = int(sys.argv[4])
count = int(sys.argv[5])

# Finding ground truth
count += 1

if os.path.isfile('../data/test-corpus/p'+str(index)+"_"+str(count)+".entropy"):
	ground_truth = np.loadtxt('../data/test-corpus/p'+str(index)+"_"+str(count)+".entropy")
else:
	ground_truth = np.loadtxt('../data/corpus/p'+str(index)+'/p'+str(index)+"_"+str(count)+".entropy")

generated_data = np.load(generated_file)

# plt.plot(generated_file, label='generated')
# plt.plot(ground_truth, label='ground truth', alpha=0.7)

# plt.legend()

# file_name = 'p'+str(index)+"_"+str(count)+".entropy"
# plt.savefig(save_dir+'/'+file_name+'.png')

correlation = np.correlate(ground_truth, generated_data, "full")

file_name = 'p'+str(index)+"_"+str(count)+".correlation"

np.savetxt(save_dir+'/'+file_name)
