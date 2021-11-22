import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
path = input()
df = pd.read_excel(path,header=0, index_col=0)
data = pd.DataFrame(df)
A = np.array(data)
p = np.corrcoef(A.T)
U,L,VH = np.linalg.svd(p)
d=[]
sigmas = sum(L)
print(L)
for i in L:
    d.append(i/sigmas)
print(d) #贡献率
#前两个主成分所对应的值
Y2 = abs(np.dot(A,VH[:2,:].T))
#重新构建数据
B = pd.DataFrame(Y2,index = data.index)
#按照第一主成分排序
print(B.sort_values(by = 0, axis=0))
#城市散点图
x = B.values[:,0]
y = B.values[:,1]
plt.scatter(x, y)
plt.xlabel("第一主成分得分",fontsize = 16)
plt.ylabel("第二主成分得分",fontsize = 16)
for i in range(len(data.index)):
    plt.annotate(data.index[i], xy = (x[i], y[i]), xytext = (x[i] - 0.1, y[i]-0.1),fontsize = 16)
plt.show()