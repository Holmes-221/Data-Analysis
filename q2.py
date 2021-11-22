import xlrd as x
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def excel2matrix(path):
    data = x.open_workbook(path)
    table = data.sheets()[0]
    nrows = table.nrows  #工作表的行数
    ncols = table.ncols  #工作表的列数
    datamatrix = np.zeros((nrows,ncols))
    for i in range(1, nrows):
        datamatrix[i,:] = table.row_values(i)
    return datamatrix

# filepath = r"D:\rubbish\data_1.xls"
filepath = input()
datas = excel2matrix(filepath) #数据提取
row = 841
data2 = np.delete(datas, row, axis = 0)

EXPE = data2[1:, 1]
QIAL = data2[1:, 2]
LOYA = data2[1:, 3]
SATI = data2[1:, 4]
a = [EXPE,QIAL,LOYA,SATI]
df = pd.DataFrame(a).T

#散点图矩阵
# pd.plotting.scatter_matrix(df, diagonal='kde', color='k')
#画箱线图
# df.boxplot()
# plt.boxplot(x = df.values, labels = df.columns, whis=1.5)
# des = df.describe()
#pearson相关系数矩阵
# pccs = np.corrcoef(a)
# print(pccs)
# plt.show()

#假设检验
import scipy.stats as ss
p_value = np.zeros((len(a),len(a)))
for i in range(len(a)):
    for j in range(len(a)):
        p_value[i,j] = ss.pearsonr(a[i],a[j])[1]
print(p_value)
