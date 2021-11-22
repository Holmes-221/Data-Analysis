import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import scipy.misc as sm
def desc(X,n):
    """
    提取特征（对数据 X 提取 n 个特征）
    """
    u,l,vh = np.linalg.svd(X)
    newX = np.dot(np.dot(u[:,:n], np.diag(l)[:n,:n]), vh[:n,:])
    return newX

path = input()
imgs = Image.open(path)
img_array = np.array(imgs)
a=[]

eig_n = 2

for i in range(img_array.shape[2]):
    a.append(desc(img_array[:,:,i],eig_n))
pic = np.dstack((a)) 
#标准图像存储，支持任意图片格式和数据格式
sm.imsave("outfile3.png", pic)