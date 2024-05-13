from sklearn import datasets

def getIrisData():

    '''
    导入Iris数据集

    返回值：
    X - 前5条训练特征数据
    y - 前5条训练数据类别
    X_shape - 训练特征数据的二维数组大小
    '''
    #初始化
    X = [] 
    y = [] 
    X_shape = () 

	#   请在此添加实现代码   #
	#********** Begin *********#
    iris = datasets.load_iris()
    X = iris.data[:5]
    y = iris.target[:5]
    X_shape = iris.data.shape

	#********** End **********#

    return X,y,X_shape