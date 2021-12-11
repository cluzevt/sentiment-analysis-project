import pandas as pd
from sklearn.utils import shuffle
import  preprocess
from ast import literal_eval


def  df_modification():
    df = pd.read_csv('../Tweets-pnn.csv', encoding='ISO-8859-1',converters={"1": literal_eval})
    #df = df.head(100)
    df.drop(df.columns.difference(['text','airline_sentiment']), 1, inplace=True)


    df['airline_sentiment'].loc[(df['airline_sentiment'] == "positive")] = 1
    df['airline_sentiment'].loc[(df['airline_sentiment'] == 'negative')] = -1
    df['airline_sentiment'].loc[(df['airline_sentiment'] == 'neutral')] = 0
    df.rename(columns={'text': '1', 'airline_sentiment': '0'}, inplace=True)


    #df = df.drop(df.columns[0], axis=1)

    print(df.head())


    df=shuffle(df)
    df.reset_index(inplace=True,drop=True)
    #print(df.head(5))
    # print(list(df))
    for i in df.index:
        #print(i)
        df['1'][i]=preprocess.preprocess_tweet(df['1'][i])
    #print(df.head(10))
    df.to_csv('../dataset_modified_2/Tweets-pnn-mod.csv')

df_modification()