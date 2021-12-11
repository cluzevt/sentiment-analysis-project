import pandas as pd
from sklearn.utils import shuffle
import  preprocess
from ast import literal_eval


def  df_modification(df):
    df.rename(columns={df.columns[0]: "s"}, inplace=True)
    df.rename(columns={df.columns[5]: "t"}, inplace=True)
    #df = df.head(100)
    df.drop(df.columns.difference(['s','t']), 1, inplace=True)
    df = shuffle(df)

    df['s'].loc[(df['s'] == 0)] = -1
    df['s'].loc[(df['s'] == 4)] = 1
    df = df[df.s != 2]

    df=shuffle(df)
    df.to_csv('modified_csv.csv')

df = pd.read_csv('kaggle_million.csv', encoding='ISO-8859-1',converters={"1": literal_eval})
df_modification(df)