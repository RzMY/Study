import pandas as pd

data = {'a': pd.Series([90,82,78.0,78.0], index=['A', 'B', 'C', 'D']),
    'b': pd.Series([89,95,67.0,67.0], index=['A', 'B', 'C', 'D']),
    'c': pd.Series([78,92], index=['A', 'B'])}
df1 = pd.DataFrame(data).transpose()

df1 = df1.applymap(lambda x: int(x) if x == x // 1 else x)

print(df1)