import pandas as pd
import argparse


def func(path,col):
    df = pd.read_csv(path)
    df.drop(df.columns[col],axis=1,inplace=True)
    df.iloc[:,1] += df.iloc[:,2]
    return df

parser = argparse.ArgumentParser()
parser.add_argument('--path',type=str,help='The path of csv file')
parser.add_argument('--col',type=int,help='The index of column which is about to be delete')
args = parser.parse_args()

if __name__ == '__main__':
    print(func(args.path, args.col))
