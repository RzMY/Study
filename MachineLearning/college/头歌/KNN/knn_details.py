import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
np.random.seed(20)


def predict(x_test, x_train, y_train, k = 3):
    results = []  # 创建一个空列表来存储所有的预测结果
    for i in range(len(x_test)):  # 对每个测试样本进行预测
        dis = np.sqrt(np.sum((x_test[i] - x_train) ** 2, axis=1))
        index = np.argsort(dis)[:k]
        count = np.bincount(y_train[index])
        result = np.argmax(count)
        results.append(result)  # 将预测结果添加到结果列表中
    return np.array(results)  # 返回包含所有预测结果的numpy数组


if __name__ == '__main__':
    iris = load_iris()
    x_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2)
    result = predict(x_test, x_train, y_train)
    score = (np.sum(result == y_test) / len(result))
    if score >= 0.9:
        print("测试通过")
    else:
        print("测试失败")
