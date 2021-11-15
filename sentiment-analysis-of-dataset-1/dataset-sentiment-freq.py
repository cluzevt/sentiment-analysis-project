import pandas as pd
from sklearn.model_selection import train_test_split

def get_freq(df):
    #print(df.groupby('0').count())
    print(df['0'].value_counts())

df=pd.read_csv('sa_file_processed2.csv',encoding='ISO-8859-1',na_filter=True,na_values='[]', converters={'1': pd.eval})
df.dropna(inplace=True)
df_train,df_test=train_test_split(df,train_size=0.8)

get_freq(df_train)
get_freq(df_test)