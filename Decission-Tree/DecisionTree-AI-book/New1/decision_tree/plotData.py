import numpy as np
import matplotlib.pyplot as plt
import csv
import glob

plt.rcParams["font.size"] = 36
list_of_files = glob.glob('C:/Users/Shiba/Desktop/ML/Decission-Tree/New1/output/plot/*.csv')
print list_of_files
#dict = {'1': 'blue', '2' :'green'}

for fname in list_of_files:
    #name = fname.split('/')[-1]
    name = fname.split('\\')[-1]
    print name
    x = []
    y = []
    with open(fname,'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            x.append(int(row[0]))
            y.append(float(row[1]))
    plt.plot(x,y, label = name)
    plt.scatter(x,y)

plt.xlabel('x')
plt.ylabel('y')
plt.title('Classification Improment with ~ with out proning')
plt.legend()
plt.show()
