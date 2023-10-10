import pandas as pd

#df = pd.DataFrame({"c1":[1,2,3], "c2":[0,0,0], "c3":[9,8,7]})
#df.to_csv('./test.csv')
def func(path):
    df = pd.read_csv(path)
    df.drop('c2',axis=1,inplace=True)
    df['c1'] += df['c3']
    return df

if __name__ == "__main__":
    df = pd.read_csv('./test.csv')
    print(df)
    df = func('./test.csv')
    print(df)




