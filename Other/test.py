import pandas as pd
import numpy as np

# 创建一个50行3列的DataFrame，第一列和第三列是随机生成的电阻和电阻变化率，第二列为空
df = pd.DataFrame({
    '电阻': np.random.rand(50),
    '': np.nan,
    '电阻变化率': np.random.rand(50)
})

# 将DataFrame写入CSV文件
df.to_csv('H:\\Study\\Study\\Other\\test.csv', index=False)