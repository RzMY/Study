from sklearn.metrics import accuracy_score,precision_score,f1_score,precision_recall_fscore_support, recall_score
from sklearn.svm import LinearSVC,SVC
def bin_evaluation(X_train, y_train, X_test, y_test):
    '''
    评估二分类模型
    :param X_train: 训练数据集
    :param y_train: 训练集类别
    :param X_test: 测试数据集
    :param y_test: 测试集实际类别
    :return:
    correct_num - 正确分类的样本个数
    prec - 正类的准确率
    recall - 正类的召回率
    f_score - 正类的f值
    '''
    classifier = LinearSVC()
    correct_num, prec, recall, fscore = None, None, None, None
    #   请在此添加实现代码   #
    # ********** Begin *********#

    classifier.fit(X_train, y_train)
    y_pred = classifier.predict(X_test)
    correct_num = accuracy_score(y_test, y_pred, normalize=False)
    prec = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    fscore = f1_score(y_test, y_pred)
    return correct_num, prec, recall, fscore
    # ********** End **********#
def multi_evaluation(X_train,y_train,X_test,y_test):
    '''
    评估多分类模型
    :param X_train: 训练数据集
    :param y_train: 训练集类别
    :param X_test: 测试数据集
    :param y_test: 测试集实际类别
    :return:
    acc - 模型的精度
    prec - 准确率
    f_score - f值
    '''
    #初始化
    acc,prec,f_score = None,None,None
    classifier = SVC(kernel='linear')
    #   请在此添加实现代码   #
    # ********** Begin *********#

    classifier.fit(X_train, y_train)
    y_pred = classifier.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    prec = precision_score(y_test, y_pred, average='macro')
    f_score = f1_score(y_test, y_pred, average='macro')
    return acc, prec, f_score
    # ********** End **********#