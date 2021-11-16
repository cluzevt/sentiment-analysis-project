import pandas as pd
from ast import literal_eval

df=pd.read_csv('../dataset/Tweets.csv', encoding='ISO-8859-1',na_filter=True,na_values='[]', converters={"1": literal_eval})

#dataset was shuffled before saving

#print(df.groupby('0').count())
print(df['airline_sentiment'].value_counts())