import pandas as pd

# 创建一个Pandas DataFrame
books_data = {
    "书名": ["Python编程", "编码", "算法（第4版）", "深入理解计算机系统（原书第2版）", "C++ Primer 中文版（第 5 版）", "算法导论（原书第3版）"],
    "作者": ["[美] 埃里克·马瑟斯", "[美] Charles Petzold", "塞奇威克 (Robert Sedgewick)", "（美）Randal E.Bryant", "[美] Stanley B. Lippman", "Thomas H.Cormen"],
    "出版社": ["人民邮电出版社", "电子工业出版社", "人民邮电出版社", "机械工业出版社", "电子工业出版社", "机械工业出版社"],
    "出版年": ["2016/7/1", "2010", "2012/10/1", "2011/1/1", "2013/9/1", "Dec-12"],
    "页数": [459, 392, 636, 702, 838, 780],
    "定价": ["89.00元", "55.00元", "99.00元", "99.00元", "128元", "128.00元"],
    "豆瓣评分": [9.1, 9.3, 9.4, 9.7, 9.4, 9.2]
}

books = pd.DataFrame(books_data)
# pandas版本原因显示，设置列名仅显示4列
pd.set_option('display.max_columns', 4)

DataFrame = pd.DataFrame


def task1(Books: DataFrame) -> DataFrame:
    '''
    参数：图书列表
    任务：添加新图书【书名: 算法图解, 作者: [美] Aditya Bhargava, 出版社: 人民邮电出版社, 出版年: 2017-3, 页数: 196, 定价: 49.00元, 豆瓣评分: 8.4】；
    '''
    Books = Books._append({"书名": "算法图解", "作者": "[美] Aditya Bhargava", "出版社": "人民邮电出版社", "出版年": "2017-3", "页数": 196, "定价": "49.00元", "豆瓣评分": 8.4}, ignore_index=True)
    return Books


def task2(Books: DataFrame) -> DataFrame:
    '''
    参数：图书列表
    任务：删除页数列的数据；
    '''
    Books = Books.drop('页数', axis=1)
    return Books


def task3(Books: DataFrame) -> DataFrame:
    '''
    参数：图书列表
    任务：修改《算法导论（原书第3版）》的价格为666元；
    提示：注意数据格式是字符串格式哦；
    '''
    Books.loc[5, '定价'] = '666元'
    return Books


def task4(Books: DataFrame) -> DataFrame:
    '''
    参数：图书列表
    任务：查询所有图书的豆瓣评分；
    '''
    Books = Books.loc[:, ['书名', '豆瓣评分']]
    return Books

def main():
    print(books)
    print(task1(books))
    print(task2(books))
    print(task3(books))
    print(task4(books))
    
if __name__ == '__main__':
    main()