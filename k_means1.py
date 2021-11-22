from sklearn.cluster import k_means
from sklearn.cluster.k_means_ import KMeans
KMeans()
"""
参数：
    n_clusters=8,         生成的分类数目，聚类数
    init=
            'k-means++',
            'random'     从训练数据中随机选取质心
            vector      将vector作为初始质心
    n_init=10, 
    max_iter=300,         算法的最大迭代次数，超过则停止运行
    tol=0.0001, 
    precompute_distances='auto',
    verbose=0, 
    random_state=None, 
    copy_x=True, 
    n_jobs=1, 
    algorithm='auto'
属性：
    cluster_centers_    质心坐标
    labels              数据集的分类结果
    inertia_            每个点到该点分类的之心的距离和
"""