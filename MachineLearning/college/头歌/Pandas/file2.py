# -*- coding: utf-8 -*-
from pandas import Series,DataFrame
import  pandas as pd
# pandas版本原因显示，设置列名仅显示4列
pd.set_option('display.max_columns', 4)


def read_csv_data():
    '''
    返回值:
    df1: 一个DataFrame类型数据
    length1: 一个int类型数据
    '''

    df1 = pd.read_csv('test3/uk_rain_2014.csv')
    df1.columns = ['water_year','rain_octsep','outflow_octsep','rain_decfeb', 'outflow_decfeb', 'rain_junaug', 'outflow_junaug']
    length1 = len(df1)
    #返回df1,length1
    return df1,length1