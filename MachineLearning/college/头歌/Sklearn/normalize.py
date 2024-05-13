from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import scale
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import fetch_california_housing
'''
Data descrption:
The data contains 20,640 observations on 9 variables.
This dataset contains the average house value as target variable
and the following input variables (features): average income,
housing average age, average rooms, average bedrooms, population,
average occupation, latitude, and longitude in that order.
dataset : dict-like object with the following attributes:
    dataset.data : ndarray, shape [20640, 8]
        Each row corresponding to the 8 feature values in order.
    dataset.target : numpy array of shape (20640,)
        Each value corresponds to the average house value in units of 100,000.
    dataset.feature_names : array of length 8
        Array of ordered feature names used in the dataset.
    dataset.DESCR : string
        Description of the California housing dataset.
'''
dataset = fetch_california_housing("./step4/")
X_full, y = dataset.data, dataset.target
#抽取其中两个特征数据
X = X_full[:, [0, 5]]
def getMinMaxScalerValue():
    '''
    对特征数据X进行MinMaxScaler标准化转换，并返回转换后的数据前5条
    返回值:
    X_first5 - 数据列表
    '''
    X_first5 = []
    #   请在此添加实现代码   #
    # ********** Begin *********#

    MinMax_Scaler = MinMaxScaler()
    X_first5 = MinMax_Scaler.fit_transform(X)[:5]

    # ********** End **********#
    return X_first5
def getScaleValue():
    '''
        对目标数据y进行简单scale标准化转换，并返回转换后的数据前5条
        返回值:
        y_first5 - 数据列表
        '''
    y_first5 = []
    #   请在此添加实现代码   #
    # ********** Begin *********#

    y = scale(y)

    # ********** End **********#
    return y_first5
def getStandardScalerValue():
    '''
    对特征数据X进行StandardScaler标准化转换，并返回转换后的数据均值和缩放比例
    返回值:
    X_mean - 均值
    X_scale - 缩放比例值
    '''
    X_mean = None
    X_scale = None
    #   请在此添加实现代码   #
    #********** Begin *********#

    Standard_Scaler = StandardScaler()
    X = Standard_Scaler.fit_transform(X)
    X_mean = Standard_Scaler.mean_
    X_scale = Standard_Scaler.scale_

    #********** End **********#
    return X_mean,X_scale