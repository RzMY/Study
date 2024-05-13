# -*- coding: utf-8 -*-
from pandas import Series,DataFrame
import  pandas as pd

def create_series():
    '''
    返回值:
    series_a: 一个Series类型数据
    series_b: 一个Series类型数据
    dict_a：  一个字典类型数据
    '''

    series_a = Series([1,2,5,7],index=['nu', 'li', 'xue', 'xi'])
    dict_a = {'ting':1, 'shuo':2, 'du':32, 'xie':44}
    series_b = Series(dict_a)

    # 返回series_a,dict_a,series_b
    return series_a,dict_a,series_b