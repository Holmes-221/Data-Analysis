import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
sns.set()
mean = (0,0)
cov=[
    [[ 1 , 0 ], [ 0 , 1 ]],
    [[ 0.2 , 0 ], [ 0 , 0.2 ]],
    [[ 4 , 0 ], [ 0 , 4 ]],
    [[ 0.2 , 0 ], [ 0 , 4 ]],
    [[ 4 , 0 ], [ 0 , 0.2 ]],
    [[ 1 , 0.5 ], [ 0.5 , 1 ]],
    [[ 0.3 , 0.5 ], [ 0.5 , 4 ]],
    [[ 3 , 1.5 ], [ 1.3 , 3 ]]
]
n=241
for i in range(len(cov)):
    x= np.random.multivariate_normal(
        mean,
        cov[0],
        size = (500,1)
    )
    x1=x[:,0]
    plt.subplot(n+i)
    plt.scatter(x1[:,0],x1[:,1], marker=".")
plt.show()