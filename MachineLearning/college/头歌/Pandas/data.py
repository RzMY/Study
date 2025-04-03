from unittest import result
import pandas as pd


def task1():
    '''
    任务：使用describe()方法对给定数据进行统计描述汇总；
    '''
    # 创建学生成绩数据
    score = [
        ["张三", 92, 95, 100, 96],
        ["李四", 85, 80, 80, 90],
        ["王二", 95, 90, 89, 95],
        ["小刚", 88, 92, 96, 93]
    ]
    score = pd.DataFrame(score, columns=['姓名', '语文', '数学', '计算机', '英语'])

    result = score.describe(include='number')

    return result


def task2():
    '''
    任务：使用统计描述描述函数求各科目成绩的中位数；
    '''
    # 创建学生成绩数据
    score = [
        ["张三", 92, 95, 100, 96],
        ["李四", 85, 80, 80, 90],
        ["王二", 95, 90, 89, 95],
        ["小刚", 88, 92, 96, 93]
    ]
    score = pd.DataFrame(score, columns=['姓名', '语文', '数学', '计算机', '英语'])

    result = score.median(axis=1)

    return result
