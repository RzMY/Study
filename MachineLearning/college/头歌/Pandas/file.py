import pandas as pd
# pandas版本原因显示，设置列名仅显示4列
pd.set_option('display.max_columns', 4)


def task():
    '''
    任务要求：实现使用Pandas读取gbk编码的文件（"FileHandling/Books.csv"），然后将数据写入到utf-8编码的文件中（"FileHandling/Out.csv"）并使用'*'号分隔数据。
    提示1：使用参数encoding指定编码格式（'gbk' 和 'utf-8'）
    提示2：使用参数sep指定数据分隔方式
    '''
    df = pd.read_csv("FileHandling/Books.csv", encoding='gbk')
    df.to_csv("FileHandling/Out.csv", sep='*')