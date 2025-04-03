# 导入数据集，分类器相关包
from sklearn import datasets, svm, metrics
import pickle

# 导入digits数据集
digits = datasets.load_digits()
n_samples = len(digits.data)
data = digits.data

# 使用前一半的数据集作为训练数据，后一半数据集作为测试数据
train_data,train_target = data[:n_samples // 2],digits.target[:n_samples // 2]
test_data,test_target = data[n_samples // 2:],digits.target[n_samples // 2:]


def createModel():
    classifier = svm.SVC()
    classifier.fit(train_data,train_target)
    return classifier

local_file = 'dumpfile'
def dumpModel():
    '''
    存储分类模型

    '''
    clf = createModel()
    # 请在此处补全模型存储语句 #
    #********** Begin *********#

    with open(local_file, 'wb') as f:
        pickle.dump(clf, f)

    #********** End **********#

def loadModel():
    '''
    加载模型，并使用模型对测试数据进行预测，返回预测值

    返回值：
    predicted - 模型预测值
    '''
    predicted = None
    # 请在此处补全模型加载语句，并对预测数据分类返回预测值#
    #********** Begin *********#

    with open(local_file, 'rb') as f:
        clf = pickle.load(f)
        predicted = clf.predict(test_data)

    #********** End **********#

    return predicted