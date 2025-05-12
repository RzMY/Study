# coding=utf-8
"""
课程：《人工智能导论》
实验2：多层人工神经网络分类
作者：林野
学校：四川农业大学，信息工程学院
日期：2022.9.29
"""

import torch
from torch import nn, optim
import torch.utils.data as Data
import numpy as np

# 超参数
BATCH_SIZE = 32  # 批大小
LEARNING_RATE = 0.01  # 学习率
STOP_ACCURACY = 98.0  # 训练终止精确度，百分比值
EPOCH = 100  # 最大训练轮数


# 网络模型定义
class DNN(nn.Module):
    def __init__(self, inputDim, outputDim):
        super(DNN, self).__init__()

        self.fc = nn.Sequential(
            nn.Linear(inputDim, 50), nn.ReLU(), nn.Linear(50, outputDim)
        )  # 输出维度即为分类数目，输出不用softmax，因为交叉熵计算时已包含进去。

    def forward(self, x):
        x = self.fc(x)
        return x


def makeDataLoader(dataSize, dim=2):
    """
    dataSize: 类数量，格式为[类别1数，类别2数]
    dim：数据维度
    """
    data = []
    labels = []
    for i, number in enumerate(dataSize):
        samples = np.random.randn(number, dim) + i * 3  # 均值3的倍增，方差1的number个数据
        label = i
        for sample in samples:
            data.append(sample)
            labels.append(label)  # 构造数据为[x,label]

    # 数据转化为tensor
    data = torch.Tensor(np.array(data))
    labels = torch.LongTensor(np.array(labels))
    datasets = Data.TensorDataset(data, labels)
    # 构建数据读取器
    return Data.DataLoader(
        dataset=datasets, batch_size=BATCH_SIZE, shuffle=True, num_workers=2
    )


def run(trainingSize, testingSize, dataDim):
    """
    实验主函数
    """
    # 获取数据
    train_loader = makeDataLoader(trainingSize, dataDim)
    test_loader = makeDataLoader(testingSize, dataDim)
    train_size = sum(trainingSize)
    test_size = sum(testingSize)

    # 训练模型，调用相关模型库
    net = DNN(dataDim, len(trainingSize))  # 实例化模型
    loss_func = nn.CrossEntropyLoss()  # 实例化损失函数，多分类用交叉熵
    optimizer = optim.SGD(net.parameters(), lr=LEARNING_RATE)  # 构建优化器

    # 开始训练
    for epoch in range(EPOCH):
        correct_num = 0  # 计算每轮正确预测类别的数量
        total_loss = 0.0  # 每轮的总损失
        for data, labels in train_loader:
            optimizer.zero_grad()  # 梯度清零
            output = net(data)  # 模型预测
            loss = loss_func(output, labels)  # 损失计算
            loss.backward()  # 反向传播，计算梯度
            optimizer.step()  # 更新模型参数
            predict = torch.argmax(output, axis=1)  # softmax回归，找到概率值最大的为预测类别
            correct_num += float(torch.sum(predict == labels))  # 累加准确数
            total_loss += float(loss)  # 累计损失
        train_accuracy = 100.0 * correct_num / train_size  # 总的训练准确度
        print(
            "训练完成度：[%d/%d]；总损失: %4.4f; 准确率：%4.2f%%"
            % (epoch + 1, EPOCH, total_loss, train_accuracy)
        )
        # 训练精度达到要求，中断训练
        if train_accuracy > STOP_ACCURACY:
            print("第%d轮训练已达成训练准确度大于%4.2f%%要求" % (epoch + 1, STOP_ACCURACY))
            break

    # 测试数据
    net.eval()  # 模型改为评估模式
    correct_num = 0
    for data, labels in test_loader:
        output = net(data)
        predict = torch.argmax(output, axis=1)  # 找到概率值最大的为预测类别
        correct_num += float(torch.sum(predict == labels))  # 累加准确数
    test_accuracy = 100.0 * correct_num / test_size
    print("模型最终测试准确率：%4.2f%%" % (test_accuracy))


# 执行程序
if __name__ == "__main__":
    training_size = [10000, 10000, 10000, 10000]  # 构建4类训练数据，大小分别为10000
    testing_size = [5000, 5000, 5000, 5000]  # 构建4类测试数据，大小分别为5000
    data_dim = 100  # 构建数据维度
    run(training_size, testing_size, data_dim)  # 执行训练和测试
