from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_digits
import numpy as np
np.random.seed(10)


def model_train(x, y):
    """
    x : 特征值
    y : 目标值
    """
    # 请根据注释正确补充代码，让程序能够输出正确答案
    # ********** Begin ********** #
    # 将给出的特征向量中分出80%作为模型训练数据，剩下作为测试数据
    x_train = x[:int(0.8 * len(x))]
    y_train = y[:int(0.8 * len(y))]
    x_test = x[int(0.8 * len(x)):]
    y_test = y[int(0.8 * len(y)):]
    # 实例化一个knn的分类器，n_neighbors值为3
    knn = KNeighborsClassifier(n_neighbors=3)
    # 传入训练数据进行模型训练
    knn.fit(x_train, y_train)
    # 传入测试数据对模型得分进行评估
    score = knn.score(x_test, y_test)
    # ********** End ********** #
    return score

if __name__ == '__main__':
    digit = load_digits()
    x = digit.data
    y = digit.target
    model_score = model_train(x, y)
    print(model_score)
