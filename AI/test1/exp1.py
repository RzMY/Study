# coding=utf-8
"""
课程：《人工智能导论》
实验1：逻辑回归和线性分类模型
作者：林野
学校：四川农业大学，信息工程学院
日期：2022.9.28
"""

from matplotlib import pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import Perceptron
from sklearn.svm import LinearSVC as SVM
import numpy as np
import random


def makeData(classNumber, dim=2):
    """
    classNumber: 类数量，格式为[类别1数，类别2数]
    dim：数据维度
    """
    data = []
    for i, number in enumerate(classNumber):
        samples = np.random.randn(number, dim) + i * 3  # 均值3的倍增，方差1的number个数据
        for sample in samples:
            label = i
            data.append([sample, label])  # 构造数据为[x,label]
    random.shuffle(data)  # 打乱数据

    # 分离数据和标签
    output = []
    labels = []
    for v in data:
        output.append(v[0])
        labels.append(v[1])
    return np.array(output), np.array(labels)


def plotSamples(data, labels, title, logical, perceptron, svm):
    """
    画出数据和决策面
    """
    # 模型参数
    logical_w = logical.coef_[0]
    logical_b = logical.intercept_[0]
    perceptron_w = perceptron.coef_[0]
    perceptron_b = perceptron.intercept_[0]
    svm_w = svm.coef_[0]
    svm_b = svm.intercept_[0]

    # 求解决策面
    x_min = np.min(data[:, 0])  # .astype("int")
    x_max = np.max(data[:, 0])  # .astype("int")
    x = np.linspace(x_min, x_max, 100)
    y_logical = (
        -(logical_w[0] * x + logical_b) / logical_w[1]
    )  # 决策面 sigmoid(z)=0.5，解得z=0, 即w0*x+w1*y+b=0
    y_perceptron = (
        -(perceptron_w[0] * x + perceptron_b + 1) / perceptron_w[1]
    )  # 决策面 z=0
    y_svm = -(svm_w[0] * x + svm_b) / svm_w[1]  # 决策面 z=0

    # 画图
    plt.plot(x, y_logical, "r")
    plt.plot(x, y_perceptron, "g")
    plt.plot(x, y_svm, "b")
    plt.legend(["Logical", "Perceptron", "SVM"])
    plt.scatter(data[:, 0], data[:, 1], c=labels)
    plt.title(title, fontsize="large", fontweight="bold", color="blue")
    plt.show()


def run(trainingSize, testingSize):
    """ 
    实验主函数
    """
    # 获取数据
    train_data, train_labels = makeData(trainingSize)
    test_data, test_labels = makeData(testingSize)

    # 训练模型，调用相关模型库
    logical = LogisticRegression()
    perceptron = Perceptron()
    svm = SVM()
    logical.fit(train_data, train_labels)
    perceptron.fit(train_data, train_labels)
    svm.fit(train_data, train_labels)

    # 计算准确率
    logical_train_accuracy = logical.score(train_data, train_labels) * 100.0
    logical_test_accuracy = logical.score(test_data, test_labels) * 100.0
    perceptron_train_accuracy = perceptron.score(train_data, train_labels) * 100.0
    perceptron_test_accuracy = perceptron.score(test_data, test_labels) * 100.0
    svm_train_accuracy = svm.score(train_data, train_labels) * 100.0
    svm_test_accuracy = svm.score(test_data, test_labels) * 100.0

    # 打印结果
    print(
        "【逻辑回归】训练准确率：%4.2f%%; 测试准确率：%4.2f%%"
        % (logical_train_accuracy, logical_test_accuracy)
    )
    print(
        "【感知机分类】训练准确率：%4.2f%%; 测试准确率：%4.2f%%"
        % (perceptron_train_accuracy, perceptron_test_accuracy)
    )
    print(
        "【SVM分类】训练准确率：%4.2f%%; 测试准确率：%4.2f%%" % (svm_train_accuracy, svm_test_accuracy)
    )

    # 画出图形
    plotSamples(train_data, train_labels, "training data", logical, perceptron, svm)
    plotSamples(test_data, test_labels, "testing data", logical, perceptron, svm)


# 执行程序
if __name__ == "__main__":
    training_size = [1000, 1000]  # 构建2类训练数据，大小分别为500，500
    testing_size = [200, 200]  # 构建2类测试数据，大小分别为100，100
    run(training_size, testing_size)  # 执行训练和测试
