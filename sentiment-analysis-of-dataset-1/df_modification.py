import pandas as pd
from sklearn.utils import shuffle
import  preprocess


def  df_modification():
    df = pd.read_csv('sentiment2.csv', encoding='ISO-8859-1')
    #df = df.head(100)
    df = df.drop(df.columns[0], axis=1)
    df=shuffle(df)
    df.reset_index(inplace=True,drop=True)
    #print(df.head(5))
    # print(list(df))
    for i in df.index:
        #print(i)
        df['1'][i]=preprocess.preprocess_tweet(df['1'][i])
    #print(df.head(10))
    df.to_csv('sa_file_processed_three_tuples.csv')

df_modification()