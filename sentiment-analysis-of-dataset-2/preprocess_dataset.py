import pandas as pd
from sklearn.utils import shuffle
df=pd.read_csv('dataset/Tweets.csv',encoding='ISO-8859-1')
df=shuffle(df)
df=df.rename(columns={'airline_sentiment':'0','text':'1'})

#df.drop(df.loc[df['0']=='neutral'].index,inplace=True)
df['0'].loc[df['0']=='neutral']=0
df['0'].loc[df['0']=='positive']=1
df['0'].loc[df['0']=='negative']=-1

df=df.filter(['0','1'])

df.to_csv('dataset-2-1.csv')