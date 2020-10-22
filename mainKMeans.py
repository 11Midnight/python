import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
def readData(param):
    points = []
    txt = open('datasets/'+param, "r")
    lines = txt.readlines()
    for i in lines:
        tmp = i.split()
        tmp[0] = int(tmp[0])
        tmp[1] = int(tmp[1])
        points.append(tmp)
    points = np.array(points)
    return points
data_paths = ['birch1.txt','birch2.txt','birch3.txt','s1.txt']
print('chose dataset:')
for i in range(len(data_paths)):
    print(str(i)+'-->'+data_paths[i])
path_index = int(input())
print('enter number of clusters:')
cl_numb = int(input())
colors = ['#1e4b44', 'red', 'blue', 'green', 'cyan', 'magenta', 'yellow', 'orange', '#ad09a3', 'deeppink']
data, _ = make_blobs(n_samples=1000, n_features=2, centers=cl_numb)
data = readData(data_paths[path_index])
kmeans = KMeans(n_clusters=cl_numb)
kmeans.fit(data)
clusters = kmeans.cluster_centers_
y_km = kmeans.fit_predict(data)
for i in range(cl_numb):
    plt.scatter(data[y_km==i,0],data[y_km==i,1],s=10,color=colors[i])
plt.show()