'''
X samples (n x m array), aka data points or "singleton clusters"
n number of samples
m number of features
Z cluster linkage array (contains the hierarchical clustering information)
k number of clusters
'''

from matplotlib import pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
import numpy as np

# https://docs.scipy.org/doc/numpy/reference/generated/numpy.random.multivariate_normal.html
a = np.random.multivariate_normal([10, 0], [[3, 1], [1, 4]], size=[100,])
b = np.random.multivariate_normal([0, 20], [[3, 1], [1, 4]], size=[50,])
X = np.concatenate((a, b),)
print X.shape  # 150 samples with 2 dimensions
plt.scatter(X[:,0], X[:,1])
plt.show()

Z = linkage(X, 'ward')

# calculate full dendrogram

plt.title('Hierarchical Clustering Dendrogram (truncated)')
plt.xlabel('sample index or (cluster size)')
plt.ylabel('distance')
dendrogram(Z,
           truncate_mode='lastp',  # show only the last p merged clusters,
           p= 25,  # show only the last p merged clusters
           leaf_rotation=90.,
           leaf_font_size=12.,
           show_contracted=True,  # to get a distribution impression in truncated branches
)
plt.show()