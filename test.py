import numpy as np
from sklearn.cluster import KMeans
from PIL import Image
import matplotlib.pyplot as plt
import scipy.misc as sm
path = r"D:\rubbish\matlab\data_asys\k_means\c_means\first.png"
k = 5
pic=[]
#聚类个数
data = Image.open(path).convert("L")
img = np.array(data)
s = img.shape
con = np.zeros(s)
line = img.flatten().reshape(-1,1)
k_means = KMeans(n_clusters = k)
k_means.fit(line)
y = k_means.predict(line)
m = k_means.cluster_centers_
for j in range(k):
    c = (y==j).reshape(s)
    name = "flat" + str(j) + ".png"
    plt.imshow(c, cmap = "gray")
    plt.savefig(name)
    pic.append(c)
    con = con + c*m[j]
plt.imshow(con, cmap = "gray")
plt.savefig("picture.png")
# plt.show()