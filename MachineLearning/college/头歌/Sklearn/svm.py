import matplotlib.pyplot as plt

# 导入数据集，分类器相关包
from sklearn import datasets, svm, metrics

# 导入digits数据集
digits = datasets.load_digits()
n_samples = len(digits.data)
data = digits.data

# 使用前一半的数据集作为训练数据，后一半数据集作为测试数据
train_data,train_target = data[:n_samples // 2],digits.target[:n_samples // 2]
test_data,test_target = data[n_samples // 2:],digits.target[n_samples // 2:]


def createModelandPredict():
    '''
    创建分类模型并对测试数据预测

    返回值：
    predicted - 测试数据预测分类值
    '''
    predicted = None
    #   请在此添加实现代码   #
    #********** Begin *********#
    
    

    Classifier = svm.SVC(gamma=0.001)
    Classifier.fit(train_data, train_target)
    predicted = Classifier.predict(test_data)
    
    #********** End **********#
    
    return predicted