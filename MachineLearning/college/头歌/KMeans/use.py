#encoding=utf8
from sklearn.cluster import KMeans

def kmeans_cluster(data):
    '''
    input:data(ndarray):样本数据
    output:result(ndarray):聚类结果
    '''
    #********* Begin *********#
    kmeans = KMeans(n_clusters=3)
    kmeans.fit(data)
    result = kmeans.predict(data)
    #********* End *********# 
    return result