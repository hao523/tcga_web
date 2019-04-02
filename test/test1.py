import numpy as np
import csv
from collections import Counter
data = np.random.rand(20, 20)
mat = np.matrix(data)
with open('outfile.txt','wb') as f:
    for line in mat:
        np.savetxt(f, line, fmt='%.2f')