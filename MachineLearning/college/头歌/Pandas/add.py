# -*- coding: utf-8 -*-
from pandas import Series,DataFrame
import numpy as np
import  pandas as pd

def add_way():
    '''
    返回值:
    df3: 一个DataFrame类型数据
    '''

    # df1,df2是DataFrame类型数据
    df1 = DataFrame(np.arange(12.).reshape((3, 4)), columns=list('abcd'))
    df2 = DataFrame(np.arange(20.).reshape((4, 5)), columns=list('abcde'))

    df3 = df1.add(df2, fill_value=4)

    # 返回df3
    return df3