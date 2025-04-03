#encoding=utf8
import numpy as np
#计算样本间距离
def distance(x, y, p=2):
    '''
    input:x(ndarray):第一个样本的坐标
          y(ndarray):第二个样本的坐标
          p(int):等于1时为曼哈顿距离，等于2时为欧氏距离
    output:distance(float):x到y的距离      
    '''
    #********* Begin *********#    
    dis = np.sum(np.abs(x-y)**p)**(1/p)
    return dis
    #********* End *********#
    
#计算质心
def cal_Cmass(data):
    '''
    input:data(ndarray):数据样本
    output:mass(ndarray):数据样本质心
    '''
    #********* Begin *********#
    Cmass = np.mean(data,axis=0)
    #********* End *********#
    return Cmass

#计算每个样本到质心的距离，并按照从小到大的顺序排列
def sorted_list(data,Cmass):
    '''
    input:data(ndarray):数据样本
          Cmass(ndarray):数据样本质心
    output:dis_list(list):排好序的样本到质心距离
    '''
    #********* Begin *********#
    dis_list = []
    for i in range(len(data)):
        dis = distance(data[i],Cmass)
        dis_list.append(dis)
    dis_list.sort()
    #********* End *********#
    return dis_list