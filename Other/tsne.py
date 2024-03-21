from sklearn.cluster import KMeans
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 使用pandas读取CSV文件
df = pd.read_csv(r'H:\\Study\\Study\\Other\\test.csv')

# 提取'电阻'和'电阻变化率'两列的值
X = df[['电阻', '电阻变化率']].values

# 可视化原始数据
plt.scatter(X[:, 0], X[:, 1])
plt.show()

# 使用KMeans进行聚类
kmeans = KMeans(n_clusters=3)  # 假设我们想要将数据分为3个聚类
kmeans.fit(X)
labels = kmeans.labels_

color = ['blue', 'green', 'red']
class_label = ['A', 'B', 'C']
recs = []
for i in range(0, len(color)):
    recs.append(plt.Rectangle((0, 0), 1, 1, fc=color[i]))
plt.legend(recs, class_label)
# 使用matplotlib进行可视化
plt.scatter(X[:, 0], X[:, 1], c=labels)
plt.show()