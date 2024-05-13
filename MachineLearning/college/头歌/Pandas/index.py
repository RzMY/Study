import pandas as pd
from sklearn import datasets

def demo():
    data = datasets.load_linnerud().data
    col = pd.MultiIndex.from_product([['stage'],['a','b','c']])
    row = pd.MultiIndex.from_product([['A','B','C','D'],['1','2','3','4','5']])
    df = pd.DataFrame(data, index=row, columns=col)
    df = df.transpose()
    df = df.stack()
    
    idx = pd.IndexSlice
    selected_data = df.loc[idx[:, :, '2'], :]
    print(selected_data)
    
if __name__ == '__main__':
    demo()